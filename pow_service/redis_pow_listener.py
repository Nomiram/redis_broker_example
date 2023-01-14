'''redis_listener.py'''

import json
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
listname = "pow-list"
print(f'listen "{listname}"')

while True:
    # Блокирующее чтение списка, возвращает список: (b'имя списка', b'значение')
    message = r.blpop(listname)
    if message:
        print((message[1]).decode())
        # Получаем аргументы из списка (ожидает {"first": int, "second": int))
        lpow = json.loads(message[1])
        result = json.dumps({"status": "ok", "result": lpow["first"]**lpow["second"]})
        print(f'{lpow["first"]}^{lpow["second"]}={result}')
        # Отправляем результат в очередь с именем <b'значение'>
        r.rpush(message[1],  result)
