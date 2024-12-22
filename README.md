# Yearly Journal Generator

## Overview
This script creates a structured directory for a specified year with monthly and weekly markdown files, including objectives files for the year and each month.

## How to Run

```bash
python3 generate-year-journal.py
```

## Input
- **Path**: Specify the root path for the year's directory.
- **Year**: Enter the year to generate the journal.

## Structure
- **Year Folder**: Named after the specified year (e.g., `2024/`).
- **Monthly Folders**: Contains weekly markdown files and a monthly objectives file.
- **Weekly Files**: Named with the week number and date range, including daily headers.
- **Objectives Files**: Yearly and monthly objectives files to outline goals.

## Example Output
```
2024/
    january/
        january-objectives.md
        week1-jan01-jan07-2024.md
        ...
    february/
        february-objectives.md
        ...
    2024-objectives.md
```

## Notes
- Ensure permissions for directory creation are set correctly.
- The script checks if the year folder already exists and will not overwrite existing data.
