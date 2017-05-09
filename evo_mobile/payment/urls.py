from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^buy_ticket/(?P<event_id>[\w-]+)$', views.buy_ticket, name='buy-ticket'),
    url(r'^receipt$', views.show_receipt, name='receipt'),
    url(r'^save_receipt$', views.save_receipt, name='save-receipt'),
    url(r'^my_ticket$', views.show_my_tickets, name='my-ticket'),
]