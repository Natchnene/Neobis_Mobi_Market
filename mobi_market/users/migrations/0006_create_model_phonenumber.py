# Generated by Django 4.2.2 on 2023-12-26 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_alter_personaldata_code_activation"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="personaldata",
            name="code_activation",
        ),
        migrations.RemoveField(
            model_name="personaldata",
            name="phone_number",
        ),
        migrations.CreateModel(
            name="PhoneNumber",
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
                ("phone_number", models.CharField(max_length=15, unique=True)),
                ("code_activation", models.PositiveIntegerField(blank=True, null=True)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
