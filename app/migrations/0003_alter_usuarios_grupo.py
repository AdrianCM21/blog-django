# Generated by Django 5.0.2 on 2024-04-05 21:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_noticias_grupo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuarios",
            name="grupo",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.CASCADE, to="app.grupos"
            ),
        ),
    ]