#!/bin/bash

# Daily Note Creation Script
# This script creates a daily note file from the template,
# organized by year and month in reverse chronological order

# Get the current date
CURRENT_DATE=$(date +"%Y-%m-%d")
CURRENT_YEAR=$(date +"%Y")
CURRENT_MONTH=$(date +"%m")
FORMATTED_DATE=$(date +"%B %d, %Y")

# Define paths
BASE_DIR="Daily Notes"
YEAR_DIR="$BASE_DIR/$CURRENT_YEAR"
MONTH_DIR="$YEAR_DIR/$CURRENT_MONTH"
NOTE_FILE="$MONTH_DIR/$CURRENT_DATE.md"
TEMPLATE_FILE="DailyNoteTemplates.md"

# Check if template exists
if [ ! -f "$TEMPLATE_FILE" ]; then
    echo "Error: Template file '$TEMPLATE_FILE' not found!"
    exit 1
fi

# Create directory structure if it doesn't exist
mkdir -p "$MONTH_DIR"

# Check if note already exists
if [ -f "$NOTE_FILE" ]; then
    echo "Note for $FORMATTED_DATE already exists at: $NOTE_FILE"
    echo "Opening existing note..."
    open "$NOTE_FILE"
    exit 0
fi

# Create the note from template
sed "s/<Add the current date>/$FORMATTED_DATE/" "$TEMPLATE_FILE" > "$NOTE_FILE"

echo "✅ Daily note created successfully!"
echo "📝 Location: $NOTE_FILE"
echo "📅 Date: $FORMATTED_DATE"

# Open the file in the default editor (optional)
if command -v code &> /dev/null; then
    code "$NOTE_FILE"
elif command -v open &> /dev/null; then
    open "$NOTE_FILE"
else
    echo "Note created at: $NOTE_FILE"
fi
