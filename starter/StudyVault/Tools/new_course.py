#!/usr/bin/env python3
"""Copy the Obsidian course blueprint without modifying Home or an existing course."""

import argparse
import json
from pathlib import Path
import re
import shutil


VAULT = Path(__file__).resolve().parent.parent
BLUEPRINT = VAULT / "Blueprints" / "Blank-Course"
COURSES = VAULT / "Courses"


def main() -> None:
    """Create one course directory and print its link for Home.md."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("course_id", help="course and term, for example STA302-2026F")
    parser.add_argument("--title", required=True, help="course title")
    args = parser.parse_args()

    course_id = args.course_id
    title = args.title.strip()
    if not re.fullmatch(r"[A-Za-z0-9]+(?:[-_][A-Za-z0-9]+)*", course_id):
        parser.error("course_id must use letters, numbers, hyphens or underscores")
    if not title or any(char in title for char in "\r\n[]|"):
        parser.error("title must be a single line without square brackets or vertical bars")

    if not (BLUEPRINT / "Course.md").is_file():
        parser.exit(1, f"Course blueprint is missing: {BLUEPRINT}\n")

    destination = COURSES / course_id
    try:
        COURSES.mkdir(exist_ok=True)
        destination.mkdir()
    except FileExistsError:
        parser.exit(1, f"Course already exists or a file blocks its path: {destination}\n")
    except OSError as error:
        parser.exit(1, f"Could not create the course directory: {error}\n")

    try:
        shutil.copytree(BLUEPRINT, destination, dirs_exist_ok=True, ignore=shutil.ignore_patterns(".DS_Store"))
        for note in destination.rglob("*.md"):
            content = note.read_text(encoding="utf-8")
            content = content.replace('"COURSE-ID"', json.dumps(course_id))
            content = content.replace('"COURSE-TITLE"', json.dumps(title, ensure_ascii=False))
            content = content.replace("# COURSE-TITLE\n", f"# {title}\n")
            note.write_text(content, encoding="utf-8")
    except (OSError, UnicodeError) as error:
        shutil.rmtree(destination, ignore_errors=True)
        parser.exit(1, f"Could not build the course: {error}\n")

    course_code = re.split(r"[-_]", course_id, maxsplit=1)[0]
    print(f"Created {destination.relative_to(VAULT)}/Course.md")
    print("Paste this line into Home.md:")
    print(f"- [[Courses/{course_id}/Course|{course_code} · {title}]]")


if __name__ == "__main__":
    main()
