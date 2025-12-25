# Employee Management System (Django)

A full-stack **Employee Management System** built with Django, implementing authentication, role-based access control, form validation, and a clean user interface.

This project follows real-world Django development practices and is suitable for **entry-level Python / Django developer roles**.

---

## 🚀 Features

* User authentication (login & logout)
* Role-based access control using Django permissions
* Employee CRUD operations (create, update, delete)
* Salary validation with business rules
* Employee search by name or role
* Custom login UI
* Django Admin integration
* Secure form handling with CSRF protection

---

## 🛠 Tech Stack

* **Python 3**
* **Django**
* **SQLite** (development database)
* **HTML / CSS**
* **Django Authentication System**

---

## 📂 Project Structure

```
employee-management-system/
│
├── config/                 # Project settings
├── employees/              # Core application
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   └── templates/
│
├── templates/
│   └── registration/
│       └── login.html
│
├── db.sqlite3
├── manage.py
└── README.md
```

---

## ⚙️ Installation & Setup

```bash
git clone https://github.com/your-username/employee-management-system.git
cd employee-management-system

python -m venv venv
source venv/bin/activate      # Windows: venv\\Scripts\\activate

pip install django
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

---

## ▶️ Usage

* Login: `http://127.0.0.1:8000/login/`
* Admin panel: `http://127.0.0.1:8000/admin/`
* Employee dashboard: `http://127.0.0.1:8000/employees/`

Access to create, update, or delete employees is controlled using Django permissions.

---

## ✅ Validation Rules

* Salary must be a positive value
* Intern salary cannot exceed **₹15,000**
* Validation enforced at both **form** and **model** levels

---

## 🎯 What This Project Demonstrates

* Strong understanding of Django MTV architecture
* Secure authentication and authorization
* Clean separation of concerns using forms and views
* Real database interaction
* Production-ready project structure
* Awareness of deployment best practices

---

## 🔮 Planned Improvements

* Pagination for employee list
* CSV export functionality
* REST API using Django REST Framework (DRF)
* Deployment on Render / Railway

---

## 👤 Author

**Phuvanenthran P**
Aspiring Python & Django Developer

---

## 📌 Final Step

```bash
git push origin main
```

(or `master`, depending on your branch)
