# Generated by Django 4.2.1 on 2023-08-15 11:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room_app', '0005_alter_room_details_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='room_details',
            options={'ordering': ['-created']},
        ),
    ]