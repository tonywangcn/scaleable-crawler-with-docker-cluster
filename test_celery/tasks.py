from __future__ import absolute_import
from test_celery.celery import app
import time,requests
from pymongo import MongoClient
client = MongoClient('10.1.1.234', 27018) # change the ip and port to your mongo database's
db = client.mongodb_test
collection = db.celery_test
post = db.test
@app.task(bind=True,default_retry_delay=10) # set a retry delay, 10 equal to 10s
def longtime_add(self,i):
    print 'long time task begins'
    try:
        r = requests.get(i)
        post.insert({'status':r.status_code,"creat_time":time.time()}) # store status code and current time to mongodb
        print 'long time task finished'
    except Exception as exc:
        raise self.retry(exc=exc)
    return r.status_code
