import redis

r = redis.Redis(host='localhost', port=46379, db=0)
r.set('foo', 'bar')
r.set('boo', '1234')

