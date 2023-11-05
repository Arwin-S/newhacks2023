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
    host = 'redis-15344.c99.us-east-1-4.ec2.cloud.redislabs.com'
    port = 15344
    password = ''

    # Interfacing
    redis_client = redis.StrictRedis(
        host=host, port=port, password=password, db=0)

    ts = redis_client.ts()

    # try:
    #     ts.delete("det", "-", "+")
    # except Exception as e:
    #     print("")

    percepter = Yolo()

    while True:
        percepter.take_img()
        output = percepter.infer()
        # print(type(output))
        for class_name, count in output.items():
            print(class_name, count)
            ts.add(class_name, "*", count)
