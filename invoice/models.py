from django.db import models
from django.core.validators import RegexValidator
# Create your models here.
class Invoice(models.Model):
    buyer = models.CharField(max_length=100,)
    buyer_phone = models.CharField(null=True, max_length=100, validators=[RegexValidator(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')])
    buyer_address = models.TextField(null=True, blank=True)
    seller = models.CharField(max_length=100)
    seller_phone = models.CharField(null=True, max_length=100, validators=[RegexValidator(r'^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$')])
    seller_address = models.TextField(null=True, blank=True)
    date = models.DateField()
    total_amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    
    def __str__(self):
        return str(self.buyer,)
    
    def get_status(self):
        return self.status

    

class LineItem(models.Model):
    
    buyer =  models.ForeignKey(Invoice, on_delete=models.CASCADE,)
    seller = models.TextField()
    service = models.TextField()
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=9, decimal_places=2)
    tax = models.DecimalField(max_digits=9, decimal_places=2)
    sub_amount = models.DecimalField(max_digits=9, decimal_places=2)
    amount = models.DecimalField(max_digits=9, decimal_places=2)

    def __str__(self):
        return str(self.buyer)
   