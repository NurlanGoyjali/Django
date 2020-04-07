from django.contrib import admin

# Register your models here.
from product.models import Category
from product.models import Product,Images

class ProductImageInLine(admin.TabularInline):
    model = Images
    extra = 3

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['title' , 'status','slug']
    list_filter = ["title" , 'status']

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title' , 'status','image_tag','slug']
    readonly_fields = ('image_tag',)
    inlines = [ProductImageInLine]

class ImageAdmin(admin.ModelAdmin):
    list_display = ['produt','image']


admin.site.register(Category,CatagoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Images,ImageAdmin)
