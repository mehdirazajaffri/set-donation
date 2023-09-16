from django.test import TestCase

from donation.models import Donation


# Create your tests here.


class TestDonation(TestCase):
    def test_donation(self):
        self.assertEqual(1, 1)

    def test_create_donation(self):
        Donation.objects.create(
            date="2021-01-01",
            transaction_type="1",
            fy="2021",
            amount="1000",
            dated="2021-01-01",
            from_to="test",
            on_account="test",
            donor="1",
            receipt_no="1",
            receipt_sent="1",
        )
