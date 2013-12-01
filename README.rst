======================
Django Celery Progress
======================

Django Celery Progress is an app which provides a reusable way to track the
progress of Celery tasks, and render a live progress bar on any page.

Requirements
------------

* Django
* Celery

Installation
------------

Install via ``pip``::

    pip install django-celery-progress

Usage
-----

Call ``set_progress()`` from within a Celery task::

    from celery_progress import backend

    @app.task(bind=True)
    def test_task(self):
        for i in range(100):
            time.sleep(random.uniform(0, 1))
            backend.set_progress(self.request.id, i)
        return 'done'

Show an automatically updating progress bar with the ``progress_bar`` template
tag::

    {% load celery_progress_tags %}

    <script type="text/javascript" src='{% static "celery_progress/js/jquery-2.0.3.min.js" %}'></script>
    <script type="text/javascript" src='{% static "celery_progress/js/update.js" %}'></script>

    {% progress_bar 'test_task' task_id %}

    <script type='text/javascript'>
        trackProgress('test_task', function taskDone(result) {
            alert('Done! Result: ' + result);
        });
    </script>
