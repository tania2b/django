# Generated by Django 4.1.4 on 2023-02-07 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_rename_profile_image_userprofile_profile_picture'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
