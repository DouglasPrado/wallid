from django.contrib import admin
import decimal
from .models import Account, Category, Launch

class LaunchInline(admin.TabularInline):
    list_display = ('value_in_cents', 'created_at')
    model = Launch
    extra = 0


# Register your models here.
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
  list_display = ('name', 'category', 'saldo')
  inlines = [LaunchInline]

  def saldo(self, request):
      last_launch = Launch.objects.filter(account=request).order_by('created_at').last()
      return last_launch.value_in_cents

  def save_model(self, request, obj, form, change):
    account = Account.objects.filter(id=obj.id).first()
    if account == None:
      account = Account(id=obj.id, name=obj.name, category=obj.category, balance_initial=obj.balance_initial )
    
    account.save()
    launch = Launch(account=account, value_in_cents=account.balance_initial)
    launch.save() 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
  list_display = ('name',)  