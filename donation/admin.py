from django.contrib import admin
from django.contrib.auth.models import Group, User

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
