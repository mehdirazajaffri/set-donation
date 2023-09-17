import csv
import io
from datetime import datetime

from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.forms import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import path

from donation.models import Donation, TransactionType, Donor

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = "The Set"
admin.site.index_title = "The Set"

admin.site.register(TransactionType)


@admin.register(Donor)
class DonorAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "email_address",
        "phone_number",
        "country",
        "total_donation",
        "total_donation_this_year",
        "total_donation_last_year",
        "donation_counts",
    )
    list_filter = ("country",)
    search_fields = ("name", "email_address", "phone_number", "country", "remarks")


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    change_list_template = "admin/donation/donations_change_list.html"

    list_display = (
        "receipt_no",
        "transaction_type",
        "fy",
        "amount",
        "dated",
        "from_to",
        "on_account",
        "donor",
        "receipt_sent",
    )
    list_filter = (
        "transaction_type",
        "fy",
        "receipt_sent",
        "donor__country",
        "on_account",
    )
    search_fields = (
        "receipt_no",
        "from_to",
        "on_account",
        "donor__name",
        "donor__email_address",
        "donor__phone_number",
        "donor__country",
        "remarks",
    )
    autocomplete_fields = ("donor",)

    actions = [
        "import_csv",
    ]

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("import-csv/", self.import_csv),
        ]
        return custom_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            try:
                csv_file = request.FILES["csv_file"]
                if not csv_file.name.endswith(".csv"):
                    self.message_user(request, "This is not a csv file")
                    return HttpResponseRedirect("../")
                io_string = io.StringIO(csv_file.read().decode("utf-8"))
                reader = csv.DictReader(io_string)
                for row in reader:
                    donor, _ = Donor.objects.get_or_create(
                        name=row["from_to"],
                        email_address=row["email"],
                        phone_number=row["phone_no"],
                        country=row["country"],
                    )
                    transaction_type, _ = TransactionType.objects.get_or_create(
                        name=row["type"]
                    )
                    Donation.objects.create(
                        date=datetime.strptime(row["date"], "%d-%b-%y").date(),
                        transaction_type=transaction_type,
                        fy=row["fy"],
                        amount=row["amount"],
                        dated=datetime.strptime(row["dated"], "%d-%b-%y").date(),
                        from_to=row["from_to"],
                        on_account=row["on_account_of"],
                        donor=donor if "C" in transaction_type.name else None,
                        receipt_no=row["no"],
                    )
                self.message_user(request, "Your csv file has been imported")
                return HttpResponseRedirect("../")
            except Exception as e:
                self.message_user(request, f"Error: {e}", level="error")
                return HttpResponseRedirect("../")
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)


class CsvImportForm(forms.Form):
    csv_file = forms.FileField(label="CSV file")
