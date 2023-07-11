from django.db import models

# Create your models here.
class Transaction(models.Model):
    bank_name = models.CharField(max_length=100)
    account_id = models.IntegerField()
    tr_id = models.IntegerField()

    def __str__(self):
        return self.bank_name