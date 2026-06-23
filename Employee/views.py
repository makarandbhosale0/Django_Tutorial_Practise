from django.shortcuts import render, get_object_or_404
from Employee.models import Employee
from django.http import Http404, HttpResponse
# Create your views here.
def employe_details(request, primary_key):
    # try:
    #     emp = Employee.objects.get(pk=primary_key)
    #     print(emp)
    # except:
    #     raise Http404 

    emp = get_object_or_404(Employee, pk=primary_key)

    # return HttpResponse(emp)
    return render(request, 'employee_detail.html')