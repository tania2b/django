# Generated by Django 4.1.4 on 2023-01-17 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0005_remove_task_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
    ]
