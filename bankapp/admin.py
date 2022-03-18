from django.contrib import admin
from bankapp.models import Customers,transactions
admin.site.site_header="Customer registered on my Bank"



class customersAdmin(admin.ModelAdmin):
    list_display=["name","email","phone","credits"]

admin.site.register(Customers,customersAdmin)
admin.site.register(transactions)