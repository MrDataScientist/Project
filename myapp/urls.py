from django.conf.urls import url
from django.views import generic

from . import views
from .models import Site

myapp_name = 'myapp'

urlpatterns = [
    url(r'^$', views.Index.as_view(), name='index'),
    url(r'^sites/(?P<pk>[0-9]+)/$', views.detail.as_view(), name='detail'),
    url(r'^summary/$', views.Sum_value.as_view(), name='summary'),
    url(r'^average/$', views.Average.as_view(), name='average'),
]