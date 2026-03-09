#!/usr/bin/env python3
"""
Auto-generate a Table of Contents for any Markdown file.

Usage:
    python generate_toc.py <file.md>              # Preview TOC in terminal
    python generate_toc.py <file.md> --insert     # Insert/update TOC in the file
"""

import re
import sys
import argparse


def slugify(text):
    """Convert header text to a GitHub-compatible anchor slug."""
    text = text.lower()
    text = re.sub(r'[^\w\s-]', '', text)   # Remove special characters
    text = re.sub(r'\s+', '-', text.strip()) # Replace spaces with hyphens
    text = re.sub(r'-+', '-', text)          # Collapse multiple hyphens
    return text


def extract_headers(lines):
    """Extract all markdown headers from lines, skipping code blocks."""
    headers = []
    in_code_block = False

    for line in lines:
        if line.startswith('```'):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue

        match = re.match(r'^(#{1,6})\s+(.*)', line.rstrip())
        if match:
            level = len(match.group(1))
            title = match.group(2).strip()
            headers.append((level, title))

    return headers


def generate_toc(headers):
    """Generate TOC lines from extracted headers."""
    toc_lines = ['## Table of Contents\n']
    slug_counts = {}

    for level, title in headers:
        # Skip the TOC header itself
        if title.lower() in ('table of contents', 'toc', 'contents'):
            continue

        slug = slugify(title)

        # Handle duplicate anchors (GitHub appends -1, -2, etc.)
        if slug in slug_counts:
            slug_counts[slug] += 1
            slug = f"{slug}-{slug_counts[slug]}"
        else:
            slug_counts[slug] = 0

        indent = '  ' * (level - 1)
        toc_lines.append(f'{indent}- [{title}](#{slug})\n')

    return toc_lines


def insert_toc(lines, toc_lines):
    """Insert or replace TOC in the file lines."""
    toc_start_pattern = re.compile(r'^##\s+Table of Contents', re.IGNORECASE)
    toc_entry_pattern = re.compile(r'^\s*-\s+\[.*\]\(#.*\)')

    # Find existing TOC block
    start_idx = None
    end_idx = None
    for i, line in enumerate(lines):
        if toc_start_pattern.match(line.strip()):
            start_idx = i
        elif start_idx is not None and end_idx is None:
            if not toc_entry_pattern.match(line) and line.strip() != '':
                end_idx = i
                break

    if end_idx is None and start_idx is not None:
        end_idx = len(lines)

    if start_idx is not None:
        # Replace existing TOC
        updated = lines[:start_idx] + toc_lines + ['\n'] + lines[end_idx:]
    else:
        # Insert after the first H1 header (or at the top if none found)
        insert_pos = 0
        for i, line in enumerate(lines):
            if re.match(r'^#\s+', line):
                insert_pos = i + 1
                break
        updated = lines[:insert_pos] + ['\n'] + toc_lines + ['\n'] + lines[insert_pos:]

    return updated


def main():
    parser = argparse.ArgumentParser(description='Auto-generate Table of Contents for Markdown files.')
    parser.add_argument('file', help='Path to the markdown file')
    parser.add_argument('--insert', action='store_true', help='Insert or update TOC directly in the file')
    args = parser.parse_args()

    try:
        with open(args.file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"Error: File '{args.file}' not found.")
        sys.exit(1)

    headers = extract_headers(lines)

    if not headers:
        print("No headers found in the file.")
        sys.exit(0)

    toc_lines = generate_toc(headers)

    if args.insert:
        updated_lines = insert_toc(lines, toc_lines)
        with open(args.file, 'w', encoding='utf-8') as f:
            f.writelines(updated_lines)
        print(f"✅ TOC inserted/updated in '{args.file}'")
    else:
        print("Generated Table of Contents:\n")
        print(''.join(toc_lines))


if __name__ == '__main__':
    main()