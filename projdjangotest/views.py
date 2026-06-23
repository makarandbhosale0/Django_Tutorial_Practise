from django.http import HttpResponse
from django.shortcuts import render
from Employee.models import Employee

def home(request):
    employe = Employee.objects.all()
    print(employe)
    context = {
        'employe': employe,
    }
    return render(request, 'home.html', context)