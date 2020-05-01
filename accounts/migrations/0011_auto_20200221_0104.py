# Generated by Django 3.0 on 2020-02-20 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_events'),
    ]

    operations = [
        migrations.CreateModel(
            name='event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10, null=True)),
                ('event_name', models.CharField(max_length=200, null=True)),
                ('event_category', models.CharField(choices=[('Birthday Party', 'House Party'), ('Office Party', 'Team Outing')], max_length=200, null=True)),
                ('date_created', models.DateField(auto_now_add=True, null=True)),
                ('details', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='events',
        ),
    ]
