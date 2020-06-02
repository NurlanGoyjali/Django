from django.contrib import admin

# Register your models here.
from home.models import UserProfile




class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['usernames', 'user', 'phone', 'country', 'image_tag']
    readonly_fields = ('image_tag',)



admin.site.register(UserProfile, UserProfileAdmin)
