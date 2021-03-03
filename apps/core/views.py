from django.shortcuts import render,redirect
from apps.classes.models import *
from apps.teacher.models import *
from apps.parents.models import *
from apps.students.models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url="login")
def home(request):
    classdb=Classes.objects.all()
    parentdb=Parent.objects.all()
    Teacherdb=Teacher.objects.all()
    StudentsDB=Students.objects.all()
    context={
       'total_classes':classdb.count(),
       'total_parents':parentdb.count(),
       'total_teachers':Teacherdb.count(),
       'total_students':StudentsDB.count()
    }
    return render(request,'index.html',context)
    
@login_required(login_url="login")   
def error_page(request):
    return render(request,'404.html')

def LoginPage(request):
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('Password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.warning(request,"Username or Password Are incorrect")
            return render(request,"login.html")
    return render(request,"login.html")

def logoutUser(request):
    logout(request)
    return redirect('login')



