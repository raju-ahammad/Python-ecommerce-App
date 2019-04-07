from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('search/', views.SearchListView.as_view(), name='query'),
]
