#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BOOKS_DIR="${1:-"$SCRIPT_DIR/books"}"
OUTPUT_DIR="${2:-"$SCRIPT_DIR/_build/books"}"
BUILD_MODE="${3:-directory}"
GENERATED_ROOT="$SCRIPT_DIR/.jupyter-book-generated"
AGGREGATE_SOURCE_DIR="$GENERATED_ROOT/books-directory"
LOCAL_MYST_TEMPLATE_DIR="${MYST_SITE_TEMPLATE_DIR:-"$SCRIPT_DIR/.myst-templates/book-theme"}"
ANNBOOK_BOOK_TITLE="${ANNBOOK_BOOK_TITLE:-Python Annotated Math}"
ANNBOOK_BOOK_AUTHOR="${ANNBOOK_BOOK_AUTHOR:-Annotated Book}"

usage() {
  cat <<'EOF'
Usage: ./book_generate.sh [BOOKS_DIR] [OUTPUT_DIR] [MODE]

MODE:
  directory  Build one Jupyter Book that contains all notebooks under BOOKS_DIR.
  source     Generate the aggregate Jupyter Book source only; do not build HTML.
  books      Build each direct child directory under BOOKS_DIR as a separate book.

Defaults:
  BOOKS_DIR  ./books
  OUTPUT_DIR ./_build/books
  MODE       directory

Environment:
  ANNBOOK_BOOK_TITLE   Book title for aggregate directory/source builds.
  ANNBOOK_BOOK_AUTHOR  Author name written into generated MyST config.
EOF
}

if [[ "${1:-}" == "-h" || "${1:-}" == "--help" ]]; then
  usage
  exit 0
fi

if command -v jupyter-book >/dev/null 2>&1; then
  JB_CMD=(jupyter-book)
elif python3 -c 'import jupyter_book' >/dev/null 2>&1; then
  JB_CMD=(python3 -m jupyter_book)
else
  echo "Error: jupyter-book is not installed." >&2
  echo "Install it with: python3 -m pip install -U jupyter-book" >&2
  exit 1
fi

if [[ ! -d "$BOOKS_DIR" ]]; then
  echo "Error: books directory not found: $BOOKS_DIR" >&2
  exit 1
fi

site_template_for() {
  local book_dir="$1"

  if [[ -f "$LOCAL_MYST_TEMPLATE_DIR/template.yml" ]]; then
    python3 - "$LOCAL_MYST_TEMPLATE_DIR" "$book_dir" <<'PY'
from pathlib import Path
import os
import sys

template_dir = Path(sys.argv[1]).resolve()
book_dir = Path(sys.argv[2]).resolve()
print(Path(os.path.relpath(template_dir, book_dir)).as_posix())
PY
  else
    printf '%s\n' "book-theme"
  fi
}

generate_aggregate_source() {
  local source_dir="$AGGREGATE_SOURCE_DIR"
  local site_template

  rm -rf "$source_dir"
  mkdir -p "$source_dir"
  cp -R "$BOOKS_DIR" "$source_dir/books"
  find "$source_dir/books" -type f -name '*.ipynb' -size 0 -delete

  site_template="$(site_template_for "$source_dir")"
  if [[ "$site_template" != "book-theme" ]]; then
    echo "Using local MyST template: $LOCAL_MYST_TEMPLATE_DIR" >&2
  fi

  python3 - "$source_dir" "$site_template" "$ANNBOOK_BOOK_TITLE" "$ANNBOOK_BOOK_AUTHOR" <<'PY'
import json
import re
import shutil
from collections import defaultdict
from pathlib import Path
import sys

source_dir = Path(sys.argv[1])
site_template = sys.argv[2]
book_title = sys.argv[3]
book_author = sys.argv[4]
books_dir = source_dir / "books"

lesson_name = re.compile(r"^(\d+)-(\d+)_")
lesson_alias = re.compile(r"^(\d+)\.(\d+)\.ipynb$")

for page in sorted(books_dir.rglob("*.ipynb")):
    rel = page.relative_to(books_dir)
    match = lesson_name.match(page.name)
    if (
        match
        and len(rel.parts) >= 2
        and not any(part.startswith((".", "_")) for part in rel.parts)
    ):
        alias = page.with_name(f"{int(match.group(1))}.{int(match.group(2))}.ipynb")
        shutil.copy2(page, alias)

def is_lesson_page(page: Path) -> bool:
    rel = page.relative_to(books_dir)
    return (
        page.suffix.lower() == ".ipynb"
        and len(rel.parts) >= 2
        and not any(part.startswith((".", "_")) for part in rel.parts)
        and lesson_alias.match(page.name) is not None
    )

pages = sorted(
    (p for p in books_dir.rglob("*.ipynb") if is_lesson_page(p)),
    key=lambda p: (
        p.parent.relative_to(books_dir).as_posix(),
        tuple(int(x) for x in lesson_alias.match(p.name).groups()),
        p.name,
    ),
)

if not pages:
    raise SystemExit(f"No lesson notebooks found under {books_dir}")

def title_from_page(page: Path) -> str:
    if page.suffix.lower() == ".ipynb":
        data = json.loads(page.read_text(encoding="utf-8"))
        for cell in data.get("cells", []):
            if cell.get("cell_type") != "markdown":
                continue
            source = "".join(cell.get("source", []))
            for line in source.splitlines():
                if line.startswith("# "):
                    return line[2:].strip()
    for line in page.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return page.stem.replace("_", " ")

groups = defaultdict(list)
for page in pages:
    rel = page.relative_to(books_dir)
    groups[rel.parts[0]].append(page)

index_lines = [
    f"# {book_title} 目录",
    "",
    "本页按年级汇总课程 Notebook。左侧目录使用“年级 -> 小节”的两级结构，便于按教材顺序学习。",
    "",
]

for group_name in sorted(groups):
    index_lines.extend([f"## {group_name}", ""])
    for page in groups[group_name]:
        rel = page.relative_to(source_dir).as_posix()
        index_lines.append(f"- [{title_from_page(page)}]({rel})")
    index_lines.append("")

(source_dir / "index.md").write_text("\n".join(index_lines), encoding="utf-8")
(source_dir / "favicon.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
    '<rect width="64" height="64" rx="12" fill="#1f2937"/>'
    '<text x="32" y="42" text-anchor="middle" font-size="28" fill="#ffffff" '
    'font-family="Arial, sans-serif">π</text>'
    '</svg>\n',
    encoding="utf-8",
)

def rel(path: Path) -> str:
    return path.relative_to(source_dir).as_posix()

myst = [
    "version: 1",
    "project:",
    f"  title: {book_title}",
    "  authors:",
    f"    - name: {book_author}",
    "  toc:",
    "    - file: index.md",
]

for group_name in sorted(groups):
    myst.append(f"    - title: {group_name}")
    myst.append("      children:")
    for page in groups[group_name]:
        myst.append(f"        - file: {rel(page)}")

myst.extend([
    "site:",
    "  options:",
    "    folders: true",
    "    favicon: favicon.svg",
    f"  template: {site_template}",
    "",
])

(source_dir / "myst.yml").write_text("\n".join(myst), encoding="utf-8")
PY

  printf '%s\n' "$source_dir"
}

build_site() {
  local source_dir="$1"
  local output_dir="$2"

  (
    cd "$source_dir"
    "${JB_CMD[@]}" build --html --force
  ) || {
    local status=$?
    if [[ -f "$source_dir/_build/html/index.html" && -d "$source_dir/_build/html/build" ]]; then
      echo "Warning: jupyter-book exited with status $status after producing HTML; continuing." >&2
    else
      return "$status"
    fi
  }

  rm -rf "$output_dir"
  mkdir -p "$output_dir"
  cp -R "$source_dir/_build/html"/. "$output_dir"
}

generate_single_book_source() {
  local book_dir="$1"
  local book_name="$2"
  local source_dir="$GENERATED_ROOT/$book_name"
  local site_template

  rm -rf "$source_dir"
  mkdir -p "$GENERATED_ROOT"
  cp -R "$book_dir" "$source_dir"
  find "$source_dir" -type f -name '*.ipynb' -size 0 -delete

  site_template="$(site_template_for "$source_dir")"

  python3 - "$source_dir" "$book_name" "$site_template" "$ANNBOOK_BOOK_AUTHOR" <<'PY'
from pathlib import Path
import sys

book_dir = Path(sys.argv[1])
book_name = sys.argv[2]
site_template = sys.argv[3]
book_author = sys.argv[4]

pages = sorted(
    p for p in book_dir.rglob("*")
    if p.suffix.lower() in {".ipynb", ".md", ".rst"}
    and not any(part.startswith(("_", ".")) for part in p.relative_to(book_dir).parts)
)

if not pages:
    raise SystemExit(f"No notebook or markdown pages found in {book_dir}")

(book_dir / "favicon.svg").write_text(
    '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
    '<rect width="64" height="64" rx="12" fill="#1f2937"/>'
    '<text x="32" y="42" text-anchor="middle" font-size="28" fill="#ffffff" '
    'font-family="Arial, sans-serif">π</text>'
    '</svg>\n',
    encoding="utf-8",
)

myst = [
    "version: 1",
    "project:",
    f"  title: {book_name}",
    "  authors:",
    f"    - name: {book_author}",
    "  toc:",
]

for page in pages:
    myst.append(f"    - file: {page.relative_to(book_dir).as_posix()}")

myst.extend([
    "site:",
    "  options:",
    "    folders: true",
    "    favicon: favicon.svg",
    f"  template: {site_template}",
    "",
])

(book_dir / "myst.yml").write_text("\n".join(myst), encoding="utf-8")
PY

  printf '%s\n' "$source_dir"
}

case "$BUILD_MODE" in
  directory)
    source_dir="$(generate_aggregate_source)"
    echo "Building notebook directory ..."
    build_site "$source_dir" "$OUTPUT_DIR"
    echo "Done. HTML output is under: $OUTPUT_DIR"
    ;;
  source)
    source_dir="$(generate_aggregate_source)"
    echo "Done. Jupyter Book source is under: $source_dir"
    ;;
  books)
    shopt -s nullglob
    book_dirs=("$BOOKS_DIR"/*/)

    if (( ${#book_dirs[@]} == 0 )); then
      echo "Error: no book directories found under $BOOKS_DIR" >&2
      exit 1
    fi

    for book_dir in "${book_dirs[@]}"; do
      book_dir="${book_dir%/}"
      book_name="$(basename "$book_dir")"
      source_dir="$(generate_single_book_source "$book_dir" "$book_name")"

      echo "Building $book_name ..."
      build_site "$source_dir" "$OUTPUT_DIR/$book_name"
    done

    echo "Done. HTML output is under: ${2:-"$SCRIPT_DIR/_build/books"}"
    ;;
  *)
    echo "Error: unknown build mode: $BUILD_MODE" >&2
    usage >&2
    exit 1
    ;;
esac
