
# JPG File Organizer - Python

## About the Project
The JPG File Organizer is a simple Python automation project developed as part of the CodeAlpha Python Programming Internship.

It helps users move JPG image files from one folder to another automatically.

## Features
- Select the source folder.
- Select the destination folder.
- Automatically move JPG images.
- Skip files if a file with the same name already exists in the destination.
- Display the number of files moved and skipped.
- Simple graphical user interface.

## Technologies Used
- Python 3
- Tkinter
- OS module
- Shutil module

## Requirements
- Python 3 installed on your computer.
- VS Code or another Python editor.

## How to Run
1. Download or clone this repository.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run the following command:

   ```bash
   python file_organizer.py
   ```

5. Select the source and destination folders.
6. Click the organize button to move JPG files.

## How It Works
1. The user selects a source folder.
2. The user selects a destination folder.
3. The program searches for JPG files in the source folder.
4. It moves eligible files to the destination folder.
5. It skips files with duplicate names and displays a summary.

## Concepts Used
- Functions
- File handling
- OS module
- Shutil module
- Conditional statements
- Loops
- Tkinter GUI

## Internship Details
- Organization: CodeAlpha
- Domain: Python Programming
- Project: Task 3 - File Automation

## Safety Note
Test the program using sample JPG images in a temporary folder first. The program moves files from the source folder.

## License
Created for educational and internship purposes.
