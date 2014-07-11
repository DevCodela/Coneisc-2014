from django.conf.urls import patterns, include, url

from .views import HomeDashboardTemplateView, Enroll

urlpatterns = patterns('',

    url(r'^$' , HomeDashboardTemplateView.as_view(), name='home'),
    url(r'^enroll/$' , Enroll.as_view(), name='enroll'),

)