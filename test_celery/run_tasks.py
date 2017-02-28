from .tasks import longtime_add
import time
if __name__ == '__main__':
    url = ['http://example1.com' , 'http://example2.com' , 'http://example3.com' , 'http://example4.com' , 'http://example5.com' , 'http://example6.com' , 'http://example7.com' , 'http://example8.com'] # change them to your ur list.
    for i in url:
        result = longtime_add.delay(i)
        print 'Task result:',result.result
