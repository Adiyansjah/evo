from django.contrib import admin

from .models import Category, Event, Ticket


class TicketInline(admin.TabularInline):
    model = Ticket

class EventAdmin(admin.ModelAdmin):
    inlines = [TicketInline]

admin.site.register(Category)
admin.site.register(Event, EventAdmin)
admin.site.register(Ticket)