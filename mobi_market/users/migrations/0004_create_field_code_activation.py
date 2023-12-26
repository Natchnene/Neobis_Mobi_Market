# Generated by Django 5.0 on 2023-12-25 14:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_add_field_to_personaldata"),
    ]

    operations = [
        migrations.AddField(
            model_name="personaldata",
            name="code_activation",
            field=models.PositiveIntegerField(blank=True, max_length=4, null=True),
        ),
    ]