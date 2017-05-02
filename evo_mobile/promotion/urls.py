from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^promotions$', views.promo_list, name='promos'),
    url(r'^promotions/(?P<promo_id>[\w-]+)$', views.promo_details, name='promo-detail'),
]
