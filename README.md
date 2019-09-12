# Challenge
I have selected Django backend with React on the frontend for the solution because
this combination provides best user experience.

# Quick setup
```bash
git clone https://github.com/przemal/ad_dashboard.git
cd ad_dashboard
python3 -m venv venv
pip install --upgrade pip setuptools
pip install pipenv
pipenv install  # install backend dependencies
python manage.py migrate  # setup database
python manage.py import '<https://..csv>'  # import data
cd frontend
npm install  # install frontend dependencies
npm run-script build
python manage.py runserver
```
