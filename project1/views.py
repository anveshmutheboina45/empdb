from django.shortcuts import render

from app.models import Employee


def home(request):
    employee=Employee.objects.all()
    context={
        'employee':employee,
        
    }
    return render(request,'home.html',context)