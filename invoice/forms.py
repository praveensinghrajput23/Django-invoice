from django import forms
from django.forms import formset_factory
from .models import Invoice
class InvoiceForm(forms.Form):
    
    buyer = forms.CharField(
        label='Buyer',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buyer Name',
            'rows':1
        })
    )
    buyer_phone = forms.CharField(
        label='Buyer Phone',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Buyer Number',
            'rows':1
        })
    )
    buyer_address = forms.CharField(
        label='Buyer Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'rows':1
        })
    )
    seller = forms.CharField(
        label='Seller',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seller Name',
            'rows':1
        })
    )
    seller_phone = forms.CharField(
        label='Seller Phone',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Seller Number',
            'rows':1
        })
    )
    seller_address = forms.CharField(
        label='Buyer Address',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '',
            'rows':1
        })
    )
    

class LineItemForm(forms.Form):
    
    service = forms.CharField(
        label='Service/Product',
        widget=forms.TextInput(attrs={
            'class': 'form-control input',
            'placeholder': 'Service Name'
        })
    )
    
    quantity = forms.IntegerField(
        label='Qty',
        widget=forms.TextInput(attrs={
            'class': 'form-control input quantity',
            'placeholder': 'Quantity'
        }) 
    )
    rate = forms.DecimalField(
        label='Rate $',
        widget=forms.TextInput(attrs={
            'class': 'form-control input rate',
            'placeholder': 'Rate'
        })
    )
    tax = forms.DecimalField(
        label='TAX %',
        widget=forms.TextInput(attrs={
            'class': 'form-control input tax',
            'placeholder': 'TAX'
        })
    )

    
LineItemFormset = formset_factory(LineItemForm, extra=1)