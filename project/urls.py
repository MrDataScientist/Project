from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^', include( 'myapp.urls', namespace="myapp")),
    url(r'^admin/', admin.site.urls),
]
