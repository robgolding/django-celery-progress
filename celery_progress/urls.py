from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns(
    '',
    url(r'^progress/(?P<task_id>[\w-]+)/$', views.ProgressView.as_view(),
        name='progress'),
)
