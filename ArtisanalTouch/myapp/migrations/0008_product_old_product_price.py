# Generated by Django 5.0.1 on 2024-02-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_alter_contact_us_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Old_Product_price',
            field=models.FloatField(null=True),
        ),
    ]
