# Generated by Django 3.2.18 on 2023-04-05 21:59

from django.db import migrations, models

import aap_eda.core.enums
import aap_eda.core.utils.crypto.fields


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0017_project_import_error"),
    ]

    operations = [
        migrations.CreateModel(
            name="Credential",
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
                ("name", models.TextField(unique=True)),
                ("description", models.TextField(blank=True, default="")),
                (
                    "credential_type",
                    models.TextField(
                        choices=[("registry", "registry")],
                        default=aap_eda.core.enums.CredentialType["REGISTRY"],
                    ),
                ),
                ("username", models.TextField(null=True)),
                (
                    "secret",
                    aap_eda.core.utils.crypto.fields.EncryptedTextField(
                        null=True
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "db_table": "core_credential",
            },
        ),
        migrations.AddConstraint(
            model_name="credential",
            constraint=models.CheckConstraint(
                check=models.Q(("name", ""), _negated=True),
                name="ck_empty_credential_name",
            ),
        ),
    ]
