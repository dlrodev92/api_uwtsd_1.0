# Generated by Django 5.1.1 on 2024-09-23 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_remove_image_project_image_task'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='task',
            new_name='task',
        ),
    ]
