# Generated by Django 4.2.5 on 2023-09-16 16:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Donor",
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
                ("name", models.CharField(max_length=100)),
                (
                    "email_address",
                    models.EmailField(blank=True, max_length=254, null=True),
                ),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("country", models.CharField(max_length=100)),
                ("remarks", models.TextField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Donors",
            },
        ),
        migrations.CreateModel(
            name="TransactionType",
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
                (
                    "name",
                    models.CharField(max_length=100, verbose_name="Transaction Type"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name_plural": "Transaction Types",
            },
        ),
        migrations.CreateModel(
            name="Donation",
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
                ("date", models.DateField()),
                (
                    "fy",
                    models.CharField(
                        editable=False, max_length=100, verbose_name="Financial Year"
                    ),
                ),
                (
                    "amount",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Donation Amount"
                    ),
                ),
                ("dated", models.DateField()),
                ("from_to", models.CharField(max_length=100, verbose_name="From/To")),
                (
                    "on_account",
                    models.CharField(max_length=100, verbose_name="On Account"),
                ),
                (
                    "receipt_no",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Receipt No"
                    ),
                ),
                (
                    "receipt_sent",
                    models.BooleanField(default=False, verbose_name="Receipt Sent"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "donor",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="donations",
                        to="donation.donor",
                        verbose_name="Donor Name",
                    ),
                ),
                (
                    "transaction_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="donation.transactiontype",
                        verbose_name="Transaction Type",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Donations",
            },
        ),
    ]
