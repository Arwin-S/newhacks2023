import redis
import time
import random
from datetime import datetime
import random
from matplotlib import pyplot as plt
import seaborn as sns

sns.set(style="dark") 
plt.style.use("dark_background")

# Database Credentials

host = 'redis-14753.c279.us-central1-1.gce.cloud.redislabs.com'
port = 14753
password = 'Clny2osKL7XFa0ySfeOZPKg67aVMeL7N'

# Interfacing
redis_client = redis.StrictRedis(host=host, port=port, password=password, db=0)

# Publish to database
redis_client.set('oh', 'value')

# Get from database
# print(redis_client.get('name'))


redis_client.set('key', 'value')


ts = redis_client.ts()
# ts.create('ts_key')

# Empty timeseries before writing

retention_time = 1000000 # 1 hour retention
try:
    ts.delete("det", "-", "+")
except Exception as e:
    print("")


try:
    ts.create("human",  retention_msecs=retention_time)
    ts.create("chair",  retention_msecs=retention_time)
    ts.create("table",  retention_msecs=retention_time)

except Exception as e:
    print("")

classes = ({"human":0.8}, {"chair":0.1}, {"table":0.1})

# Extract the class names and their corresponding probabilities
class_names = [list(c.keys())[0] for c in classes]
probabilities = [list(c.values())[0] for c in classes]

humanCount = 0
chairCount = 0
tableCount = 0


count = [0 , 0 , 0]
while True:
    for i in range(20):
        
        chosen_class = random.choices(class_names, probabilities)[0]
        index = class_names.index(chosen_class)
        count[index] += 1
    
    ts.add("human", "*", count[0], retention_msecs=retention_time)
    ts.add("chair", "*", count[1], retention_msecs=retention_time)
    ts.add("table", "*", count[2], retention_msecs=retention_time)

    # data = ts.range("det", "-", "+")
    
    # print(count)

    plt.bar(class_names, count)
    # plt.show()

    # x = [item[0] for item in data]
    # y = [item[1] for item in data]
    
    # x = [i - x[0] for i in x]

    # print(x)
    # print(datetime.utcfromtimestamp(x[0] // 1000))
    # plt.xlim(min(x), max(x))
    # plt.ylim(min(y), max(y))
    
    # plt.plot(x, y)
    plt.pause(0.005)
    plt.clf()

    time.sleep(0.25)
    print(ts.range("human", "-", "+"))

# plt.show()


# Display max
# print(data)


# ts.get("ts_key")

# r = redis.Redis(decode_responses=True)
# ts = r.ts()

# ts.create("ts_key")


# for i in range(6):
#     ts.add("ts_key", "*")
