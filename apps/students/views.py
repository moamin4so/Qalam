from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from apps.Fees.models import *
# Create your views here.
@login_required(login_url="login")
def Student(request):
    StudentsDB=Students.objects.all()
    form=StudentForm()
    if request.method=="POST":
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            db=form.save()
            messages.success(request,"New Students successfully added "+form.cleaned_data.get('full_name'))
            return redirect('Student')
    context={
        'students':StudentsDB,
        'form':form,
    }
    return render(request,"student.html",context)

@login_required(login_url="login")
def Student_details(request,pk):
    StudentsDB=Students.objects.filter(id=pk)
    image_form=editphotoform()
    student_file_form=Student_file_form()
    if len(StudentsDB)==0:
        return redirect('404')
    student_files=Student_File.objects.filter(student_id=StudentsDB[0].id)
    student_fees=Fees.objects.filter(student_id=pk)
    context={
        'students':StudentsDB,
        'image_form':image_form,
        'student_files':student_files,
        'student_file_form':student_file_form,
        'student_Fees':student_fees
    }
    return render(request,"student_detail.html",context)
@login_required(login_url="login")
def Edit_Student(request,pk):
    StudentsDB=Students.objects.filter(id=pk)
    if len(StudentsDB)!=0 and request.method=="POST":
        form=StudentForm(request.POST,instance=Students.objects.get(id=pk))
        if form.is_valid():
            form.save()
            messages.success(request,"Record successfully updated. "+form.cleaned_data.get('full_name'))
            return redirect('Student')

    elif len(StudentsDB)==0:
        return redirect('404')
        
    form=StudentForm(instance=Students.objects.get(id=pk))
    context={
        'form':form,
    }
    return render(request,"editstudent.html",context)

@login_required(login_url="login")
def edit_studentphoto(request,pk):
    StudentsDB=Students.objects.filter(id=pk)
    form=editphotoform()
    if request.method=="POST" and len(StudentsDB)!=0:
        form=editphotoform(request.POST,request.FILES)
        if form.is_valid():
            studentphoto=Students.objects.get(id=pk)
            studentphoto.student_photo.delete()
            studentphoto.student_photo=form.cleaned_data.get('photo')
            studentphoto.save()
            return HttpResponseRedirect(reverse('view_student',args=[StudentsDB[0].id]))   
    return redirect('404page')


@login_required(login_url="login")
def Delete_Student(request,pk):
    StudentsDB=Students.objects.filter(id=pk)
    if len(StudentsDB)!=0:
        messages.success(request,"you deleted successfully this Student "+str(StudentsDB[0]))
        StudentsDB[0].student_photo.delete()
        StudentsDB.delete()
        return redirect('Student')
    elif len(StudentsDB)==0:
       return redirect('404')
    return redirect('Student')

@login_required(login_url="login")
def student_files(request,pk):
    StudentsDB=Students.objects.filter(id=pk)
    if len(StudentsDB)!=0 and request.POST:
        form=Student_file_form(request.POST, request.FILES)
        if form.is_valid():
            form_save=form.save(commit=False)
            form_save.student=Students.objects.get(id=pk)
            form_save.save()
            return HttpResponseRedirect(reverse('view_student',args=[StudentsDB[0].id]))   
    return redirect('Student') 
@login_required(login_url="login")
def delete_student_file(request,pk): 
    student_file=Student_File.objects.filter(id=pk)
    if len(student_file)!=0:
        s_id=student_file[0].student.id
        student_file[0].file_input.delete()
        student_file.delete()
        return HttpResponseRedirect(reverse('view_student',args=[s_id]))  
    return redirect('Student')