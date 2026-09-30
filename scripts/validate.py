"""Repository validation. Standard library only. Run: python scripts/validate.py"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ["spec-generator", "pr-reviewer", "test-plan-generator"]
REQUIRED = [
    "AGENTS.md", "README.md", "CONTRIBUTING.md", "constitution.md",
    "docs/standards.md", "docs/open-questions.md",
    "specs/TEMPLATE.md", "plans/TEMPLATE.md", "tasks/TEMPLATE.md",
    "review/change-template.md", "scripts/validate.py", ".gitignore",
] + [f"skills/{s}/SKILL.md" for s in SKILLS] + [f"skill-runs/{s}.md" for s in SKILLS]
SKILL_HEADINGS = ["## Purpose and when to use it", "## Required inputs", "## Steps",
                  "## Stop conditions", "## Output format", "## Quality checks", "## Example"]
SPEC_HEADINGS = ["## Problem", "## Scope", "## Out of Scope", "## Requirements",
                 "## Acceptance Criteria", "## Security and Dependencies",
                 "## Open Questions", "## Human approval"]
REVIEW_QUESTIONS = [
    "Is an approved specification linked?", "Is the change within scope?",
    "Are acceptance criteria covered by tests?", "Did validation pass?",
    "Are secrets absent?", "Are dependencies justified?",
    "Are protected paths unchanged or approved?", "Are relevant documents updated?",
]
MANIFESTS = ["package.json", "requirements.txt", "pyproject.toml", "Pipfile", "go.mod",
             "Cargo.toml", "pom.xml", "build.gradle", "Gemfile", "composer.json"]
SECRET_PATTERNS = [
    re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(sk|pk)_(live|test)_[0-9A-Za-z]{16,}"),
    re.compile(r"gh[pousr]_[0-9A-Za-z]{30,}"),
    re.compile(r"(?i)(password|secret|api_key|token)\s*[:=]\s*['\"][^'\"<>\s]{8,}['\"]"),
]
LINK = re.compile(r"\]\(([^)#\s]+)(#[^)]*)?\)")
CODE = re.compile(r"```.*?```|`[^`\n]*`", re.S)
errors = []


def read(rel):
    return (ROOT / rel).read_text(encoding="utf-8")


def tracked_files():
    skip = {".git", ".idea", ".vscode", "__pycache__"}
    for p in ROOT.rglob("*"):
        if p.is_file() and not skip.intersection(p.relative_to(ROOT).parts):
            yield p


def approved_spec_exists():
    for p in (ROOT / "specs").glob("[0-9]*.md"):
        if re.search(r"^Status: Approved\s*$", p.read_text(encoding="utf-8"), re.M):
            return True
    return False


def reviewers():
    section = re.search(r"^## Approved human reviewers\s*$(.*?)(?=^## |\Z)", read("AGENTS.md"), re.M | re.S)
    return set(re.findall(r"^- (.+?)\s*$", section.group(1), re.M)) if section else set()


def check():
    if sys.version_info < (3, 10):
        errors.append(f"Python 3.10 or newer required, found {sys.version.split()[0]}")
    for rel in REQUIRED:
        if not (ROOT / rel).is_file():
            errors.append(f"missing required file: {rel}")
    for d in ["src", "tests"]:
        if not (ROOT / d).is_dir():
            errors.append(f"missing required folder: {d}/")
    if errors:
        return

    agents = read("AGENTS.md")
    governance = [r for r in REQUIRED if r.endswith(".md") and r not in ("AGENTS.md", "README.md")]
    for rel in governance:
        if f"]({rel})" not in agents:
            errors.append(f"AGENTS.md does not link governance doc: {rel}")

    for p in tracked_files():
        if p.suffix != ".md":
            continue
        prose = CODE.sub("", p.read_text(encoding="utf-8"))
        for target, _ in LINK.findall(prose):
            if "://" in target or target.startswith("mailto:") or "NNNN" in target:
                continue
            if not (p.parent / target).resolve().exists():
                errors.append(f"broken link in {p.relative_to(ROOT)}: {target}")

    for s in SKILLS:
        text = read(f"skills/{s}/SKILL.md")
        for h in SKILL_HEADINGS:
            if h not in text:
                errors.append(f"skills/{s}/SKILL.md missing heading: {h}")
        run = read(f"skill-runs/{s}.md")
        for h in ["## Input", "## Output"]:
            if h not in run:
                errors.append(f"skill-runs/{s}.md missing heading: {h}")

    review, reviewer = read("review/change-template.md"), read("skills/pr-reviewer/SKILL.md")
    for q in REVIEW_QUESTIONS:
        if q not in review:
            errors.append(f"review/change-template.md missing question: {q}")
        if q not in reviewer:
            errors.append(f"pr-reviewer SKILL.md missing checklist question: {q}")

    if read("constitution.md").count("In practice, this means") != 7:
        errors.append("constitution.md must have exactly 7 'In practice, this means' lines")

    allowed = reviewers()
    if not allowed:
        errors.append("AGENTS.md lists no approved human reviewers")
    for p in (ROOT / "specs").glob("*.md"):
        text = p.read_text(encoding="utf-8")
        for h in SPEC_HEADINGS:
            if h not in text:
                errors.append(f"{p.relative_to(ROOT)} missing heading: {h}")
        m = re.search(r"^Status: (\S.*?)\s*$", text, re.M)
        if not m or m.group(1) not in ("Draft", "In Review", "Approved", "Rejected"):
            errors.append(f"{p.relative_to(ROOT)} has invalid or missing Status")
        elif m.group(1) in ("Approved", "Rejected"):
            name = re.search(r"^- Approved by: *(.*?)\s*$", text, re.M)
            if not name or name.group(1) not in allowed or not re.search(r"^- Date: *\d{4}-\d{2}-\d{2}", text, re.M):
                errors.append(f"{p.relative_to(ROOT)} is {m.group(1)} without an approved reviewer name and date")

    for line in read("docs/open-questions.md").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 4 or not re.fullmatch(r"Q\d+", cells[0]):
            continue
        answer, resolved = cells[2], cells[3]
        if answer or resolved:
            m = re.fullmatch(r"(.+?),\s*(\d{4}-\d{2}-\d{2})", resolved)
            if not answer or not m or m.group(1) not in allowed:
                errors.append(f"docs/open-questions.md {cells[0]} needs an answer plus an approved reviewer name and date")

    approved_numbers = {p.name[:4] for p in (ROOT / "specs").glob("[0-9]*.md")
                        if re.search(r"^Status: Approved\s*$", p.read_text(encoding="utf-8"), re.M)}
    for d in ["plans", "tasks"]:
        for p in (ROOT / d).glob("[0-9]*.md"):
            if p.name[:4] not in approved_numbers:
                errors.append(f"{p.relative_to(ROOT)} has no matching Approved spec {p.name[:4]}")

    has_approved = approved_spec_exists()
    for d in ["src", "tests"]:
        extra = [p for p in (ROOT / d).rglob("*") if p.is_file() and p.name != ".gitkeep"]
        if extra and not has_approved:
            errors.append(f"{d}/ contains files but no spec is Approved: {extra[0].relative_to(ROOT)}")

    for p in tracked_files():
        if p.name in MANIFESTS and not has_approved:
            errors.append(f"dependency manifest without an approved spec: {p.relative_to(ROOT)}")
        if p.name == ".env" or p.suffix in (".pem", ".key"):
            errors.append(f"secret-like file present: {p.relative_to(ROOT)}")
        if p.suffix in (".png", ".jpg", ".ico", ".zip") or p.name == "validate.py":
            continue
        try:
            text = p.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        for n, line in enumerate(text.splitlines(), 1):
            if any(pat.search(line) for pat in SECRET_PATTERNS):
                errors.append(f"possible secret: {p.relative_to(ROOT)}:{n}")


if __name__ == "__main__":
    check()
    for e in errors:
        print(f"FAIL: {e}")
    print("VALIDATION FAILED" if errors else "VALIDATION PASSED")
    sys.exit(1 if errors else 0)
