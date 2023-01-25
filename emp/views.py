from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Employee
# Create your views here.
def emp_home(request):
    empp=Employee.objects.all()
    print(empp)
    return render(request,'emp/emp_show.html',{'empp':empp})

def add_emp(request):
    if request.method =='POST':
        # print('finallly data is commmmmmmmmmmmmmmmmmmmmmming')
        e=Employee()
        e.name=request.POST.get('name')
        e.emp_id=request.POST.get('emp_id')
        e.phone=request.POST.get('phone')
        e.e_addr=request.POST.get('e_addr')
        if request.POST.get('wfh')==None :
          e.wfh=False
        else :
          e.wfh=True
        e.dept=request.POST.get('dept')
        e.save()
        print(e.name)

        return redirect('/emp')

    return render(request,'emp/add_emp.html',{})

def delete_emp(request,emp_id):
    print(emp_id)
    e=Employee.objects.get(pk=emp_id)
    e.delete()
    return redirect('/emp/')

def update_emp(request,emp_id):
    e=Employee.objects.get(pk=emp_id)
    print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
    print(emp_id)
    return render(request,'emp/update_emp.html',{'e':e})

def update_emp2(request,emp_id):
    if request.method =='POST':
        print('finallly data is commmmmmmmmmmmmmmmmmmmmmming2')
       
        e=Employee.objects.get(pk=emp_id)
        e.name=request.POST.get('name')
        e.emp_id=request.POST.get('emp_id')
        e.phone=request.POST.get('phone')
        e.e_addr=request.POST.get('e_addr')
        if request.POST.get('wfh')==None :
          e.wfh=False
        else :
          e.wfh=True
        e.dept=request.POST.get('dept')
        e.save()
        print(e.name)
        return redirect('/emp')
 
    return render(request,'emp/update_emp.html',{}) 



