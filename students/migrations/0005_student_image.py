# Generated by Django 4.1.7 on 2023-04-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_remove_student_age_student_date_of_birth_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='students'),
        ),
    ]