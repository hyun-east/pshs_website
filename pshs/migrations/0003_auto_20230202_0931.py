# Generated by Django 3.1.3 on 2023-02-02 00:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pshs', '0002_apply_attendance_recurit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='apply',
            name='recurit',
        ),
        migrations.DeleteModel(
            name='Attendance',
        ),
        migrations.DeleteModel(
            name='apply',
        ),
        migrations.DeleteModel(
            name='Recurit',
        ),
    ]
