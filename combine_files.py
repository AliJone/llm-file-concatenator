import os
from pathlib import Path
import argparse

def combine_files(input_dir: str, output_file: str, file_extensions: list = None, include_all: bool = False):
    """
    Combines all text files from a directory (and its subdirectories) into a single file,
    formatted for LLM prompting.
    
    Args:
        input_dir (str): Path to the input directory
        output_file (str): Path to the output file
        file_extensions (list): List of file extensions to include (e.g., ['.txt', '.py', '.js'])
                              If None, includes common text files
        include_all (bool): If True, includes all files regardless of extension
    """
    # Convert to Path object for easier handling
    input_path = Path(input_dir).resolve()
    
    # If no extensions specified and not including all, use common text file extensions
    if file_extensions is None and not include_all:
        file_extensions = ['.txt', '.py', '.js', '.jsx', '.ts', '.tsx', '.html', 
                         '.css', '.md', '.json', '.yaml', '.yml', '.csv']
    
    # Ensure extensions start with dot if extensions are specified
    if file_extensions:
        file_extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in file_extensions]
    
    with open(output_file, 'w', encoding='utf-8') as outfile:
        outfile.write(f"Combined files from directory: {input_path}\n")
        outfile.write("="*80 + "\n\n")
        
        # Walk through directory
        for root, _, files in os.walk(input_path):
            # Sort files for consistent output
            for filename in sorted(files):
                file_path = Path(root) / filename
                
                # Skip files if they don't match the extension criteria
                if not include_all:
                    if not any(file_path.name.endswith(ext) for ext in file_extensions):
                        continue
                
                try:
                    # Get relative path from input directory
                    rel_path = file_path.relative_to(input_path)
                    
                    # Try to read file as text
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        
                        # Write file path and separator
                        outfile.write(f"FILE: {rel_path}\n")
                        outfile.write("-"*80 + "\n\n")
                        
                        # Write content
                        outfile.write(content)
                        
                        # Add newlines between files
                        outfile.write("\n\n")
                        outfile.write("="*80 + "\n\n")
                        
                except (UnicodeDecodeError, IOError) as e:
                    print(f"Skipping {file_path}: {str(e)}")
                    continue

def main():
    parser = argparse.ArgumentParser(description='Combine text files for LLM prompting')
    parser.add_argument('input_dir', help='Input directory path')
    parser.add_argument('output_file', help='Output file path')
    parser.add_argument('--extensions', nargs='+', help='File extensions to include (e.g., txt py js)')
    parser.add_argument('--all', action='store_true', help='Include all files regardless of extension')
    
    args = parser.parse_args()
    
    if args.all and args.extensions:
        print("Warning: --all flag is used, ignoring specified extensions")
    
    # Convert extensions list
    extensions = [f'.{ext.lstrip(".")}' for ext in args.extensions] if args.extensions and not args.all else None
    
    combine_files(args.input_dir, args.output_file, extensions, args.all)
    print(f"Files combined successfully into {args.output_file}")

if __name__ == "__main__":
    main()