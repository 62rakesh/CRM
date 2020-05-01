# Generated by Django 3.0 on 2020-02-21 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200221_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='event_category',
            field=models.CharField(choices=[('Birthday Party', 'Birthday Party'), ('Office Party', 'Office Party'), ('Team Outings', 'Team Outings'), ('House Party', 'House Party')], max_length=200, null=True),
        ),
    ]
