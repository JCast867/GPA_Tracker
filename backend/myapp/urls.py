from django.urls import path
from . import views

urlpatterns = [
    path('add-course/', views.add_course, name='add_course'),
    path('view-gpa/', views.view_gpa, name='view_gpa'),
    path('api/courses/', views.api_courses, name='api_courses'),
]