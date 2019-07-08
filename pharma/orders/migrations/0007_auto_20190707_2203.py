# Generated by Django 2.2.2 on 2019-07-07 22:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_order_billing_adress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='shipping_adress',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_adress_id', to='adresse.Address'),
        ),
    ]