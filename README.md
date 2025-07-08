# 🏦 Shomiti Management System

A web-based system to manage cooperative society (Shomiti) operations including member management, installment tracking, payment workflows, and financial reporting.

---

### 🔧 Installation

```bash
git clone https://github.com/obaidullah-faruk/Shomiti-management-system.git
cd Shomiti-management-system
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt


python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver