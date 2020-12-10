from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration 
from .models import User

# Create your views here.

# This function add new student and show all students
def add_show(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm= fm.cleaned_data['name']
            em= fm.cleaned_data['email']
            pw= fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration() 

    else:
        fm = StudentRegistration() 
    stud = User.objects.all()   
    return render(request, 'crud_app/addandshow.html', {'form': fm, 'stu':stud})

# This Function will Update/Edit

def update_data(request, id):
    if request.method == 'POST':
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance= pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance= pi)
    return render(request, 'crud_app/updatestudent.html', {'form':fm})

# This function Will Delete Items 

def delete_data(request, id):
    if request.method =='POST':
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


       