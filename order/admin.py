from django.contrib import admin
from .models import Order, OrderItem, code


# Register your models here.
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    pass




@admin.register(code)
class CodeAdmin(admin.ModelAdmin):
    raw_id_fields = ("user", )