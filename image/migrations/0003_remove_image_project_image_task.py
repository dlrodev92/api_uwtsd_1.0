import django.db.models.deletion
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_rename_name_image_alt_image_text'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='project',
        ),
        migrations.AddField(
            model_name='image',
            name='task',
            field=models.ForeignKey(
                null=True,  # Allow null values if there are existing images without tasks
                on_delete=django.db.models.deletion.CASCADE,
                related_name='images',
                to='task.task'
            ),
        ),
    ]
