import os
import sys
from datetime import datetime

def combine_yaml_files(directory_path=None):
    # If no directory provided, use the current directory
    if directory_path is None:
        directory_path = os.getcwd()
    
    # Get all .yml files in the directory
    yaml_files = [f for f in os.listdir(directory_path) if f.endswith(('.yml', '.yaml'))]
    
    if not yaml_files:
        print("No YAML files found in the directory!")
        return
    
    # Create output filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = f"combined_yaml_{timestamp}.txt"
    
    try:
        with open(output_file, 'w', encoding='utf-8') as outfile:
            # Write header
            outfile.write(f"# Combined YAML files from {directory_path}\n")
            outfile.write(f"# Generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Process each YAML file
            for yaml_file in sorted(yaml_files):
                file_path = os.path.join(directory_path, yaml_file)
                
                # Write file name as comment
                outfile.write(f"\n{'#' * 80}\n")
                outfile.write(f"# File: {yaml_file}\n")
                outfile.write(f"{'#' * 80}\n\n")
                
                # Read and write content
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content)
                        outfile.write('\n\n')
                except Exception as e:
                    outfile.write(f"# Error reading file {yaml_file}: {str(e)}\n\n")
        
        print(f"\nSuccess! Combined {len(yaml_files)} files into: {output_file}")
        print(f"Output file location: {os.path.abspath(output_file)}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    # Get directory path from command line argument if provided
    directory_path = sys.argv[1] if len(sys.argv) > 1 else None
    combine_yaml_files(directory_path)
