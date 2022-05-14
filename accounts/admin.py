from django.contrib import admin
from accounts.models import Profile
# Register your models here.
# # admin.site.register(Profile)
# @admin.site.register(Profile)
# class ProfileAdmin(admin.ModelAdmin):
#     list_display=['is_email_verified','email_token','profile_image']

admin.site.register(Profile)