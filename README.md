Duplicate Email Checker (Python + Pandas)

Overview

This project is a simple command-line application built using Python and Pandas. It allows users to enter their name and email, and checks whether the email already exists in the system. If a duplicate email is found, the program identifies the existing user associated with that email.

This project demonstrates basic data handling, validation logic, and user interaction using Python.

---

Features

- Accepts user input (name and email)
- Detects duplicate email entries
- Displays the name of the existing user if email is already used
- Adds new users if the email is unique
- Simple and interactive command-line interface

---

Technologies Used

- Python
- Pandas

---

How It Works

1. A dataset is created using a Pandas DataFrame.
2. The user is prompted to enter their name and email.
3. The program checks whether the email already exists in the dataset.
4. If the email exists:
   - A message is displayed indicating which user already owns the email.
5. If the email does not exist:
   - The new user is added to the dataset.

---

Installation and Setup

Prerequisites

- Python installed (version 3.x)
- Pandas library installed

Install Pandas

pip install pandas

---

How to Run

1. Save the file as:

duplicate_check.py

2. Run the program:

python duplicate_check.py

3. Follow the prompts in the terminal to enter user details.

---

Example Output

Duplicate email case:

Enter your name: Arun
Enter your email: a@b.com
This email is already used by Ramya

New email case:

Enter your name: Priya
Enter your email: x@y.com
User added successfully!

---
Future Improvements
- Store data permanently using CSV or database
- Add password functionality and user authentication
- Build a graphical user interface (GUI)
- Convert into a web-based application

---
Author
Rhamya Sri A K
---
License
This project is for educational purposes.
