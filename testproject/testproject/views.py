from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.views.generic.base import View, TemplateView

from .tasks import test_task


class EnqueueView(View):

    def get(self, request):
        result = test_task.delay()
        return HttpResponseRedirect('/progress/?task_id={}'.format(
            result.task_id))


class ProgressBarView(TemplateView):
    template_name = 'progress.html'

    def get_context_data(self, **kwargs):
        context = super(ProgressBarView, self).get_context_data(**kwargs)
        context.update({
            'task_id': self.request.GET.get('task_id'),
        })
        return context
