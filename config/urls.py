from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from apps.core.views import *
from apps.classes.views import *
from apps.teacher.views import *
from apps.parents.views import *
from apps.students.views import *
from apps.Fees.views import *
from apps.admins.views import *
urlpatterns = [
    path('',home,name="home"),
    path('login/',LoginPage,name="login"),
    path('Logout/',logoutUser,name="Logout"),
    path('admin/', admin.site.urls),
    path('404/',error_page,name="404"),
    path('class/',classes,name="class"),
    path('edit-class/<str:pk>/', edit_class,name="edit_class"),
    path('delete-class/<str:pk>/', delete_class,name="delete_class"),
    path('teachers/',Teachers,name="Teacher"),
    path('view-teacher/<str:pk>/', teacher_detail,name="view_teacher"),
    path('edit-teacher/<str:pk>/', edit_teacher,name="edit_teacher"),
    path('delete-teacher/<str:pk>/', delete_teacher,name="delete_teacher"),
    path('teacher-file/<str:pk>/', teacher_files,name="teacher_file"),
    path('delete-teacher-file/<str:pk>/', delete_teacher_file,name="delete_teacher_file"),
    path('edit-teacher-image/<str:pk>/', edit_teacherphoto,name="edit_teacher_photo"),
    path('parents/',parents,name="parents"),
    path('view-parent/<str:pk>/', parent_detail,name="view_parent"),
    path('edit-parent/<str:pk>/', edit_parent,name="edit_parent"),
    path('delete-parent/<str:pk>/', delete_parent,name="delete_parent"),
    path('Student/',Student,name="Student"),
    path('view-student/<str:pk>/', Student_details,name="view_student"),
    path('Edit-student/<str:pk>/', Edit_Student,name="edit_student"),
    path('Delete-student/<str:pk>/', Delete_Student,name="delete_student"),
    path('Edit-student-photo/<str:pk>/', edit_studentphoto,name="edit_student_photo"),
    path('Student-file/<str:pk>/', student_files,name="student_file"),
    path('delete-student-file/<str:pk>/', delete_student_file,name="delete_student_file"),
    path('Fees/',Fee,name="Fees"),
    path('Edit-Fees/<str:pk>/', edit_fees,name="edit_fees"),
    path('Delete-Fees/<str:pk>/', delete_fees,name="delete_fees"),
    path('Admins/',admins,name="Admins"),
    path('Delete-Admin/<str:pk>/', delete_admins,name="delete_admin"),
    
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

