from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import (
    User, SchoolProfile, AcademicYear, ClassLevel, Subject,
    Teacher, TeacherSubject, Student, Grade, Attendance,
    P5Project, TeacherNote, Attitude
)

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'role', 'is_staff')
    list_filter = ('role', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    fieldsets = UserAdmin.fieldsets + (
        ('Role Info', {'fields': ('role', 'photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role Info', {'fields': ('role', 'photo')}),
    )

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('user', 'nisn', 'class_level')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'nisn')
    list_filter = ('class_level',)

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('user', 'nip')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'nip')

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'numeric_grade', 'academic_year')
    list_filter = ('subject', 'academic_year', 'student__class_level')
    search_fields = ('student__user__first_name', 'student__user__last_name', 'subject__name')

@admin.register(ClassLevel)
class ClassLevelAdmin(admin.ModelAdmin):
    list_display = ('name', 'program', 'phase')
    list_filter = ('program', 'phase')

@admin.register(AcademicYear)
class AcademicYearAdmin(admin.ModelAdmin):
    list_display = ('year', 'semester', 'is_active')
    list_filter = ('is_active',)

admin.site.register(SchoolProfile)
admin.site.register(Subject)
admin.site.register(TeacherSubject)
admin.site.register(Attendance)
admin.site.register(P5Project)
admin.site.register(TeacherNote)
admin.site.register(Attitude)
