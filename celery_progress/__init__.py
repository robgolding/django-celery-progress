from django.conf import settings
from django.utils.module_loading import import_by_path

BACKEND = getattr(settings, 'CELERY_PROGRESS_BACKEND',
                  'celery_progress.backends.CeleryBackend')


def get_backend():
    return import_by_path(BACKEND)


backend = get_backend()()
