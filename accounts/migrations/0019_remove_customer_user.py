# Generated by Django 3.0 on 2020-03-11 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
