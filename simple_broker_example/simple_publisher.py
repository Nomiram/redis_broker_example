'''simple_publisher.py'''

import redis
r = redis.Redis(host='localhost', port=6379, db=0)
# Опубликовать значение message в list listname
r.rpush('my-list-1', 'my data')
