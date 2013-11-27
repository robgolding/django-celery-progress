import json

from django.http import HttpResponse
from django.views.generic.base import View

from . import backend


class ProgressView(View):

    def get(self, request, *args, **kwargs):
        task_id = self.kwargs['task_id']
        return HttpResponse(json.dumps({
            'progress': backend.get_progress(task_id),
            'result': backend.get_result(task_id),
        }))
