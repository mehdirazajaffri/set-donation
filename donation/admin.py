from django.contrib import admin
from django.contrib.auth.models import Group, User

from donation.models import Donation, TransactionType

admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.site_header = "The Set"
admin.site.index_title = "The Set"

admin.site.register(TransactionType)


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
        "email_address",
        "phone_number",
        "country",
        "receipt_sent",
        "remarks",
    )
    list_filter = (
        "transaction_type",
        "fy",
        "receipt_sent",
        "country",
        "from_to",
        "on_account",
    )
    search_fields = (
        "receipt_no",
        "from_to",
        "on_account",
        "email_address",
        "phone_number",
        "country",
        "remarks",
    )
