import redis
import time
import random
from datetime import datetime
import random
from matplotlib import pyplot as plt
import seaborn as sns

# Seaborn styling
sns.set(style="dark")
plt.style.use("dark_background")

# Database Credentials
host = 'redis-15344.c99.us-east-1-4.ec2.cloud.redislabs.com'
port = 15344
password = ''

all_classes = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard', 38: 'tennis racket',
               39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 78: 'hair drier', 79: 'toothbrush'}

cls = list(all_classes.values())


# Interfacing
redis_client = redis.StrictRedis(host=host, port=port, password=password, db=0)

ts = redis_client.ts()

count = []

for i in range(0, len(cls) - 1):
    count.append(i)

while True:

    c = 0

    # Calculation accumulation per class.
    for __, name in all_classes.items():
        try:
            data = ts.range(name, "-", "+")
            x = [item[1] for item in data]
            count[c] = sum(x)
        except Exception as e:
            print("")

        c += 1

    # Largest 5 values and their keys.
    combined_dict = dict(zip(cls, count))
    values = list(combined_dict.values())
    sorted_values = sorted(values, reverse=True)

    largest_5_values = sorted_values[:5]
    keys_for_largest_values = [
        key for key, value in combined_dict.items() if value in largest_5_values]

    print(keys_for_largest_values)
    print(largest_5_values)

    # Plot.
    try:
        plt.bar(keys_for_largest_values, largest_5_values)
        plt.pause(0.005)
        plt.clf()
        time.sleep(0.25)
    except Exception as e:
        print("Plot Error!")
