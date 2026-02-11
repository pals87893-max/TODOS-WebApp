**📝 Flask To-Do App**

A simple To-Do List web application built using Flask, SQLAlchemy, and SQLite.
This app allows users to create, view, update, and delete tasks.

**🚀 Features**

*Add new tasks

*View all tasks

*Update existing tasks

*Delete tasks

*SQLite database integration

*MVC structure using Flask and Jinja2 templates

**🛠️ Tech Stack**

*Backend: Flask (Python)

*Database: SQLite

*ORM: Flask-SQLAlchemy

*Frontend: HTML (Jinja2 Templates)

**📂 Project Structure**
project-folder/
│
├── app.py
├── todo.db (created automatically)
├── templates/
│   ├── home.html
│   ├── index.html
│   ├── add.html
│   └── update.html
└── README.md

**⚙️ Installation & Setup**
1️⃣ Clone the Repository
git clone | https://github.com/pals87893-max/TODOS-WebApp.git
cd flask-todo-app

2️⃣ Create Virtual Environment (Recommended)
python -m venv venv


Activate the environment:

Windows

venv\Scripts\activate


Mac/Linux

source venv/bin/activate

3️⃣ Install Dependencies
pip install flask flask_sqlalchemy


Or create a requirements.txt file:

Flask
Flask-SQLAlchemy


Then install:

pip install -r requirements.txt

▶️ Running the Application
python app.py


**🗄️ Database Model**
Todo Model
Field	Type	Description
sl_no	Integer	Primary Key (Auto Increment)
created_at	DateTime	Auto-generated timestamp
title	String(200)	Optional title
todo	String(600)	Task description (Required)
**🌐 Routes**
Route	Method	Description
/	GET	Home page
/index	GET, POST	View all tasks & add task
/add	GET, POST	Add new task
/update/<sl_no>	GET, POST	Update task
/delete/<sl_no>	GET	Delete task
📌 How It Works

User submits a form.

Flask captures form data using request.form.

Data is stored in SQLite database using SQLAlchemy ORM.

Tasks are retrieved using Todo.query.all().

Jinja2 templates render data dynamically.

**🧠 Learning Objectives**
This project demonstrates:

Flask routing

CRUD operations

SQLAlchemy ORM usage

HTML templating with Jinja2

Redirect handling

Form handling in Flask

**🔒 Future Improvements**

Add user authentication

Add task completion status

Add search functionality

Improve UI with Bootstrap

Add REST API support

Pagination support

**📄 License**

This project is open-source and free to use for educational purposes.
