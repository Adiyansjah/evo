from django.contrib import admin

from .models import Promotion

class PromotionAdmin(admin.ModelAdmin):
    list_display = ('name', 'expired')

admin.site.register(Promotion, PromotionAdmin)
