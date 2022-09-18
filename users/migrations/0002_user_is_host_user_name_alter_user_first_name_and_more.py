# Generated by Django 4.1 on 2022-09-18 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="is_host",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="name",
            field=models.CharField(default="", max_length=150),
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(editable=False, max_length=150),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(editable=False, max_length=150),
        ),
    ]
