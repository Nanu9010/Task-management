
from django import views
from django.shortcuts import render, redirect, get_object_or_404
from task_manager.forms import LoginForm, SignUpForm, TaskForm
from task_manager.models import Login, SignUp, Task


# Create your views here.

def login_view(request):
    error = None
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = form.cleaned_data['role']

            try:
                user = Login.objects.get(password=password , username=username)

                if role=='Admin' and user.role == 'Admin':
                    return redirect('home')

                if role=='Employee' and user.role== 'Employee':
                    return redirect('employee')
                else:
                    error = 'User not found...'

            except Login.DoesNotExist:
                error = 'Invalid username or Password'
    else:
        form = LoginForm()
    return render(request,'task_manager/login.html', {'form': form , 'error': error })

def signup_view(request):
    if request.method== 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            signup_data = form.save(commit=False)
            login_data = Login(
                username=signup_data.username,
                password=signup_data.password,
                role= 'User')
            login_data.save()
            signup_data.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request,'task_manager/signup.html', {'form': form })

def employee_add(request):
    error = None
    if request.method=='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            signup_data = form.save()
            login_data = Login(
                username=signup_data.username,
                password = signup_data.password,
                role = 'Employee'
            )
            login_data.save()
            return redirect('employee_view')
    else:
        form= SignUpForm()
    return render(request,'task_manager/employee_add.html',
                    {'form':form,
                     'error':error}
    )

def employee_view(request):
    employees = SignUp.objects.all()
    return render(request,'task_manager/employee_view.html',{
        'employees':employees
    })

def task_add(request):
    error=None
    form = TaskForm()
    if request.method=='POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task_view')
        else:
            error = 'data not found '
    else:
        form = TaskForm()
    return render(request,'task_manager/task_add.html',{
        'form': form,
        'error': error
    })

def task_view(request):
    task = Task.objects.all()
    return render(request, 'task_manager/task_view.html',{
        'tasks':task
    })

def task_Assign(request, task_id):
    error = None
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task_view')
        else:
            error = 'Invalid data. Please check the form.'
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_manager/task_Assign.html', {
        'error': error,
        'form': form,
        'task': task
    })


def home_view(request):
    tasks = Task.objects.all()
    return render(request,'task_manager/Home.html' ,{
        'tasks':tasks
    })

def employee_profile(request):
    return render(request, 'task_manager/employee_profile.html')

def employee_home(request):
    return render(request,'task_manager/HomeEmployee.html')


class HomeEmployee:
    pass