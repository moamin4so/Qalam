from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from .forms import *
# Create your views here.
@login_required(login_url="login")
def admins(request):
    admindb=AdminsDB.objects.all()
    form=AdminForm()
    if request.method=="POST":
        form=AdminForm(request.POST)
        if form.is_valid(): 
            user = User.objects.create_user(
                username =form.cleaned_data.get('username'),
                password = form.cleaned_data.get('password'), 
                first_name = form.cleaned_data.get('full_name')
            )
            user.save()
            db=form.save(commit=False)
            db.user=user
            db.save()
            messages.success(request,"New Admin successfully added "+form.cleaned_data.get('full_name'))
            return redirect('Admins')
        
    context={
        'users':admindb,
        'form':form
    }
    return render(request,"admin.html",context)

@login_required(login_url="login")
def delete_admins(request,pk):
    admindb=AdminsDB.objects.filter(id=pk)
    if len(admindb)!=0:
        user = User.objects.filter(id=admindb[0].user.id)
        user.delete()
        messages.success(request,"you deleted successfully")
        return redirect('Admins')
    elif len(admindb)==0:
        return redirect('404')
    return redirect('Admins')