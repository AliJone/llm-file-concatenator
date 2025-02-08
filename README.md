# File Combiner for LLM Prompting

A Python script that combines multiple files from a directory (and its subdirectories) into a single text file, formatted specifically for Large Language Model (LLM) prompting.

## Features

- Recursively processes all subdirectories
- Maintains directory structure in output
- Supports filtering by file extensions
- Option to include all file types
- Clear file separators and path indicators
- Handles encoding errors gracefully
- Sorts files for consistent output

## Prerequisites

- Python 3.4+
- No external dependencies required

## Installation

1. Clone this repository or download the `combine_files.py` script
2. Ensure you have Python 3.6 or higher installed

## Usage

### Basic Usage (Default Extensions)

```bash
python combine_files.py /path/to/source/directory output.txt
```

This will combine common text files (`.txt`, `.py`, `.js`, `.jsx`, `.ts`, `.tsx`, `.html`, `.css`, `.md`, `.json`, `.yaml`, `.yml`, `.csv`)

### Specify File Extensions

```bash
python combine_files.py /path/to/source/directory output.txt --extensions py js tsx
```

### Include All Files

```bash
python combine_files.py /path/to/source/directory output.txt --all
```

## Output Format

The script generates a formatted text file that looks like this:

```
Combined files from directory: /absolute/path/to/source
================================================================================

FILE: src/components/Button.tsx
--------------------------------------------------------------------------------
[file content here]

================================================================================

FILE: src/utils/helpers.js
--------------------------------------------------------------------------------
[file content here]

================================================================================
```

## Command Line Arguments

- `input_dir`: Path to the input directory (required)
- `output_file`: Path to the output file (required)
- `--extensions`: List of file extensions to include (optional)
- `--all`: Include all files regardless of extension (optional)

## Error Handling

- The script will skip binary files and files that cannot be read as text
- Error messages will be printed for skipped files
- If both `--all` and `--extensions` flags are used, `--all` takes precedence

## Use Cases

- Preparing codebase for LLM analysis
- Code documentation and review
- Project archival
- Creating training data for LLMs
- Sharing code context in a single file

## Notes

- Binary files and files that cannot be read as text will be skipped automatically
- File paths in the output are relative to the input directory
- Files are sorted alphabetically for consistent output
- Each file's content is clearly separated with path information and dividers

## Contributing

Feel free to submit issues and enhancement requests!
