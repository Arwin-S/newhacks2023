import redis
import time
import random
from datetime import datetime
import random
from matplotlib import pyplot as plt
import seaborn as sns
from yolo import Yolo


if __name__ == "__main__":

    # Database Credentials
    host = 'redis-14753.c279.us-central1-1.gce.cloud.redislabs.com'
    port = 14753
    password = 'Clny2osKL7XFa0ySfeOZPKg67aVMeL7N'

    # Interfacing
    redis_client = redis.StrictRedis(host=host, port=port, password=password, db=0)

    ts = redis_client.ts()

    try:
        ts.delete("det", "-", "+")
    except Exception as e:
        print("")

    percepter = Yolo()

    while True:
        percepter.take_img()
        output = percepter.infer()
        # print(type(output))
        for class_name, count in output.items():
            print(class_name, count)
            ts.add(class_name, "*", count)


