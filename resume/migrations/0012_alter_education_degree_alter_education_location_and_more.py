# Generated by Django 5.1 on 2024-10-02 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0011_alter_education_degree_alter_education_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='degree',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='education',
            name='university',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='company',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='location',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='workexperience',
            name='position',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]