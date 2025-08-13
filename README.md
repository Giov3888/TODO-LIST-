# Task Manager – Python with Excel Storage

A command-line tool to **create, manage, and track tasks** with automatic saving in an Excel (`.xlsx`) file.  
This project is designed not only for practical task management but also as a **learning resource** for anyone who wants to get hands-on experience with:
- **Object-Oriented Programming (OOP) in Python**
- **Data manipulation using pandas**
- **Reading and writing Excel files in Python**

---

## Main Features
- **Add tasks** with custom name and due date/time
- **Edit task deadlines** with automatic status update
- **Mark tasks as completed**
- **Delete tasks** by ID or by name
- **Display tasks** with details: ID, name, status, creation date, due date
- **Persistent storage** in an Excel file (`taches.xlsx`)

---

## Target Audience
- Beginners learning **Python classes, methods, and objects**
- Anyone interested in **reading/writing Excel files in Python**
- Students looking for a **simple, real-world project** to practice `pandas` and `datetime`

---

## Technologies Used
- **Python 3.x**
- `pandas` for table-based data management
- `openpyxl` (via pandas) for Excel file handling
- `datetime` for date and time management
- `os` & `re` for file handling and flexible search

---

## How to Use

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Giov3888/TODO-LIST-.git
cd TODO-LIST-
```
### 2️⃣ Install dependencies
```bash
pip install pandas openpyxl
```

### 3️⃣ Run the program
```bash
python main.py
```
### 4️⃣ Use the menu to:
  Add new tasks
  Edit deadlines
  Mark tasks as completed
  Delete tasks
  View all tasks

## Learning Goals
This project can be used as a practical exercise for:
Understanding how to design a Python program with classes and methods
Learning how to store and retrieve data from Excel files in Python
Managing dates, times, and status updates dynamically


