from django.shortcuts import render
from employee.models import Employee


def employee_list(request):
    employees = Employee.objects.all()
    
    return render(request, "employee_list.html", {
        "employees": employees
    })


def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    return render(request, "employee_detail.html", {
        "employee": employee
    })