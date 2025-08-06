
from django.shortcuts import render, redirect
from student_app.forms import AddStudentForm, LoginForm, SignUpForm
from student_app.models import Student, SignUp


# Create your views here.

def add_student(request):
    if request.method == 'POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            student = form.save(commit=True)
            total = student.maths + student.science + student.english
            student.percentage = round(total/3,2)
            student.save()
            return redirect('view_students')
    else:
        form = AddStudentForm()
    return render(request,'student_app/add_student.html', {'form':form} )

def view_students(request):
    error = None
    form = AddStudentForm()
    students = Student.objects.all()
    return render(request,'student_app/view_student.html',{
        'form':form,
        'students': students,
        'error' : error
    })

def login(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_id = form.cleaned_data['user_id']
            password = form.cleaned_data['password']
            try:

                user = SignUp.objects.get(user_id = user_id , password = password )
                return redirect('view_students')
            except SignUp.DoesNotExist:
                error = ' Wrong UserId and Password '
        else:
            error = 'Enter wrong Id or password '
    else:
        form = LoginForm()

    return render(request,'student_app/login.html',{
        'form':form,
        'error': error
    })

def signup(request):
    error = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request,'student_app/signup.html',{
        'forms':form,
        'error':error
    })