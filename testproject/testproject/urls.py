from django.conf.urls import patterns, include, url

from .views import EnqueueView, ProgressBarView

urlpatterns = patterns(
    '',
    url(r'^task/', include('celery_progress.urls',
                           namespace='celery_progress')),
    url(r'^enqueue/$', EnqueueView.as_view()),
    url(r'^progress/$', ProgressBarView.as_view()),
)
