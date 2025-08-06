from django.urls import path

from . import views

urlpatterns = [
    path('',views.view_students, name='view_students'),
    path('add/',views.add_student, name='add_student'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),

]
