# Generated by Django 2.2.2 on 2019-06-27 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ordering_Information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('material_1', models.CharField(max_length=120)),
                ('material_2', models.CharField(max_length=120)),
                ('material_3', models.CharField(max_length=120)),
                ('description_1', models.CharField(max_length=300)),
                ('description_2', models.CharField(max_length=300)),
                ('description_3', models.CharField(max_length=300)),
                ('packaging_1', models.CharField(max_length=100)),
                ('packaging_2', models.CharField(max_length=100)),
                ('packaging_3', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Specifications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hpis_code_1', models.CharField(max_length=100)),
                ('hpis_code_2', models.CharField(max_length=100)),
                ('hpis_code_3', models.CharField(max_length=100)),
                ('S999_200_40_0_1', models.CharField(max_length=100)),
                ('S999_200_40_0_2', models.CharField(max_length=100)),
                ('S999_200_40_0_3', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='pre_price',
            field=models.DecimalField(decimal_places=2, default=99.99, max_digits=20),
        ),
        migrations.AddField(
            model_name='product',
            name='ordering_information',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Ordering_Information'),
        ),
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Specifications'),
        ),
    ]
