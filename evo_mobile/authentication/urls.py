from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.sigin, name='login'),
    url(r'^logout$', views.signout, name='logout'),
    url(r'^signup$', views.register, name='signup'),
    url(r'^account/create', views.create_user, name='create-user'),
    url(r'^auth', views.authentication, name='authentication'),
]