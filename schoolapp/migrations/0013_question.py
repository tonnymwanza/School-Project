# Generated by Django 3.2.16 on 2022-12-09 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schoolapp', '0012_delete_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer_one', models.CharField(max_length=100)),
                ('answer_two', models.CharField(max_length=100)),
                ('answer_three', models.CharField(max_length=100)),
                ('answer_four', models.CharField(max_length=100)),
            ],
        ),
    ]
