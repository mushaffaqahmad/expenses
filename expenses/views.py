from django.shortcuts import render

# https://pypi.org/project/django-heroku/
# pip install gunicorn
# https://gunicorn.org/
# web: gunicorn expenseswebsite.wsgi
# Create your views here.

def index(request):
    return render(request, 'expenses/index.html')

def add_expense():
    return render(request, 'expenses/add_expense.html')
