# Generated by Django 5.0.1 on 2024-03-08 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0013_store'),
    ]

    operations = [
        migrations.AddField(
            model_name='complain',
            name='Email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
