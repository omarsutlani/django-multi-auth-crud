# Generated by Django 4.2.4 on 2023-09-24 02:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_task_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.FileField(default='default.jpg', upload_to='uploads'),
        ),
    ]
