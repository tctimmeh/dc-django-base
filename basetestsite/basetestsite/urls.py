from dcbasetest.views import home, popupForm
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'', include('dcbase.urls')),
    url(r'^$', home, name='home'),
    url(r'^popupForm/$', popupForm, name='popupAjaxForm'),
)
