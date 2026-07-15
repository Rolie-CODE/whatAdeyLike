# Python to TypeScript Practice

## 📖 Overview

This repository is a beginner-friendly team project focused on learning **Python** and **TypeScript** side by side.

The project is first implemented in **Python**, then rewritten in **TypeScript** while maintaining the same logic and workflow. This helps reinforce programming concepts while introducing the syntax and features of both languages.

---

## 🎯 Objectives

* Learn the fundamentals of Python.
* Translate Python programs into TypeScript.
* Understand the similarities and differences between the two languages.
* Practice working with modules and file organization.
* Learn how data flows between multiple files in a project.

---

## 👥 Team Workflow

The project is divided into three stages:

```text
Input
   ↓
Processing
   ↓
Report
```

Each stage is handled in a separate file.

---

## 📁 Project Structure

```text
project/
│
├── input.py
├── process.py
├── report.py
├── student_data.json
│
├── ts/
│   ├── input.ts
│   ├── process.ts
│   ├── report.ts
│   └── student_data.json
│
└── README.md
```

---

## 🐍 Python Version

### `input.py`

Responsible for collecting the student's information.

* Student name
* Five subject scores

Outputs the student data for processing.

---

### `process.py`

Processes the student data by calculating:

* Total score
* Average score
* Grade
* Pass/Fail status

The processed information is stored in **`student_data.json`**.

---

### `report.py`

Reads the information from **`student_data.json`** and prints a formatted student report.

---

## 🟦 TypeScript Version

The **`ts/`** folder contains the TypeScript implementation of the same project.

### `input.ts`

Collects the student's information.

### `process.ts`

Processes the student's scores and saves the results to **`ts/student_data.json`**.

### `report.ts`

Reads **`ts/student_data.json`** and displays the final student report.

---

## 🔄 Project Flow

### Python

```text
input.py
    ↓
process.py
    ↓
student_data.json
    ↓
report.py
```

### TypeScript

```text
ts/input.ts
      ↓
ts/process.ts
      ↓
ts/student_data.json
      ↓
ts/report.ts
```

---

## 📚 Concepts Covered

This project introduces:

* Variables
* Data Types
* User Input
* Lists / Arrays
* Dictionaries / Objects
* Functions
* Conditional Statements
* Loops
* Modules
* Importing Files
* Reading and Writing JSON
* Basic Project Structure

---

## 🚀 Goal

After completing this project, every team member should be able to:

* Build the same program in both Python and TypeScript.
* Organize code across multiple files.
* Pass data between modules.
* Read from and write to JSON files.
* Understand how the same programming concepts are expressed in different languages.

---

Happy Coding! 🚀
