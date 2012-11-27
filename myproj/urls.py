from django.conf.urls import patterns, include, url
from django.views.generic.simple import redirect_to
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('social_auth.urls')),
    url(r'^login/$', redirect_to, {'url':'/login/github'}),
    url(r'^home/$', 'gitrepos.views.home'),
    url(r'^$', 'gitrepos.views.login'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^gitrepos/$','gitrepos.views.gitrepos', name="repo"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name="logout"),
)
