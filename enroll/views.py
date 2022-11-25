from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User


# Create your views here.

# This Fuction will add New Student and show all the Student
def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg_user = User(name=nm, email=em, password=pw)
            reg_user.save()
    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


# This Fuction will Delete Student
def delete_student(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# This Fuction Will Update/Edit
def update_data(request, id):
    if request.method == "POST":
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi = User.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html', {'form': fm})
