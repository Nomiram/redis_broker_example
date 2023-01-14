'''publisher.py'''

import sys
import redis
r = redis.Redis(host='localhost', port=6379, db=0)
listname = 'my-list-1'
basemessage = 'my data'
# r.publish('my-channel-1', 'my data')

if len(sys.argv)>1 and sys.argv[1].isdecimal():
    print(sys.argv[1])
    for i in range(int(sys.argv[1])):
        message = basemessage +'-'+str(i)

        # Опубликовать значение message в list listname
        r.rpush(listname, message)
        print(f'send "{message}" to "{listname}"')
else:
    r.rpush(listname, basemessage)
    print(f'send "{basemessage}" to "{listname}"')
