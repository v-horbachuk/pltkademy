import socket
import multiprocessing
from psutil import virtual_memory, disk_usage

try:
    hostname = socket.gethostname()
except NotImplementedError:
    pass

try:
    cpu_number = multiprocessing.cpu_count()
except NotImplementedError:
    pass

try:
    total_memory = virtual_memory().total
except NotImplementedError:
    pass

try:
    total_disk_space = disk_usage("/").total
except NotImplementedError:
    pass

try:
    with open("./system_info.txt", "w") as file:
        data = f"Hostname: {hostname}\n" \
            f"Cpu number: {cpu_number}\n" \
            f"Total memory: {total_memory}\n" \
            f"Total disk space: {total_disk_space}\n"
        file.write(data)
except NotImplementedError:
    pass
