# Generated by Django 3.2.8 on 2021-10-08 13:40

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_account_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='balance_initial',
            field=models.IntegerField(default=None, verbose_name='Saldo Inicial'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Launch',
            fields=[
                ('id', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('value_in_cents', models.IntegerField(verbose_name='Saldo Atual')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('account', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='account.account', verbose_name='Contas')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
