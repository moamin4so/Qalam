from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url="login")
def classes(request):
    classdb=Classes.objects.all()
    form=Class_Form()
    if request.method=="POST":
        form=Class_Form(request.POST)
        if form.is_valid():
            db=form.save()
            messages.success(request,"New Class successfully added "+form.cleaned_data.get('name'))
            return redirect('class')
    context={
        'classes':classdb,
        'form':form,
    }
    return render(request,"class.html",context)

@login_required(login_url="login")
def edit_class(request,pk):
    classdb=Classes.objects.filter(id=pk)
    if len(classdb)!=0 and request.method=="POST":
        form=Class_Form(request.POST,instance=Classes.objects.get(id=pk))
        if form.is_valid():
            form.save()
            messages.success(request,"Record successfully updated. "+form.cleaned_data.get('name'))
            return redirect('class')
    elif len(classdb)==0:
        return redirect('404')
        
    form=Class_Form(instance=Classes.objects.get(id=pk))
    context={
        'form':form,
    }
    return render(request,"editclass.html",context)
    
@login_required(login_url="login")
def delete_class(request,pk):
    classdb=Classes.objects.filter(id=pk)
    if len(classdb)!=0:
        messages.success(request,"you deleted successfully this Class "+str(classdb[0]))
        classdb.delete()
        return redirect('class')
    elif len(classdb)==0:
       return redirect('404')
    return redirect('class')