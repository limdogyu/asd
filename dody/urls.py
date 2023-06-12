from django.contrib import admin
from django.urls import path, include

from .views import index

app_name = 'dody'

urlpatterns = [
    path('', index, name='index'),  # '/' 에 해당되는 path
]
