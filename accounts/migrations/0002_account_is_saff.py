# Generated by Django 4.1.7 on 2023-04-08 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_saff',
            field=models.BooleanField(default=False),
        ),
    ]