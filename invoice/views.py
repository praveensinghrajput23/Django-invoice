from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.template.loader import get_template
from django.http import HttpResponse
from django.views import View
from .models import LineItem, Invoice
from .forms import LineItemFormset, InvoiceForm

import pdfkit

class InvoiceListView(View):
    def get(self, *args, **kwargs):
        invoices = Invoice.objects.all()
        context = {
            "invoices":invoices,
        }

        return render(self.request, 'invoice/invoice-list.html', context)
    
    def post(self, request):        
        
        invoice_ids = request.POST.getlist("invoice_id")
        invoice_ids = list(map(int, invoice_ids))

        update_status_for_invoices = int(request.POST['status'])
        invoices = Invoice.objects.filter(id__in=invoice_ids)
        
        if update_status_for_invoices == 0:
            invoices.update(status=False)
        else:
            invoices.update(status=True)

        return redirect('invoice:invoice-list')

def createInvoice(request):
    """
    Invoice Generator page it will have Functionality to create new invoices, 
    this will be protected view, only admin has the authority to read and make
    changes here.
    """

    
    if request.method == 'GET':
        formset = LineItemFormset(request.GET or None)
        form = InvoiceForm(request.GET or None)
    elif request.method == 'POST':
        formset = LineItemFormset(request.POST)
        form = InvoiceForm(request.POST)
        
        if form.is_valid():
            invoice = Invoice.objects.create(buyer=form.data["buyer"],
                    buyer_phone=form.data["buyer_phone"],
                    buyer_address = form.data["buyer_address"],
                    seller=form.data["seller"],
                    seller_phone=form.data["seller_phone"],
                    seller_address = form.data["seller_address"],
                    date=form.data["date"],
                    )
            
            
        if formset.is_valid():
            
            total = 0
            for form in formset:
                service = form.cleaned_data.get('service')
                
                quantity = form.cleaned_data.get('quantity')
                rate = form.cleaned_data.get('rate')
                tax = form.cleaned_data.get('tax')
                if service  and quantity and rate and tax:
                    sub_amount = float(rate)*float(quantity)
                    tax_amount = sub_amount*float(tax/100)
                    amount = float(rate)*float(quantity) + tax_amount


                    total += amount
                    LineItem(buyer=invoice,
                            service=service,
                            sub_amount =sub_amount,
                            quantity=quantity,
                            rate=rate,
                            tax=tax,
                            amount=amount).save()
            invoice.total_amount = total
            invoice.save()
            try:
                generate_PDF(request, id=invoice.id)
            except Exception as e:
                print(f"********{e}********")
            return redirect('/')
    context = {
        "title" : "Invoice Generator",
        "formset": formset,
        "form": form,
    }
    return render(request, 'invoice/invoice-create.html', context)


def view_PDF(request, id=None):
    invoice = get_object_or_404(Invoice, id=id)
    lineitem = invoice.lineitem_set.all()

    context = {
        "invoice_id": invoice.id,
        "invoice_total": invoice.total_amount,
        "buyer": invoice.buyer,
        "buyer_phone": invoice.buyer_phone,
        "buyer_address": invoice.buyer_address,
        "seller": invoice.seller,
        "seller_phone": invoice.seller_phone,      
        "seller_address": invoice.seller_address,
        "date": invoice.date,   
        "lineitem": lineitem,

    }
    return render(request, 'invoice/pdf_template.html', context)


def generate_PDF(request, id):
    # Use False instead of output path to save pdf to a variable
    path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    pdf = pdfkit.from_url(request.build_absolute_uri(reverse('invoice:invoice-detail', args=[id])), False, configuration=config)
    response = HttpResponse(pdf,content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="invoice.pdf"'

    return response


def change_status(request):
    return redirect('invoice:invoice-list')

def view_404(request,  *args, **kwargs):

    return redirect('invoice:invoice-list')

def invoicedelete(request, id):
    invoice = Invoice.objects.get(id=id)
    invoice.delete()
    return redirect('/')