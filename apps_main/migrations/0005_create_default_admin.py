from django.db import migrations
from django.contrib.auth.hashers import make_password


def create_default_admin(apps, schema_editor):
    User = apps.get_model('apps_main', 'User')

    if User.objects.exists():
        return

    user = User(
        username='admin',
        email='',
        first_name='Admin',
        role='ADMIN',
        is_staff=True,
        is_superuser=True,
        password=make_password('admin'),
    )
    user.save()


class Migration(migrations.Migration):
    dependencies = [
        ('apps_main', '0004_classlevel_homeroom_teacher'),
    ]

    operations = [
        migrations.RunPython(create_default_admin, migrations.RunPython.noop),
    ]
