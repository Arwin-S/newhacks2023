import redis

# Database Credentials

host = 'redis-14753.c279.us-central1-1.gce.cloud.redislabs.com'
port = 14753
password = ''

# Interfacing
redis_client = redis.StrictRedis(host=host, port=port, password='', db=0)

# Publish to database
redis_client.set('key', 'value')

# Get from database
print(redis_client.get('name'))

