from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('home/', views.home, name='employee_home'),
    path('view_emp/', views.employee_view, name='employee_view'),
    path('add_emp/', views.employee_create, name='employee_create'),
    path('edit_emp/<int:id>/', views.employee_edit, name='employee-edit-id'),
    path('edit_emp/', views.employee_edit, name='employee-edit'),
]
