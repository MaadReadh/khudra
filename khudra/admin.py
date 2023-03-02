from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Outlet)
admin.site.register(List)
admin.site.register(Order)
admin.site.register(Debts)
admin.site.register(Customer)