'''redis_listener.py'''

import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
listname = "pow-list"

for i in range(10):
    message = json.dumps({"first":2,"second":i})
    # Отправляем запрос в очередь с именем <listname>
    r.rpush(listname, message)
    print(f'send "{message}" to "{listname}"')
    # Получаем результат из очереди с именем <message>
    result = r.blpop(message, timeout=1)
    if result:
        print(f'receive "{json.loads(result[1])}" from "{message}"')
    else:
        print("timeout")
        print("removed: ", r.lrem(listname, 1, message))
