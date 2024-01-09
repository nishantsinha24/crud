from django.shortcuts import render, HttpResponseRedirect
from .forms import StudentRegistration
from .models import User

# Create your views here.


def add_data(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = User(name=nm, email=em, password=pw)
            reg.save()
            fm = StudentRegistration()

    else:
        fm = StudentRegistration()
    stud = User.objects.all()
    return render(request, 'enroll/addandshow.html', {'form': fm, 'stu': stud})


# Edit/Update Function

def update_data(request , id):
    if request.method == 'POST':
        obj = User.objects.get(pk = id)
        fm = StudentRegistration(request.POST , instance=obj)
        if fm.is_valid():
            fm.save()
    else:   
        obj = User.objects.get(pk = id)
        fm = StudentRegistration(instance=obj)
    return render(request, 'enroll/updatestudent.html' , {'form' : fm})            
    


# delete function

def delete_data(request, id):
    if request.method == 'POST':
        obj = User.objects.get(pk=id)
        obj.delete()
        return HttpResponseRedirect('/')
