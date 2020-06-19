from django.contrib import admin

# Register your models here.
from home.models import UserProfile, FAQ, ContactForm, Setting


class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'status', 'create_at')
    list_filter = ('status', 'create_at')



class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['usernames', 'user', 'phone', 'country', 'image_tag']
    readonly_fields = ('image_tag',)


class FAQAdmin(admin.ModelAdmin):
    list_display = ['order_number', 'question', 'answer', 'status']
    list_filter = ['status']


admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(FAQ, FAQAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile, UserProfileAdmin)
