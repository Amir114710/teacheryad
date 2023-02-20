# Generated by Django 4.1.6 on 2023-02-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0007_user_is_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="is_teacher",
            field=models.BooleanField(
                blank=True, default=False, null=True, verbose_name="ایا معلم است؟"
            ),
        ),
    ]
