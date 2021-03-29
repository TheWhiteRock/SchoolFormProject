from django.shortcuts import render, redirect
from .forms import TeacherForm, StudentForm, PrincipalForm
from .models import Principal, Teacher, Student
# Create your views here.

def form(request):
    form = PrincipalForm()
    return render(request, "form_register/form.html",{'form':form})



def formp(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PrincipalForm()
        else:
            principal = Principal.objects.get(pk=id)
            form = PrincipalForm(instance = principal)
        return render(request, "form_register/formp.html",{'form':form})
    else:
        if id == 0:
            form = PrincipalForm(request.POST)
        else:
            principal = Principal.objects.get(pk=id)
            form = PrincipalForm(request.POST, instance = principal)
        if form.is_valid():
            form.save()
        return redirect('principal_list/')
    
def formt(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = TeacherForm()
        else:
            teacher = Teacher.objects.get(pk=id)
            form = TeacherForm(instance = teacher)
        return render(request, "form_register/formt.html",{'form':form})
    else:
        if id == 0:
            form = TeacherForm(request.POST)
        else:
            teacher = Teacher.objects.get(pk=id)
            form = TeacherForm(request.POST, instance = teacher)
        if form.is_valid():
            form.save()
        return redirect('teacher_list/')

def forms(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(instance = student)
        return render(request, "form_register/forms.html",{'form':form})
    else:
        if id == 0:
            form = StudentForm(request.POST)
        else:
            student = Student.objects.get(pk=id)
            form = StudentForm(request.POST, instance = student)
        if form.is_valid():
            form.save()
        return redirect('student_list/')
    



def principal_list(request):
    context = {'principal_list': Principal.objects.all(), 
               'teacher_list': Teacher.objects.all(),
               'student_list': Student.objects.all()}
    return render(request, "form_register/principal_list.html", context)
def teacher_list(request):
    context = {'teacher_list': Teacher.objects.all(),
               'student_list': Student.objects.all()}
    return render(request, "form_register/teacher_list.html", context)

def student_list(request):
    context = {'student_list': Student.objects.all()}
    return render(request, "form_register/student_list.html", context)

    

def student_delete(request, id):
    student = Student.objects.get(pk=id)
    student.delete()
    return redirect('../student_list/')

def principal_delete(request, id):
    principal = Principal.objects.get(pk=id)
    principal.delete()
    return redirect('../principal_list/')

def teacher_delete(request, id):
    teacher = Teacher.objects.get(pk=id)
    teacher.delete()
    return redirect('../teacher_list/')