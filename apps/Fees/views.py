from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="login")
def Fee(request):
    FeesDB=Fees.objects.all()
    form=Fees_form()
    if request.method=="POST":
        form=Fees_form(request.POST)
        if form.is_valid():
            db=form.save()
            messages.success(request,"New Fees successfully added ")
            return redirect('Fees')
    context={
        'Fees':FeesDB,
        'form':form,
    }
    return render(request,"fees.html",context)

@login_required(login_url="login")
def edit_fees(request,pk):
    FeesDB=Fees.objects.filter(id=pk)
    if len(FeesDB)!=0 and request.method=="POST":
        form=Fees_form(request.POST,instance=Fees.objects.get(id=pk))
        if form.is_valid():
            form.save()
            messages.success(request,"Record successfully updated. ")
            return redirect('Fees')

    elif len(FeesDB)==0:
        return redirect('404')
        
    form=Fees_form(instance=Fees.objects.get(id=pk))
    context={
        'form':form,
    }
    return render(request,"editfees.html",context)

@login_required(login_url="login")
def delete_fees(request,pk):
    FeesDB=Fees.objects.filter(id=pk)
    if len(FeesDB)!=0:
        messages.success(request,"you deleted successfully this Fees "+str(FeesDB[0]))
        FeesDB.delete()
        return redirect('Fees')
    elif len(FeesDB)==0:
       return redirect('404')
    return redirect('Fees')