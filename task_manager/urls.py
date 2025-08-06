from django.urls import path

from task_manager import  views

urlpatterns = [
    path('',views.home_view, name='home'),
    path('login/',views.login_view, name='login'),
    path('signup/',views.signup_view, name='signup'),
    path('task_view/',views.task_view, name='task_view'),
    path('add_task/',views.task_add, name='task_add'),
    path('add_employee/',views.employee_add, name='employee_add'),
    path('view_employee/', views.employee_view, name='employee_view'),
    path('employee/', views.HomeEmployee, name='employee'),
    path('profile/',views.employee_profile, name='profile'),
    path('Assign/<int:task_id>/', views.task_Assign, name='task_Assign')





]
