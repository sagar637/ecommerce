# Generated by Django 3.1.7 on 2021-03-06 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_module', '0003_cartitem'),
        ('payment_module', '0002_invoice_invoicedetails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='InvoiceDetails',
            new_name='InvoiceDetail',
        ),
    ]
