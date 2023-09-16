from django.db import models


class TransactionType(models.Model):
    name = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Transaction Type"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Transaction Types"


class Donation(models.Model):
    date = models.DateField(blank=False, null=False)
    transaction_type = models.ForeignKey(
        TransactionType,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name="Transaction Type",
    )
    fy = models.CharField(max_length=100, editable=False, verbose_name="Financial Year")
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Donation Amount"
    )
    dated = models.DateField(blank=False, null=False)
    from_to = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="From/To"
    )
    on_account = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="On Account"
    )
    email_address = models.EmailField(
        blank=True, null=True, verbose_name="Email Address"
    )
    phone_number = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Phone Number"
    )
    country = models.CharField(
        max_length=100, blank=False, null=False, verbose_name="Country"
    )
    remarks = models.TextField(blank=True, null=True, verbose_name="Remarks")
    receipt_no = models.CharField(
        max_length=100, blank=True, null=True, verbose_name="Receipt No"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    receipt_sent = models.BooleanField(default=False, verbose_name="Receipt Sent")

    def save(self, *args, **kwargs):
        if self.date.month >= 4:
            self.fy = self.date.year
        else:
            self.fy = self.date.year - 1
        super(Donation, self).save(*args, **kwargs)

    def __str__(self):
        return self.from_to

    class Meta:
        verbose_name_plural = "Donations"
