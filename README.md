<div align="center">

# 🐍 Django Tutorial Practise

**A beginner-friendly Django project built while learning core Django fundamentals — models, views, templates, and the MVT architecture.**

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Django](https://img.shields.io/badge/Django-5.x-092E20?logo=django&logoColor=white)](https://www.djangoproject.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](#-license)

</div>

---

## 📖 About

**Django_Tutorial_Practise** is a hands-on learning project for practicing the **Django** web framework end-to-end — from defining models and views to rendering dynamic **HTML templates**. It centers around an **Employee** app that demonstrates a classic Django MVT (Model–View–Template) workflow, making it a handy reference for anyone getting started with Django.

> ℹ️ This README was generated from the repository's folder structure. Update the **Features** section with the exact functionality implemented in the `Employee` app.

---

## ✨ Features

- 🏗️ Classic Django **MVT (Model–View–Template)** architecture
- 👨‍💼 **Employee** app demonstrating models, views, and forms
- 🖥️ Server-rendered pages using Django's **template engine**
- 🗄️ Django ORM for database interactions
- ⚙️ Django Admin panel for managing data
- 🧩 Clean, beginner-friendly project layout — great for learning by example

---

## 🛠️ Tech Stack

| Category         | Technology         |
|--------------------|-----------------------|
| Language            | Python                |
| Web Framework       | Django                |
| Templating          | Django Template Engine (HTML) |
| Database            | SQLite (default, configurable) |

---

## 📂 Project Structure

```
Django_Tutorial_Practise/
├── Employee/           # Django app: models, views, urls for Employee data
├── projdjangotest/     # Main Django project (settings, urls, wsgi/asgi)
├── templates/           # Shared HTML templates
├── manage.py            # Django's command-line utility
└── .gitignore
```

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.8+](https://www.python.org/downloads/)
- `pip` (Python package manager)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/makarandbhosale0/Django_Tutorial_Practise.git

# 2. Move into the project directory
cd Django_Tutorial_Practise

# 3. (Recommended) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate    # On Windows: venv\Scripts\activate

# 4. Install Django
pip install django
```

> 💡 If a `requirements.txt` is added to the repo later, replace step 4 with `pip install -r requirements.txt`.

### Set Up the Database

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create a Superuser (optional, for Django Admin access)

```bash
python manage.py createsuperuser
```

### Run the Development Server

```bash
python manage.py runserver
```

Visit **http://127.0.0.1:8000/** to view the app, and **http://127.0.0.1:8000/admin/** for the Django admin panel.

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the project
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📄 License

This project is available under the **MIT License**. Feel free to use, modify, and distribute it.

---

## 👤 Author

**Makarand Bhosale**
GitHub: [@makarandbhosale0](https://github.com/makarandbhosale0)

<div align="center">

⭐ If you found this project useful, consider giving it a star!

</div>
