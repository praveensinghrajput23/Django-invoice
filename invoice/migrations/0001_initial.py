# Generated by Django 4.0.2 on 2022-02-20 21:44

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer', models.CharField(max_length=100)),
                ('buyer_phone', models.CharField(max_length=100, null=True, validators=[django.core.validators.RegexValidator('^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]\\d{3}[\\s.-]\\d{4}$')])),
                ('buyer_address', models.TextField(blank=True, null=True)),
                ('seller', models.CharField(max_length=100)),
                ('seller_phone', models.CharField(max_length=100, null=True, validators=[django.core.validators.RegexValidator('^(\\+\\d{1,2}\\s)?\\(?\\d{3}\\)?[\\s.-]\\d{3}[\\s.-]\\d{4}$')])),
                ('seller_address', models.TextField(blank=True, null=True)),
                ('date', models.DateField()),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller', models.TextField()),
                ('service', models.TextField()),
                ('quantity', models.IntegerField()),
                ('rate', models.DecimalField(decimal_places=2, max_digits=9)),
                ('tax', models.DecimalField(decimal_places=2, max_digits=9)),
                ('sub_amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoice.invoice')),
            ],
        ),
    ]
