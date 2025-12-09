#!/bin/bash

# Leetcode Note Creation Script
# This script creates a leetcode problem note from the template
# Usage: ./create_leetcode_note.sh "Problem Name"

# Check if problem name is provided
if [ -z "$1" ]; then
    echo "Error: Problem name is required!"
    echo "Usage: ./create_leetcode_note.sh \"Problem Name\""
    exit 1
fi

PROBLEM_NAME="$1"

# Define paths
BASE_DIR="Interviewing Note/Leetcode"
TEMPLATE_FILE="LeetcodeTemplates.md"
NOTE_FILE="$BASE_DIR/${PROBLEM_NAME}.md"

# Check if template exists
if [ ! -f "$TEMPLATE_FILE" ]; then
    echo "Error: Template file '$TEMPLATE_FILE' not found!"
    exit 1
fi

# Create directory structure if it doesn't exist
mkdir -p "$BASE_DIR"

# Check if note already exists
if [ -f "$NOTE_FILE" ]; then
    echo "Note for '$PROBLEM_NAME' already exists at: $NOTE_FILE"
    echo "Opening existing note..."
    if command -v code &> /dev/null; then
        code "$NOTE_FILE"
    elif command -v open &> /dev/null; then
        open "$NOTE_FILE"
    fi
    exit 0
fi

# Create the note from template by replacing <NAME> with the problem name
sed "s/<NAME>/$PROBLEM_NAME/" "$TEMPLATE_FILE" > "$NOTE_FILE"

echo "✅ Leetcode note created successfully!"
echo "📝 Location: $NOTE_FILE"
echo "📋 Problem: $PROBLEM_NAME"

# Open the file in the default editor
if command -v code &> /dev/null; then
    code "$NOTE_FILE"
elif command -v open &> /dev/null; then
    open "$NOTE_FILE"
else
    echo "Note created at: $NOTE_FILE"
fi
