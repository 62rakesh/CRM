# Generated by Django 3.0 on 2020-02-18 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200216_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
    ]