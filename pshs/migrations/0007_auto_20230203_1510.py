# Generated by Django 3.1.3 on 2023-02-03 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pshs', '0006_auto_20230203_0915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='assembly',
        ),
        migrations.DeleteModel(
            name='apply',
        ),
        migrations.DeleteModel(
            name='info',
        ),
        migrations.DeleteModel(
            name='Recurit',
        ),
    ]
