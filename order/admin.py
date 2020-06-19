from django.contrib import admin

# Register your models here.
from home.models import FAQ
from order.models import ShopCart, OrderProduct, Order


class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'quantity', 'amount']
    list_filter = ['user']


def __str__(self):
    return self.product.title


class OrderProductLine(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'quantity', 'amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'total', 'status']
    list_filter = ['status']
    readonly_fields = ('user', 'address', 'city', 'country', 'phone', 'first_name', 'ip', 'last_name', 'city', 'total')
    inlines = [OrderProductLine]


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']




admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderProduct, OrderProductAdmin)

