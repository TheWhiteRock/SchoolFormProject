from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.form, name='defaultForm'),

    path('formp/<int:id>', views.formp, name='principal_update'),
    path('formp/', views.formp, name='principalForm'),
    path('formp/principal_list/', views.principal_list, name='principal_list'),
    path('formp/delete/<int:id>', views.principal_delete, name='principal_delete'),

    path('formt/<int:id>', views.formt, name='teacher_update'),
    path('formt/', views.formt, name='teacherForm'),
    path('formt/teacher_list/', views.teacher_list, name='teacher_list'),
    path('formt/delete/<int:id>', views.teacher_delete, name='teacher_delete'),

    path('forms/<int:id>', views.forms, name='student_update'),
    path('forms/', views.forms, name='studentForm'),
    path('forms/student_list/', views.student_list, name='student_list'),
    path('forms/delete/<int:id>', views.student_delete, name='student_delete'),
]
