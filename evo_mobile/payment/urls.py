from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^buy_ticket/(?P<event_id>[\w-]+)$', views.buy_ticket),
    url(r'^receipt/(?P<receipt_id>[\w-]+)', views.show_receipt),
]