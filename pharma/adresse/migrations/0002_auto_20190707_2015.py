# Generated by Django 2.2.2 on 2019-07-07 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adresse', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_type',
            field=models.CharField(blank=True, choices=[('billing', 'Billing'), ('shipping', 'Shipping')], max_length=120, null=True),
        ),
    ]