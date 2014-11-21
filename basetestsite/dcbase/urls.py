from django.conf.urls import url, include
from dcbase.views.profile import profileView
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/profile/$', profileView, name = 'account_profile'),
]
