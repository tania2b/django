# Generated by Django 4.1.4 on 2023-01-16 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_task_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='completed',
        ),
    ]