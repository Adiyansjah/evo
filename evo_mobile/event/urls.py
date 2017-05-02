from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^events$', views.event_list, name='events'),
    url(r'^calendar$', views.calendar, name='calendar'),
    url(r'^events/(?P<event_id>[\w-]+)$',
        views.event_details, name='event-detail'),
]
