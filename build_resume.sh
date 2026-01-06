#!/usr/bin/env bash
set -euo pipefail

BUILD_DIR="build"
OUTPUT_BASE="evanbosia_resume"
COMMENT=""
FORCE=false
RESET=false

usage() {
  echo "Usage: $0 [-r] [-f] [-m comment]"
  exit 1
}

# Parse arguments
while getopts ":rfm:" opt; do
  case "$opt" in
    r) RESET=true ;;
    f) FORCE=true ;;
    m) COMMENT="$OPTARG" ;;
    *) usage ;;
  esac
done

# Create build directory if missing
mkdir -p "$BUILD_DIR"

# Clear build directory if requested
if $RESET; then
  if ! $FORCE; then
    read -r -p "Clear contents of '$BUILD_DIR'? [y/N] " confirm
    [[ "$confirm" =~ ^[Yy]$ ]] || exit 0
  fi
  rm -rf "${BUILD_DIR:?}/"*
fi

# Sanitize comment for filename (spaces → _, remove unsafe chars)
if [[ -n "$COMMENT" ]]; then
  SAFE_COMMENT=$(echo "$COMMENT" | tr ' ' '_' | tr -cd '[:alnum:]_-')
  OUTPUT_FILE="${OUTPUT_BASE}_${SAFE_COMMENT}.pdf"
else
  OUTPUT_FILE="${OUTPUT_BASE}.pdf"
fi

# Run pandoc
pandoc resume.md \
  --include-in-header=header.tex \
  --pdf-engine=xelatex \
  -o "$BUILD_DIR/$OUTPUT_FILE"
