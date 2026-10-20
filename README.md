# Environment Finder [EFinder]
<img width="2032" height="774" alt="image" src="https://github.com/user-attachments/assets/64021c67-3d19-4293-9fbf-673ba17b45a1" />

**Environment Finder v0.1** — A Python-based system information and environment inspection tool developed by **SwiftGlitxh**.

Environment Finder provides a structured overview of your operating system, Python installation, development tools, and environment variables directly from the terminal.

Designed for developers, IT administrators, and cybersecurity enthusiasts who need a quick way to inspect their local system configuration.

## Features

### Operating System Information

- Detect operating system and release version.
- Display system architecture.
- Identify the installed Python version.
- Locate the active Python executable.
- Display the current working directory.
- Check virtual environment status.

### Development Tool Detection

Locate commonly used development tools and executables:

- Git
- Python
- Python 3
- pip
- Node.js
- Docker

Identify whether each tool is available on the system PATH.

### Environment Variable Inspection

Inspect system and user environment variables, including:

- `ALLUSERSPROFILE`
- `APPDATA`
- `COMPUTERNAME`
- `COMSPEC`
- `DRIVERDATA`
- `COMMONPROGRAMFILES`
- Custom application environment variables

Environment Finder can assist with identifying configuration issues, locating installed tools, and troubleshooting development environments.

### Terminal Interface

- Structured tables for easy readability.
- Cyan-themed terminal presentation.
- Clearly separated system information and environment variable sections.
- Lightweight command-line operation.

## Requirements

- Python 3.10 or newer recommended.
- Windows operating system for the environment shown in the screenshot.
- Terminal or command prompt.

**Note:** The screenshot demonstrates Windows functionality. Compatibility with other operating systems has not yet been verified.

## Installation

Clone the repository:

```bash
git clone https://github.com/swiftglitxh/Environment-Finder.git
```

Navigate into the project directory:

```bash
cd Environment-Finder
```

Install dependencies if a `requirements.txt` file is provided:

```bash
pip install -r requirements.txt
```

## Usage

Run the main Python script:

```bash
python environment_finder.py
```

The tool displays available system information, installed development utilities, and environment variables.

*Adjust the filename if your entry-point script has a different name.*

## Security Considerations

**Warning: Environment variables can contain sensitive information.**

These may include:

- API keys and authentication tokens.
- Application secrets.
- Passwords and database credentials.
- Private directory paths.
- Internal system identifiers.

Never publish unredacted terminal output without inspecting it first.

For safer operation, future versions should mask values associated with sensitive names such as `API_KEY`, `SECRET`, `PASSWORD`, and `TOKEN`.

Environment Finder is intended for inspection of systems you own or are authorized to administer.

## Planned Improvements

- [ ] Automatic masking of sensitive environment variables.
- [ ] Export system information to JSON.
- [ ] Export reports to TXT.
- [ ] Cross-platform compatibility testing.
- [ ] Additional development tool detection.
- [ ] Command-line arguments for selective scanning.
- [ ] Improved error handling and logging.
- [ ] Optional verbose output.

## Use Cases

Environment Finder can be useful for:

- IT system diagnostics.
- Python development troubleshooting.
- Development environment auditing.
- Security configuration reviews.
- Checking tool availability.
- Troubleshooting environment variables.

## Author

**SwiftGlitxh**

GitHub: https://github.com/swiftglitxh

Developed for educational purposes, system administration, and cybersecurity tooling.

## Disclaimer

This software is provided as-is, without warranty. Users are responsible for protecting sensitive system information collected or displayed by the tool.

---

**Environment Finder v0.1 | Developed by SwiftGlitxh**
