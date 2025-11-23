# File Management App

## Overview

This is a simple command-line file management application written in Python. It allows users to create, view, read, edit, and delete files interactively through a menu-driven terminal interface, helping manage files quickly without needing a graphical file browser.

## Features

- Create new files (with checks to avoid overwriting existing files)  
- View all files in the current working directory  
- Delete existing files with error handling if file not found  
- Read and display contents of any file  
- Append additional content to files via user input  
- Easy-to-use menu interface with clear instructions  

## Technologies/Tools Used

- Python 3 (standard libraries)  
- `os` module for file system operations like listing and deletion  
- Built-in file handling functions (`open`, `read`, `write`, `append`)  

## Steps to Install & Run the Project

1. Ensure Python 3 is installed on your computer.  
2. Download or clone the project code and save it to a local directory.  
3. Open a terminal or command prompt and navigate (`cd`) to the project folder.  
4. Run the app using the command:python file_manager.py
(or `python3 file_manager.py` depending on your Python setup)  
5. Follow the menu prompts to use the file management features.

## Instructions for Testing

To test the application interactively:  
- Choose option 1 to create a new file; (try creating the same file twice to test error handling).  
- Use option 2 to view the list of files including the one created.  
- Edit a file (option 5) by appending some data and then read it (option 4) to verify the content.  
- Delete a file (option 3) and confirm it no longer appears in the file list.  
- Attempt to delete or read a non-existent file to see error messages.  
- Exit the app cleanly via option 6.

This simple manual testing covers all core functionalities of the app and ensures proper handling of common edge cases.

