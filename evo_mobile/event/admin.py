from django.contrib import admin

from .models import Category, Event, Ticket


class TicketInline(admin.TabularInline):
    model = Ticket

class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_date', 'end_date', 'category')
    inlines = [TicketInline]

admin.site.register(Category)
admin.site.register(Event, EventAdmin)