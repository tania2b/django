# Generated by Django 4.1.4 on 2023-02-08 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0009_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='project',
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ManyToManyField(blank=True, to='todo.project'),
        ),
    ]
