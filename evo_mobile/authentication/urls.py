from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^login$', views.login, name='login'),
    url(r'^signup$', views.register, name='signup'),
    url(r'^account/create', views.create_user, name='create-user'),
    url(r'^auth', views.authentication, name='authentication'),
]