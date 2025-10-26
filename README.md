# Railway Reservation System (Python + MySQL)

A simple **command-line based Railway Reservation System** built using Python and MySQL.  
This project demonstrates the fundamentals of database connectivity, user interaction, and record management in Python.

## 📌 Table of contents
- <a href="#features">🚉 Features</a>
- <a href="#languages-or-frameworks-used"></> Languages or Frameworks Used</a>
- <a href="#requirements">⚙️ Requirements</a>
- <a href="#setup-instructions">🧩 Setup Instructions</a>
- <a href="#disclaimer">⚠️ Disclaimer</a>
- <a href="author">🤖 Author</a>

<h2><a class="anchor" id="features"></a>🚉 Features</h2>

- Automatic admin account setup on first run
- Secure admin login 
- Add, view, and delete train details in admin mode 
- Reserve and cancel passenger tickets  
- View passenger list with booking details  
- Auto seat update after booking or cancellation  

<h2><a class="anchor" id="languages-or-frameworks-used"></a>&lt/> Languages or Frameworks Used</h2>

- **Python**
- **MySQL**
- **mysql-connector-python** - library (for database connectivity)
- **pwinput** - library (for secure password input)
- **time** - library (for delay and loading simulation)

<h2><a class="anchor" id="requirements"></a>⚙️ Requirements</h2>

Before running the program, ensure that the following are installed on your computer:
- **MySQL Server**  
- **Python libraries:**  
  Install the required Python packages by running the following commands in your terminal or command prompt:  
  ```bash 
  pip install mysql-connector-python
  pip install pwinput
<h2><a class="anchor" id="setup-instructions"></a>🧩 Setup Instructions</h2>

1. Open your Python editor (like IDLE, VS Code, or PyCharm).
2. Copy and paste the code into a new Python file, for example `railway-reservation.py`.
3. In the script, update the database connection line to match your local MySQL credentials:
    ```bash
    mydb=con.connect(host="localhost",user="yourusername",password="yourpassword")
4. Run the program.

The database and required tables will be created automatically during the first execution.
You will also be prompted to create an admin account if none exists.

<h2><a class="anchor" id="disclaimer"></a>⚠️ Disclaimer</h2>

This project is intended solely for educational purposes. It is not a deployable or production-level system and should not be used for real-world railway management or organizational purposes.

The program runs on a local computer with a manually configured MySQL server and does not support remote or concurrent multi-user access. Its goal is to demonstrate how Python can interact with SQL databases through basic CRUD operations, condition handling, and menu-driven programming.

<h2><a class="anchor" id="author"></a>🤖 Author</h2>

[sreyassasikumar](https://github.com/sreyassasikumar)