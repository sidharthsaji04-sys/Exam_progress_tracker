# Exam Progress Tracker

A simple Python project that tracks exam marks, analyzes mistakes, and gives a study suggestion for each subject.

The program uses:

- `pandas` to read the CSV file and analyze marks
- `tkinter` to show a simple GUI
- `matplotlib` to display a bar chart of marks

## Features

- Shows marks and suggestions in a table
- Calculates points based on marks and mistake types
- Displays a bar chart for subject marks
- Uses a CSV file to store progress data

## Mistake Codes

| Code | Meaning |
| --- | --- |
| c | Concept mistake |
| a | Attention mistake |
| n | Not revised |
| p | Practice needed |
| x | No mistake |

## Files

```text
Exam progress tracker/
├── exam progress(pandas).py
├── progress.csv
└── README.md
```

## How To Run

Install the required libraries:

```bash
pip install pandas matplotlib
```

Run the program:

```bash
python "exam progress(pandas).py"
```

## CSV Format

The `progress.csv` file should look like this:

```csv
subject,mark,mistakes
english,24,x
chemistry,22,"c,n,a"
maths,17,"c,p"
biology,22,"a,n"
physics,18,"c,a,n"
```

## Future Improvements

- Add a button to update marks from the GUI
- Add a button to update mistake codes
- Save the analysis report to a CSV file
- Add better styling to the interface
