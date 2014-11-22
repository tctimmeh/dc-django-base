from dcbasetest.views import home, authwall
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'', include('dcbase.urls')),
    url(r'^$', home),
    url(r'^auth/$', authwall, name = "authwall"),
)
