# Generated by Django 3.1.7 on 2021-03-31 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0002_bill_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wallet',
            name='balance',
            field=models.CharField(max_length=25),
        ),
    ]
