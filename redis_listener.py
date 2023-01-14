'''redis_listener.py'''

import redis

r = redis.Redis(host='localhost', port=6379, db=0)
listname = "my-list-1"
print(f'listen "{listname}"')

while True:
    # Блокирующее чтение списка, возвращает список: (b'имя списка', b'значение')
    message = r.blpop(listname)
    if message:
        print((message[1]).decode())
