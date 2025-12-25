# Employee Management System (Django)

A professional Django CRUD application with authentication, role-based permissions, validation, search, and clean UI.

This project demonstrates real-world Django development practices and is suitable for entry-level Python/Django roles.

---

## Features

- User authentication (login & logout)
- Role-based access control using Django permissions
- Create, update, delete employees
- Salary validation (role-based rules)
- Search employees by name or role
- Clean UI (custom login page)
- Admin panel integration
- Secure forms with CSRF protection

---

## Tech Stack

- Python 3
- Django
- SQLite (development database)
- HTML / CSS
- Django Authentication System

---

## Project Structure

employee-management-system/
│
├── config/ # Project settings
├── employees/ # Main application
│ ├── models.py
│ ├── views.py
│ ├── forms.py
│ ├── urls.py
│ └── templates/
│
├── templates/
│ └── registration/
│ └── login.html
│
├── db.sqlite3
├── manage.py
└── README.md



---

## Installation & Setup

```bash
git clone https://github.com/your-username/employee-management-system.git
cd employee-management-system

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
Usage
Visit /login/ to log in

Admin panel: /admin/

Employee dashboard: /employees/

Permissions control who can add, edit, or delete employees

Validation Rules
Salary must be positive

Intern salary cannot exceed ₹15,000

Validation enforced at form and model level

What This Project Proves
Understanding of Django MVC (MTV) architecture

Secure form handling

Authentication & authorization

Real database interaction

Clean project organization

Deployment readiness

Next Improvements (Planned)
Pagination

Export to CSV

REST API (DRF)

Deployment on Render / Railway

Author
Built by Phuvanenthran P
Aspiring Python & Django Developer


⚠️ Replace the GitHub URL and name if needed — nothing else.

---

## PART 3 — FINAL PUSH

```bash
git push origin main
(or master, depending on your branch)

