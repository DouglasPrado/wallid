# Generated by Django 3.2.8 on 2021-10-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20211008_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='balance_initial',
            field=models.IntegerField(default=0, verbose_name='Saldo Inicial'),
        ),
    ]
