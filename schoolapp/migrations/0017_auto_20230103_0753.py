# Generated by Django 3.2.16 on 2023-01-03 07:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0016_auto_20221212_1145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='gender',
        ),
    ]