from django.db import models
from datetime import date
from djmoney.models.fields import MoneyField
import uuid

from account.models import Account
# Create your models here.
MONTHS = [
    ('1', 'Janeiro'),
    ('2', 'Fevereiro'),
    ('3', 'Março'),
    ('4', 'Abril'),
    ('5', 'Maio'),
    ('6', 'Junho'),
    ('7', 'Julho'),
    ('8', 'Agosto'),
    ('9', 'Setembro'),
    ('10', 'Outubro'),
    ('11', 'Novembro'),
    ('12', 'Dezembro'),
]

today = date.today()

class Revenue(models.Model):
  id = models.UUIDField(db_index=True, primary_key=True, default=uuid.uuid4, editable=False)
  account = models.ForeignKey(Account, on_delete=models.CASCADE, default=None )
  value_in_cents = MoneyField('Valor do aporte', max_digits=14, decimal_places=2, default_currency='BRL')
  month_at = models.CharField('Mês Ativo', max_length=191, choices=MONTHS, default=today.month)
  year_at = models.CharField('Ano Ativo', max_length=191, default=today.year)
  created_at = models.DateTimeField(auto_now=True)
  

  class Meta:
    verbose_name = 'Aporte'
    verbose_name_plural = 'Aportes'
