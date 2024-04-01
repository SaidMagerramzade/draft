from django.db import models
from django.utils import timezone

# Create your models here.
class Transaction(models.Model):
    transaction_id = models.CharField(max_length=100, default=True)
    transaction_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True, null=True)
    amount = models.FloatField(default=0, help_text="AZN")
    receiver_account = models.CharField(max_length=32, null=True)
    sender_account = models.CharField(max_length=32, null=True)
    currency = models.CharField(max_length=3, default='AZN')
    #status = models.CharField(max_length=20, choices=)
    notes = models.TextField(blank=True, null=True)