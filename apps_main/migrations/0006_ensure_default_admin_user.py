from django.db import migrations
from django.contrib.auth.hashers import make_password


def ensure_default_admin_user(apps, schema_editor):
    User = apps.get_model('apps_main', 'User')

    if User.objects.filter(username='admin').exists():
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
        ('apps_main', '0005_create_default_admin'),
    ]

    operations = [
        migrations.RunPython(ensure_default_admin_user, migrations.RunPython.noop),
    ]
