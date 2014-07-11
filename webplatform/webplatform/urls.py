from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    # Home urls
    url(r'^', include('apps.home.urls', namespace='home')),

    # Dashboard urls
    url(r'^', include('apps.courses.urls', namespace='courses')),

    # Django administrator
    url(r'^admin/', include(admin.site.urls)),

    # Login / Logout
    url(r'^login/$', 'django.contrib.auth.views.login', { 'template_name': 'login.html' }, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login', name='logout'),
)
