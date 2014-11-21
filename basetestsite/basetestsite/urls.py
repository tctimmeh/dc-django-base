from dcbasetest.views import home
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'', include('dcbase.urls')),
    url(r'^$', home),
)
