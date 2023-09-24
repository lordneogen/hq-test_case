from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('lessons/', List_cr_Lessons.as_view()),
    path('products/<int:id>/lessons', rud_Lessons.as_view()),
    path('products/', List_cr_Lesons.as_view()),
]
