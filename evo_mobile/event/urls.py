from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^events$', views.event_list, name='events'),
    url(r'^calendar$', views.calendar, name='calendar'),
    url(r'^events/(?P<event_id>[\w-]+)$',
        views.event_details, name='event-detail'),
    url(r'^reviews$', views.event_review_list, name='event-review'),
    url(r'^reviews/(?P<event_id>[\w-]+)$', views.event_review_detail, name='event-review-detail'),
    url(r'^save_comment$', views.create_review, name='create-review')
]
