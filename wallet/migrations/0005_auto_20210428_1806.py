# Generated by Django 3.2 on 2021-04-28 12:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wallet', '0004_auto_20210331_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.AlterField(
            model_name='wallet',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='wallet',
            name='name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='bill',
        ),
        migrations.DeleteModel(
            name='customer',
        ),
    ]
