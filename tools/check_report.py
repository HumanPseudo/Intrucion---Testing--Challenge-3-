#!/usr/bin/env python3
"""Verification checks for the Challenge 3 defensive-design report.

Checks the deliverable against the rubric (C1 format, C3 integrity) and reports
the running body word count, which must stay between 6,000 and 8,000 words
excluding the reference list.

Usage
-----
    python3 tools/check_report.py            # all checks
    python3 tools/check_report.py --wordcount # word count only (per-section breakdown)

Exit codes
----------
    0  all hard checks passed
    1  at least one hard check failed
"""

from __future__ import annotations

import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOC_MD = ROOT / "report" / "doc.md"
DOCX = ROOT / "report" / "report.docx"

WORD_MIN = 6000
WORD_MAX = 8000

SECTION_TITLES = [
    "1. Introduction and scope of defensive design",
    "2. Synthesis of the Challenge 2 offensive analysis",
    "3. Risk prioritization matrix",
    "4. Traceability matrix: vector to control",
    "5. Design of defensive controls",
    "6. Monitoring and detection proposal",
    "7. DevSecOps proposal",
    "8. Incident response plan",
    "9. Validation criteria for Challenge 4",
    "10. Conclusions and references",
]

TABLE_COUNT = 13

# --------------------------------------------------------------------------- #
# helpers
# --------------------------------------------------------------------------- #


def strip_frontmatter(text: str) -> str:
    return re.sub(r"\A---.*?---\n", "", text, flags=re.S)


def body_of_markdown(text: str) -> tuple[str, str]:
    """Return (body, references) split at the reference list.

    The body is everything from section 1 up to the reference list; the
    reference list and the AI-usage appendix are excluded from the word count.
    """
    text = strip_frontmatter(text)
    start = text.find("# 1. Introduction")
    ref = text.find("## References")
    if start < 0 or ref < 0:
        return text, ""
    return text[start:ref], text[ref:]


def count_words(text: str) -> int:
    """Count words the way Word does: whitespace-separated tokens that contain
    at least one alphanumeric character. Markdown markers are removed first;
    table separator rows carry no alphanumerics and are therefore ignored."""
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", r"\1", text)      # images -> alt text
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)        # links -> label
    text = re.sub(r"[*_`#>|]", " ", text)                       # inline markers
    tokens = [t for t in text.split() if re.search(r"[0-9A-Za-zÁÉÍÓÚÜÑáéíóúüñ]", t)]
    return len(tokens)


def section_breakdown(body: str) -> list[tuple[str, int]]:
    """Word count per top-level section, in document order."""
    parts = re.split(r"\n(?=# )", body)
    out = []
    for part in parts:
        first = part.split("\n", 1)[0].lstrip("# ").strip()
        if not first:
            continue
        out.append((first, count_words(part)))
    return out


def docx_body_words() -> int | None:
    """Word count of the rendered .docx body (sections 1-10), i.e. what the
    evaluator sees in Word when selecting the body without the references."""
    if not DOCX.exists():
        return None
    try:
        with zipfile.ZipFile(DOCX) as zf:
            xml = zf.read("word/document.xml").decode("utf-8")
    except (KeyError, zipfile.BadZipFile):
        return None
    paras = re.findall(r"<w:p[ >].*?</w:p>", xml, re.S)
    texts = [
        "".join(re.findall(r"<w:t[^>]*>(.*?)</w:t>", p, re.S)) for p in paras
    ]
    joined = "\n".join(texts)
    # The table of contents repeats every heading: take the last occurrence.
    start = joined.rfind("1. Introduction")
    end = joined.find("References")
    if start < 0 or end < 0 or end < start:
        return None
    return count_words(joined[start:end])


# --------------------------------------------------------------------------- #
# checks
# --------------------------------------------------------------------------- #


class Report:
    def __init__(self) -> None:
        self.fails: list[str] = []
        self.warns: list[str] = []
        self.oks: list[str] = []

    def fail(self, msg: str) -> None:
        self.fails.append(msg)

    def warn(self, msg: str) -> None:
        self.warns.append(msg)

    def ok(self, msg: str) -> None:
        self.oks.append(msg)


def check_word_count(rep: Report, body: str) -> int:
    words = count_words(body)
    docx_words = docx_body_words()

    detail = f"body word count (sections 1-10, references excluded): {words}"
    if docx_words is not None:
        detail += f" / rendered .docx: {docx_words}"
        if abs(docx_words - words) > max(50, int(words * 0.03)):
            rep.warn(
                f"markdown and .docx counts differ by more than 3% ({words} vs "
                f"{docx_words}); measure in Word before submitting"
            )
    rep.ok(detail)

    if words < WORD_MIN:
        rep.fail(
            f"body is {WORD_MIN - words} words short of the {WORD_MIN}-word minimum "
            f"(current: {words})"
        )
    elif words > WORD_MAX:
        rep.fail(
            f"body exceeds the {WORD_MAX}-word maximum by {words - WORD_MAX} words "
            f"(current: {words})"
        )
    else:
        rep.ok(f"body word count is inside the {WORD_MIN}-{WORD_MAX} range")
    return words


def check_sections(rep: Report, body: str) -> None:
    missing = [t for t in SECTION_TITLES if t not in body]
    if missing:
        rep.fail(f"missing section heading(s): {', '.join(missing)}")
    else:
        rep.ok(f"all {len(SECTION_TITLES)} mandatory section headings are present")


def check_tables(rep: Report, body: str) -> None:
    captions = re.findall(r"\*\*Table (\d+)\s+—", body)
    numbers = [int(n) for n in captions]
    if len(numbers) != TABLE_COUNT:
        rep.fail(
            f"expected {TABLE_COUNT} numbered table captions, found {len(numbers)}"
        )
    else:
        rep.ok(f"{TABLE_COUNT} numbered table captions found")
    if numbers and numbers != list(range(1, len(numbers) + 1)):
        rep.fail(f"table numbering is not sequential: {numbers}")
    for n in numbers:
        if len(re.findall(rf"Table {n}\b", body)) < 2:
            rep.warn(f"Table {n} is never referenced in the text")


def check_placeholders(rep: Report, body: str) -> None:
    cells = len(re.findall(r"\[\.\.\]", body))
    blocks = len(re.findall(r"to complete", body, re.I))
    if cells or blocks:
        rep.fail(
            f"draft placeholders left: {cells} empty table cell(s) '[..]' and "
            f"{blocks} 'to complete' note(s)"
        )
    else:
        rep.ok("no draft placeholders left in the body")


def check_no_images(rep: Report, body: str) -> None:
    images = re.findall(r"!\[[^\]]*\]\([^)]*\)", body)
    if images:
        rep.fail(
            f"{len(images)} image(s) found; the rubric forbids screenshots or "
            f"image-tables as a substitute for editable matrices"
        )
    else:
        rep.ok("no images or image-tables in the body")


def check_symbol(rep: Report, body: str) -> None:
    if "§" in body:
        rep.fail("the section symbol is present in the body")
    else:
        rep.ok("no section symbol in the body")


def check_references(rep: Report, body: str, references: str) -> None:
    raw_entries = re.findall(r"^-\s+(.+)$", references, re.M)
    entries = []
    optional = []
    for raw in raw_entries:
        m = re.match(r"(.+?)\((\d{4}[a-z]?)\)", raw)
        if not m:
            continue
        if "to be verified" in raw.lower():
            optional.append((m.group(1).strip(), m.group(2)))
        else:
            entries.append((m.group(1).strip(), m.group(2)))
    if not entries:
        rep.fail("no reference entries found in the reference list")
        return
    uncited = []
    for author, year in entries:
        surname = re.split(r"[,\s&(]", author.strip())[0].rstrip(".")
        if surname and not re.search(re.escape(surname), body):
            uncited.append(f"{surname} ({year})")
    if uncited:
        rep.warn(
            f"{len(uncited)} listed source(s) never cited in the text: "
            + ", ".join(uncited)
        )
    else:
        rep.ok(f"all {len(entries)} listed sources are cited in the text")

    if optional:
        rep.warn(
            f"{len(optional)} source(s) carry the 'to be verified' caveat "
            "(handle returns 404); citing them in the text is optional: "
            + ", ".join(f"{a.split(',')[0]} ({y})" for a, y in optional)
        )

    in_text = set(re.findall(r"\(([A-ZÁÉÍÓÚÑ][^()]{0,40}?),\s*(?:19|20)\d\d[a-z]?\)", body))
    listed = " ".join(a for a, _ in entries + optional)
    missing = []
    for cite in in_text:
        surname = re.split(r"[,\s&(]", cite.strip())[0]
        if surname and surname not in listed:
            missing.append(cite)
    if missing:
        rep.warn(
            f"{len(missing)} in-text citation(s) without a reference entry: "
            + ", ".join(sorted(missing)[:10])
        )
    else:
        rep.ok("every in-text citation has a reference entry")


FRAMEWORK_MARKERS = (
    "CIS Controls",
    "NIST CSF",
    "NIST SP 800",
    "ISO/IEC 27001",
    "OWASP",
    "MITRE ATT&CK",
    "NVD",
)


def check_source_mix(rep: Report, references: str) -> None:
    """The rubric asks for at least 8 sources: 3 course resources and 3 technical
    frameworks. The two groups are separated by the 'Technical frameworks' heading."""
    entries = re.findall(r"^-\s+(.+)$", references, re.M)
    if len(entries) < 8:
        rep.fail(
            f"only {len(entries)} reference entries; the rubric requires at least 8"
        )
    else:
        rep.ok(f"{len(entries)} reference entries (minimum 8)")

    split = re.search(
        r"^[>#*]*[ \t]*\**[ \t]*Technical frameworks[^\n]*$", references, re.M | re.I
    )
    if split:
        course_block = references[: split.start()]
        framework_block = references[split.end() :]
    else:
        course_block, framework_block = references, references

    course_n = len(re.findall(r"^-\s+", course_block, re.M))
    framework_n = len(re.findall(r"^-\s+", framework_block, re.M))

    if course_n < 3:
        rep.fail(f"only {course_n} course-resource entries; at least 3 are required")
    else:
        rep.ok(f"{course_n} course-resource entries")

    if framework_n < 3:
        rep.fail(
            f"only {framework_n} technical-framework entries; at least 3 are required "
            f"(CIS Controls, NIST CSF, NIST SP 800-61, ISO/IEC 27001, OWASP, "
            f"MITRE ATT&CK are valid)"
        )
    else:
        rep.ok(f"{framework_n} technical-framework entries")

    missing = [
        m
        for m in FRAMEWORK_MARKERS
        if not any(m.lower() in e.lower() for e in re.findall(r"^-\s+(.+)$", framework_block, re.M))
    ]
    if missing and framework_n >= 3:
        rep.warn(
            "technical-framework entries do not mention any of: "
            + ", ".join(missing)
        )


# --------------------------------------------------------------------------- #
# main
# --------------------------------------------------------------------------- #


def main() -> int:
    wordcount_only = "--wordcount" in sys.argv

    if not DOC_MD.exists():
        print(f"ERROR: {DOC_MD} not found")
        return 1

    raw = DOC_MD.read_text(encoding="utf-8")
    body, references = body_of_markdown(raw)
    words = count_words(body)

    if wordcount_only:
        print(f"Body word count (sections 1-10, references excluded): {words}")
        docx_words = docx_body_words()
        if docx_words is not None:
            print(f"Rendered .docx (same slice): {docx_words}")
        print(f"Target: {WORD_MIN}-{WORD_MAX} -> ", end="")
        if words < WORD_MIN:
            print(f"{WORD_MIN - words} words still to write")
        elif words > WORD_MAX:
            print(f"{words - WORD_MAX} words over the limit")
        else:
            print("within range")
        print("\nPer section:")
        for title, n in section_breakdown(body):
            print(f"  {n:>6}  {title}")
        return 0 if WORD_MIN <= words <= WORD_MAX else 1

    rep = Report()
    check_word_count(rep, body)
    check_sections(rep, body)
    check_tables(rep, body)
    check_placeholders(rep, body)
    check_no_images(rep, body)
    check_symbol(rep, body)
    check_references(rep, body, references)
    check_source_mix(rep, references)

    print("=" * 72)
    print("CHALLENGE 3 — REPORT VERIFICATION")
    print("=" * 72)
    for msg in rep.oks:
        print(f"  PASS  {msg}")
    for msg in rep.warns:
        print(f"  WARN  {msg}")
    for msg in rep.fails:
        print(f"  FAIL  {msg}")
    print("-" * 72)
    print(f"  {len(rep.fails)} failed / {len(rep.warns)} warnings / {len(rep.oks)} passed")
    print("=" * 72)
    return 1 if rep.fails else 0


if __name__ == "__main__":
    sys.exit(main())
