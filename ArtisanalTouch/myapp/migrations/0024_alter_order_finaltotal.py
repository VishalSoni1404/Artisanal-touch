# Generated by Django 5.0.1 on 2024-03-10 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0023_alter_order_login_id_alter_order_pay_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='finaltotal',
            field=models.IntegerField(null=True),
        ),
    ]
