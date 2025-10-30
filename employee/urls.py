# employee/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('getAll/', views.get_all),
    path('getById/<int:id>/', views.get_by_id),
    path('register/', views.register),
    path('update/<int:id>/', views.update),
    path('delete/<int:id>/', views.delete),
    path('login/', views.login),
]
