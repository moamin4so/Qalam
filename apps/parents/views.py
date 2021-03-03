from django.shortcuts import render
from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from apps.students.models import *
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="login")
def parents(request):
    parentdb=Parent.objects.all()
    form=ParentForm()
    if request.method=="POST":
        form=ParentForm(request.POST)
        if form.is_valid():
            db=form.save()
            messages.success(request,"New Parent successfully added "+form.cleaned_data.get('full_name'))
            return redirect('parents')
    context={
        'parents':parentdb,
        'form':form,
    }
    return render(request,"parent.html",context)
@login_required(login_url="login")
def parent_detail(request,pk):
    parentdb=Parent.objects.filter(id=pk)
    if len(parentdb)==0:
        return redirect('404')
    allstudents=Students.objects.filter(student_parent_id=pk)
    context={
        'parent':parentdb,
        'students':allstudents,
    }
    return render(request,"parent_detail.html",context)

@login_required(login_url="login")
def edit_parent(request,pk):
    parentdb=Parent.objects.filter(id=pk)
    if len(parentdb)!=0 and request.method=="POST":
        form=ParentForm(request.POST,instance=Parent.objects.get(id=pk))
        if form.is_valid():
            form.save()
            messages.success(request,"Record successfully updated. "+form.cleaned_data.get('full_name'))
            return redirect('parents')
    elif len(parentdb)==0:
        return redirect('404')
        
    form=ParentForm(instance=Parent.objects.get(id=pk))
    context={
        'form':form,
    }
    return render(request,"editparent.html",context)

@login_required(login_url="login")
def delete_parent(request,pk):
    parentdb=Parent.objects.filter(id=pk)
    if len(parentdb)!=0:
        messages.success(request,"you deleted successfully this Parent "+str(parentdb[0]))
        parentdb.delete()
        return redirect('parents')
    elif len(parentdb)==0:
       return redirect('404')
    return redirect('parents')