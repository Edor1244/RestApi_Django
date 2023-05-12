# Generated by Django 4.1 on 2023-05-11 23:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("Cartas", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254, unique=True)),
                ("password", models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name="cartas",
            name="user",
            field=models.ForeignKey(
                default=1, on_delete=django.db.models.deletion.CASCADE, to="Cartas.user"
            ),
        ),
    ]