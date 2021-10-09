from django.contrib import admin
from .models import Withdraw
from account.models import Account, Launch
# Register your models here.
@admin.register(Withdraw)
class WithdrawAdmin(admin.ModelAdmin):
  list_display = ('account', 'value_in_cents', 'month_at', 'year_at')

  def save_model(self, request, obj, form, change):
    account = Account.objects.filter(id=obj.account_id).first()
    last_launch = Launch.objects.filter(account=account).order_by('created_at').last()
    launch = Launch(account=account, value_in_cents=( last_launch.value_in_cents - obj.value_in_cents ))
    launch.save()
    obj.save()