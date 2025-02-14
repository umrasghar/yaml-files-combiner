# YAML Files Combiner

A simple, lightweight tool to combine multiple YAML files into a single text file with proper formatting and file separation.

## Features

- Combines multiple .yml/.yaml files into a single text file
- Adds clear separators and file names as comments
- Generates timestamped output files
- Works on Windows, Linux, and macOS
- No external dependencies required
- UTF-8 encoding support
- Error handling for corrupted or inaccessible files

## Installation

No installation required! Just download the script and run it with Python 3.x.

```bash
git clone https://github.com/umrasghar/yaml-files-combiner.git
cd yaml-files-combiner
```

## Usage

There are two ways to use the tool:

1. **Simple way** - Double-click the script:
   - Put the script in the folder with your YAML files
   - Double-click `combine_yaml.py`
   - Find the combined file in the same directory

2. **Command line** - Specify a directory:
   ```bash
   python combine_yaml.py "path/to/your/yaml/files"
   ```

## Output

The tool will create a file named `combined_yaml_TIMESTAMP.txt` containing:
- A header with generation timestamp
- All YAML files' contents
- Clear separators between files
- Original file names as comments

## Error Handling

- Gracefully handles missing files
- Reports encoding issues
- Continues processing even if some files fail
- Clear error messages in the output

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

UMAR ASGHAR

## Acknowledgments

- Thanks to everyone who contributes to making open source software accessible
- Built with Python 3
