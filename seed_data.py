import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from apps_main.models import User, ClassLevel, Subject, Teacher, TeacherSubject, Student, AcademicYear, SchoolProfile

def seed():
    # 1. School Profile
    sp, _ = SchoolProfile.objects.get_or_create(
        name='PKBM Darul Ulum Agrabinta',
        defaults={
            'principal_name': 'H. Ahmad Syauqi, M.Pd.',
            'address': 'Jl. Raya Agrabinta No. 12, Cianjur, Jawa Barat',
            'nip': '197501012000031001'
        }
    )

    # 2. Academic Year
    ay, _ = AcademicYear.objects.get_or_create(
        year='2023/2024',
        semester=1,
        defaults={'is_active': True}
    )

    # 3. Class Level
    cl_b, _ = ClassLevel.objects.get_or_create(
        name='Kelas 7-A',
        defaults={'program': 'PAKET_B', 'phase': 'D'}
    )
    cl_c, _ = ClassLevel.objects.get_or_create(
        name='Kelas 10-A',
        defaults={'program': 'PAKET_C', 'phase': 'E'}
    )

    # 4. Subjects
    math, _ = Subject.objects.get_or_create(name='Matematika', defaults={'code': 'MAT-01'})
    indo, _ = Subject.objects.get_or_create(name='Bahasa Indonesia', defaults={'code': 'IND-01'})

    # 5. Teacher
    t_user, created = User.objects.get_or_create(
        username='guru1',
        defaults={
            'email': 'guru1@example.com',
            'first_name': 'Budi',
            'last_name': 'Santoso',
            'role': 'TEACHER'
        }
    )
    if created:
        t_user.set_password('guru123')
        t_user.save()
    
    teacher, _ = Teacher.objects.get_or_create(user=t_user, defaults={'nip': '198005052010011001'})
    
    # 6. Teacher-Subject Assignments
    TeacherSubject.objects.get_or_create(teacher=teacher, subject=math, class_level=cl_b)
    TeacherSubject.objects.get_or_create(teacher=teacher, subject=indo, class_level=cl_b)

    # 7. Students
    s1_user, created = User.objects.get_or_create(
        username='siswa1',
        defaults={
            'email': 'siswa1@example.com',
            'first_name': 'Andi',
            'last_name': 'Pratama',
            'role': 'STUDENT'
        }
    )
    if created:
        s1_user.set_password('siswa123')
        s1_user.save()
    Student.objects.get_or_create(user=s1_user, defaults={'nisn': '0012345678', 'class_level': cl_b})

    s2_user, created = User.objects.get_or_create(
        username='siswa2',
        defaults={
            'email': 'siswa2@example.com',
            'first_name': 'Siti',
            'last_name': 'Aminah',
            'role': 'STUDENT'
        }
    )
    if created:
        s2_user.set_password('siswa123')
        s2_user.save()
    Student.objects.get_or_create(user=s2_user, defaults={'nisn': '0012345679', 'class_level': cl_b})

    print("Demo data seeded successfully!")
    print("- Admin: admin / admin")
    print("- Teacher: guru1 / guru123")
    print("- Student: siswa1 / siswa123")

if __name__ == "__main__":
    seed()
