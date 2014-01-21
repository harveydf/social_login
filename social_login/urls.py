from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'home.views.home', name='home'),
    url(r'^login/$', 'home.views.enter', name='enter'),
    url(r'^log-out/$', 'home.views.log_out', name='log-out'),
    url('', include('social.apps.django_app.urls', namespace='social')),
)
