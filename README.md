# Python Automation & Data Handling Projects

This repository contains Python-based projects focused on **automation**, **structured data handling**, and **JSON-based persistence**, demonstrating practical data workflows and validation logic.

---

## 📁 Automated Folder Cleaner (Python, JSON)

### Overview
A Python script that automatically organizes files in a target directory into categorized folders based on file extensions.  
The classification rules are defined using a **JSON configuration file**, making the workflow flexible and easy to modify.


### Key Features
- Automatically categorizes files (Images, Documents, Audio, Video, etc.)
- Uses **JSON-based configuration** for file classification rules
- Performs directory traversal and file movement
- Includes error handling for invalid paths and file operations
- Ensures consistency in file organization


### Project Structure
FolderSorter.py
categories.json

### How to Run
python FolderSorter.py

You will be prompted to enter a folder path.
Press Enter to use the default ~/Downloads directory.

### Concepts Used
- Python scripting
- File handling and directory traversal
- JSON parsing and structured configuration
- Workflow automation
- Error handling

---

## 📇 Contact Book Application (Python, JSON)

### Overview
A command-line contact book application built using Python that stores contact information persistently using a **JSON file**. 
The application supports basic CRUD operations while ensuring data consistency and integrity.

---

### Key Features
- Add, view, update, search, and delete contacts
- Uses **JSON-based persistent storage** for contact data
- Reads from and writes to JSON files dynamically
- Handles missing or malformed JSON files safely
- Includes input validation and logical consistency checks


### Project Structure
Contactsproj.ipynb
contacts.json

### How to run
python ContactsProj.py
