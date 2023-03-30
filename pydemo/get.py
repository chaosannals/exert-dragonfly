import redis

r = redis.Redis(host='localhost', port=46379, db=0)
print(r.get('foo'))
print(r.get('boo'))
