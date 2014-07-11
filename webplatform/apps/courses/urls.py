from django.conf.urls import patterns, include, url

from .views import CourseDetailView

urlpatterns = patterns('',

    url(r'^courses/(?P<slug>[-\w]+)/$', CourseDetailView.as_view(), name='detail_course'),

)