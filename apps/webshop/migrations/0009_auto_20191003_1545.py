# Generated by Django 2.1.11 on 2019-10-03 13:45

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    dependencies = [
        ('webshop', '0008_auto_20190826_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='fiken_account',
            field=models.CharField(choices=[('sales_medals', 'Innbetaling medaljer og pins'), ('sales_exempt', 'Salgsinntekt handelsvarer, avgiftsfri'), ('sales_none', 'Salgsinntekt handelsvarer, utenfor avgiftsområdet'), ('services', 'Salgsinntekt tjenester, utenfor avgiftsområdet'), ('offline', 'Abonnement Offline'), ('sales_nibble', 'Salgsinntekt Nibble'), ('attendees_arrkom', 'Deltager avgift Arrkom'), ('attendees_galla', 'Deltakeravgift immatrikuleringsball'), ('attendees_graduation', 'Deltakeravgift utmatrikulering'), ('attendees_are', 'Deltakeravgift Åre')], default='sales_exempt', max_length=128, verbose_name='Konto i Fiken'),
            preserve_default=False,
        ),
    ]