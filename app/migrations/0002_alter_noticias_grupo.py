# Generated by Django 5.0.2 on 2024-04-05 21:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="noticias",
            name="grupo",
            field=models.ForeignKey(
                null=True, on_delete=django.db.models.deletion.RESTRICT, to="app.grupos"
            ),
        ),
    ]
