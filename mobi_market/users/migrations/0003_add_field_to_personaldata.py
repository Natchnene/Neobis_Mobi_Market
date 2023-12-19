# Generated by Django 4.2.2 on 2023-12-17 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0002_create_personaldata"),
    ]

    operations = [
        migrations.AddField(
            model_name="personaldata",
            name="user",
            field=models.OneToOneField(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="personaldata",
            name="birth_date",
            field=models.DateField(blank=True, null=True),
        ),
    ]