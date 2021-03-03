from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="login")
def Teachers(request):
    Teacherdb=Teacher.objects.all()
    form=TeacherForm()
    if request.method=="POST":
        form=TeacherForm(request.POST,request.FILES)
        if form.is_valid():
            db=form.save()
            messages.success(request,"New Teacher successfully added "+form.cleaned_data.get('full_name'))
            return redirect('Teacher')
    context={
        'teachers':Teacherdb,
        'form':form,
    }
    return render(request,"teacher.html",context)

@login_required(login_url="login")
def teacher_detail(request,pk):
    Teacherdb=Teacher.objects.filter(id=pk)
    form=Teacher_file_form()
    image_form=editphotoform()
    if len(Teacherdb)==0:
        return redirect('404')
    context={
        'teacher':Teacherdb,
        'form':form,
        'teacher_files':Teacher_File.objects.filter(teacher=Teacher.objects.get(id=pk)),
        'image_form':image_form,
    }
    return render(request,"teacher_detail.html",context)

@login_required(login_url="login")
def edit_teacher(request,pk):
    Teacherdb=Teacher.objects.filter(id=pk)
    if len(Teacherdb)!=0 and request.method=="POST":
        form=TeacherForm(request.POST,instance=Teacher.objects.get(id=pk))
        if form.is_valid():
            form.save()
            messages.success(request,"Record successfully updated. "+form.cleaned_data.get('full_name'))
            return redirect('Teacher')
    elif len(Teacherdb)==0:
        return redirect('404')
        
    form=TeacherForm(instance=Teacher.objects.get(id=pk))
    context={
        'form':form,
    }
    return render(request,"editteacher.html",context)
    
@login_required(login_url="login")
def delete_teacher(request,pk):
    Teacherdb=Teacher.objects.filter(id=pk)
    if len(Teacherdb)!=0:
        messages.success(request,"you deleted successfully this Teacher "+str(Teacherdb[0]))
        Teacherdb[0].image.delete()
        Teacherdb.delete()
        return redirect('Teacher')
    elif len(Teacherdb)==0:
       return redirect('404')
    return redirect('Teacher')

@login_required(login_url="login")
def teacher_files(request,pk):
    Teacherdb=Teacher.objects.filter(id=pk)
    if len(Teacherdb)!=0 and request.POST:
        form=Teacher_file_form(request.POST, request.FILES)
        if form.is_valid():
            form_save=form.save(commit=False)
            form_save.teacher=Teacher.objects.get(id=pk)
            form_save.save()
            return HttpResponseRedirect(reverse('view_teacher',args=[Teacherdb[0].id]))   
    return redirect('Teacher') 

@login_required(login_url="login")
def delete_teacher_file(request,pk): 
    teacher_file=Teacher_File.objects.filter(id=pk)
    if len(teacher_file)!=0:
        t_id=teacher_file[0].teacher.id
        teacher_file[0].file_input.delete()
        teacher_file.delete()
        return HttpResponseRedirect(reverse('view_teacher',args=[t_id]))  
    return redirect('Teacher')

@login_required(login_url="login")
def edit_teacherphoto(request,pk):
    teachers=Teacher.objects.filter(id=pk)
    form=editphotoform()
    if request.method=="POST" and len(teachers)!=0:
        form=editphotoform(request.POST,request.FILES)
        if form.is_valid():
            teacherphoto=Teacher.objects.get(id=pk)
            teacherphoto.image.delete()
            teacherphoto.image=form.cleaned_data.get('photo')
            teacherphoto.save()
            return HttpResponseRedirect(reverse('view_teacher',args=[teachers[0].id]))   
    return redirect('404page')
        



