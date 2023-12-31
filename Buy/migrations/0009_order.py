# Generated by Django 4.2.5 on 2023-09-18 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Buy', '0008_remove_cart_quantity_cart_choices_product_desc_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254, verbose_name='Customer Name')),
                ('amount', models.FloatField(verbose_name='Amount')),
                ('status', models.CharField(choices=[('SUCCESS', 'Success'), ('FAILURE', 'Failure'), ('PENDING', 'Pending')], default='PENDING', max_length=254, verbose_name='Payment Status')),
                ('provider_order_id', models.CharField(max_length=40, verbose_name='Order ID')),
                ('payment_id', models.CharField(max_length=36, verbose_name='Payment ID')),
                ('signature_id', models.CharField(max_length=128, verbose_name='Signature ID')),
            ],
        ),
    ]
