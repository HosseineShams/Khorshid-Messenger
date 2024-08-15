# Generated by Django 5.0.4 on 2024-04-25 11:26

import django.core.validators
import user.models
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="customuser",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="uploads/",
                validators=[
                    user.models.file_size,
                    django.core.validators.FileExtensionValidator(
                        ["png", "jpg", "jpeg", "webp", "jfif"]
                    ),
                ],
            ),
        ),
    ]
