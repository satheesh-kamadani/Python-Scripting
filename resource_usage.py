# Getting the cpu and memory usage using python script

import psutil

def monitor_resource_usage():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_usage = psutil.virtual_memory().percent
    print(f"CPU usage:  {cpu_usage}%")
    print(f"Memory usgage: {memory_usage}%")

monitor_resource_usage()