# Generated by Django 4.1.7 on 2023-02-17 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0003_alter_teacher_user_alter_teacher_username'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='Foundation',
            field=models.CharField(default=1, max_length=15, verbose_name='پایه چندم'),
            preserve_default=False,
        ),
    ]
