# Generated by Django 5.1 on 2024-10-02 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_personaldetail_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldetail',
            name='user',
        ),
    ]