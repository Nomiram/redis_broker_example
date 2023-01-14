'''simple_publisher.py'''
import redis

r = redis.Redis(host='localhost', port=6379, db=0)
# Установить key123=value456
r.set("key123", "value456")
value = r.get("key123")
if value:
    print("value: ", value)
else:
    print("value is not set")
