# Generated by Django 5.0.2 on 2024-05-12 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0004_alter_noticias_imagen"),
    ]

    operations = [
        migrations.AddField(
            model_name="noticias",
            name="subtitulo",
            field=models.CharField(default="", max_length=250),
        ),
    ]
