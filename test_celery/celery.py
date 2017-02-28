from __future__ import absolute_import
from celery import Celery
app = Celery('test_celery',broker='amqp://admin:mypass@10.1.1.234:5673',backend='rpc://',include=['test_celery.tasks'])

