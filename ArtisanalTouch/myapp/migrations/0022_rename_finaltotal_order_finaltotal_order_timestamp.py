# Generated by Django 5.0.1 on 2024-03-10 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0021_alter_order_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='Finaltotal',
            new_name='finaltotal',
        ),
        migrations.AddField(
            model_name='order',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
