from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from config import settings

import event.views as event

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', event.front_page, name='home'),
    url(r'', include('authentication.urls')),
    url(r'', include('event.urls')),
    url(r'', include('promotion.urls')),
    url(r'', include('payment.urls')),
]

# The static url for debugging
if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
