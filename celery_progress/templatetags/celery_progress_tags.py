from django import template
from django.core.urlresolvers import reverse_lazy

from .. import backend

register = template.Library()


@register.simple_tag
def task_progress(task_id):
    return backend.get_progress(task_id)


@register.inclusion_tag('celery_progress/progress_bar.html')
def progress_bar(element_id, task_id):
    return {
        'element_id': element_id,
        'task_id': task_id,
        'progress_url': reverse_lazy('celery_progress:progress', kwargs={
            'task_id': task_id,
        }),
    }
