from django.db import models
from djmoney.models.fields import MoneyField
import uuid

# Create your models here.
class Category(models.Model):
  id = models.UUIDField(db_index=True, primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField('Nome da categoria', max_length=190)
  #Cor

  def __str__(self):
      return self.name

  class Meta:
    verbose_name = 'Categoria'
    verbose_name_plural = 'Categorias'

# Create your models here.
class Account(models.Model):
  id = models.UUIDField(db_index=True, primary_key=True, default=uuid.uuid4, editable=False)
  name = models.CharField('Nome da conta', max_length=190)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None )
  balance_initial = MoneyField('Saldo Inicial', max_digits=14, decimal_places=2, default_currency='BRL')

  def __str__(self):
      return self.name
  
  class Meta:
    verbose_name = 'Conta'
    verbose_name_plural = 'Contas'

class Launch(models.Model):
  id = models.UUIDField(db_index=True, primary_key=True, default=uuid.uuid4, editable=False)
  account = models.ForeignKey(Account, verbose_name="Contas", on_delete=models.CASCADE, default=None)
  value_in_cents = MoneyField('Saldo Atual', max_digits=14, decimal_places=2, default_currency='BRL')
  created_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return str(self.value_in_cents)

  class Meta:
    verbose_name = 'Lançamento'
    verbose_name_plural = 'Lançamentos'
