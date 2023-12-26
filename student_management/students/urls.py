# students/urls.py
from django.urls import path
from .views import home, student_list, student_detail, add_grade, add_student, delete_grade, delete_student_confirm

urlpatterns = [
    path('', home, name='home'),
    path('students/', student_list, name='student_list'),
    path('students/<int:student_id>/', student_detail, name='student_detail'),
    path('add_grade/', add_grade, name='add_grade'),
    path('add_student/', add_student, name='add_student'),
    path('delete_grade/<int:grade_id>/', delete_grade, name='delete_grade'),
    path('delete_student_confirm/<int:student_id>/', delete_student_confirm, name='delete_student_confirm'),
]
