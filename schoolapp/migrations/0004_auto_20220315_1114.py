# Generated by Django 3.2.16 on 2022-03-15 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_auto_20220315_1407'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('answer_one', models.CharField(max_length=50)),
                ('answer_two', models.CharField(max_length=50)),
                ('answer_three', models.CharField(max_length=50)),
                ('answer_four', models.CharField(max_length=50)),
            ],
        ),
        migrations.DeleteModel(
            name='Answers',
        ),
        migrations.DeleteModel(
            name='QuestionChoices',
        ),
    ]