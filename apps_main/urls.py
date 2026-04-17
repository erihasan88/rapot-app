from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('students/', views.manage_students, name='manage_students'),
    path('students/delete/<int:student_id>/', views.delete_student, name='delete_student'),
    path('students/export/', views.export_students_excel, name='export_students_excel'),
    path('students/import/', views.import_students_excel, name='import_students_excel'),
    path('teachers/', views.manage_teachers, name='manage_teachers'),
    path('teachers/delete/<int:teacher_id>/', views.delete_teacher, name='delete_teacher'),
    path('teachers/export/', views.export_teachers_excel, name='export_teachers_excel'),
    path('teachers/import/', views.import_teachers_excel, name='import_teachers_excel'),
    path('classes/', views.manage_classes, name='manage_classes'),
    path('subjects/', views.manage_subjects, name='manage_subjects'),
    path('academic-years/', views.manage_academic_years, name='manage_academic_years'),
    path('grades/', views.manage_grades, name='manage_grades'),
    path('settings/', views.manage_settings, name='manage_settings'),
    path('input-grades/', views.input_grades, name='input_grades'),
    path('input-grades/student/<int:student_id>/', views.student_detail_input, name='student_detail_input'),
    path('report/', views.view_report, name='view_report'),
]
