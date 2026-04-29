Contact Management Application

A simple web app built using Django to manage contacts.
You can add, view, edit, and delete contacts.

Tools & Technologies Used
- Python
- Django
- SQLite (default Django database)
- HTML, CSS
- VS Code

How I Set It Up

1. Opened the project folder in cmd and activated a virtual environment
       python -m venv myenv
       myenv\Scripts\activate

2. Installed Django
       pip install django

3. Created the project and app
       django-admin startproject contact_management_project.
       python manage.py startapp base

4. Wrote the model, form, views, urls, and templates

5. Ran migrations
       python manage.py makemigrations
       python manage.py migrate

6. Started the server
       python manage.py runserver

Features
- Add a new contact (name, address, email, phone)
- View all contacts in a table
- Edit contact details
- Delete a contact with a confirmation step
- Phone number validation for numbers
- Flash messages after actions


How to Run
1. Download the project
2. Create and activate a virtual environment
3. Run:  pip install -r requirements.txt
4. Run:  python manage.py migrate
5. Run:  python manage.py runserver
6. Open: http://127.0.0.1:8000/
