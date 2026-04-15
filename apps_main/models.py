from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    ROLE_CHOICES = (
        ('ADMIN', 'Super Admin'),
        ('TEACHER', 'Teacher'),
        ('STUDENT', 'Student'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='STUDENT')
    photo = models.ImageField(upload_to='user_photos/', null=True, blank=True)

    def __str__(self):
        return self.username

class SchoolProfile(models.Model):
    name = models.CharField(max_length=255, default="PKBM Darul Ulum Agrabinta")
    logo = models.ImageField(upload_to='school/', null=True, blank=True)
    principal_name = models.CharField(max_length=255)
    nip = models.CharField(max_length=50, blank=True, null=True)
    address = models.TextField()
    phone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    theme_color = models.CharField(max_length=20, default="#1e295b")
    signature = models.ImageField(upload_to='school/signature/', null=True, blank=True)
    stamp = models.ImageField(upload_to='school/stamp/', null=True, blank=True)

    def __str__(self):
        return self.name

class AcademicYear(models.Model):
    year = models.CharField(max_length=20) # e.g. 2023/2024
    semester = models.IntegerField(choices=((1, 'Ganjil'), (2, 'Genap')))
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.year} - {self.get_semester_display()}"

class ClassLevel(models.Model):
    PROGRAM_CHOICES = (
        ('PAKET_B', 'Paket B (SMP)'),
        ('PAKET_C', 'Paket C (SMA)'),
    )
    PHASE_CHOICES = (
        ('D', 'Fase D'),
        ('E', 'Fase E'),
        ('F', 'Fase F'),
    )
    name = models.CharField(max_length=50)
    program = models.CharField(max_length=20, choices=PROGRAM_CHOICES)
    phase = models.CharField(max_length=2, choices=PHASE_CHOICES)
    homeroom_teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True, blank=True, related_name='homeroom_classes')

    def __str__(self):
        return f"{self.name} ({self.get_program_display()})"

class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='teacher_profile')
    nip = models.CharField(max_length=50, unique=True, null=True, blank=True)
    subjects = models.ManyToManyField(Subject, through='TeacherSubject')

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class TeacherSubject(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    class_level = models.ForeignKey(ClassLevel, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('teacher', 'subject', 'class_level')

class Student(models.Model):
    GENDER_CHOICES = (
        ('L', 'Laki-laki'),
        ('P', 'Perempuan'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    nisn = models.CharField(max_length=20, unique=True)
    nis = models.CharField(max_length=20, unique=True, null=True, blank=True)
    class_level = models.ForeignKey(ClassLevel, on_delete=models.SET_NULL, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='L')
    birth_place = models.CharField(max_length=100, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    parent_name = models.CharField(max_length=255, null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username

class Grade(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    daily_test_grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    midterm_grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    final_exam_grade = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    numeric_grade = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField(help_text="Deskripsi Capaian Kompetensi")

    class Meta:
        unique_together = ('student', 'subject', 'academic_year')

class SubjectActivity(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='activities')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    activity_score = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    activity_note = models.TextField(blank=True, default='')

    class Meta:
        unique_together = ('student', 'subject', 'academic_year')

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    sakit = models.IntegerField(default=0)
    izin = models.IntegerField(default=0)
    alpha = models.IntegerField(default=0)

    class Meta:
        unique_together = ('student', 'academic_year')

class P5Project(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    score = models.CharField(max_length=100, help_text="e.g. Sangat Berkembang")

class TeacherNote(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    notes = models.TextField()

class Attitude(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.CASCADE)
    score = models.CharField(max_length=50, help_text="e.g. Baik, Sangat Baik")
    description = models.TextField()
