from celery import app
import random
import time

from celery_progress import backend


@app.task(bind=True)
def test_task(self):
    for i in range(100):
        time.sleep(float(random.randrange(1, 10))/10)
        backend.set_progress(self.request.id, i)
    return 'done'
