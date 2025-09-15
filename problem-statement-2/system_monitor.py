import psutil
import time

def check_system_health():
# Checks CPU, memory, and disk usage and prints alerts if limit exceeded.
   
    CPU_THRESHOLD = 80.0  
    MEMORY_THRESHOLD = 80.0  
    DISK_THRESHOLD = 90.0  
    
   
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_info = psutil.disk_usage('/')

   
    if cpu_usage > CPU_THRESHOLD:
        print(f"ALERT: High CPU Usage! Current usage is {cpu_usage:.2f}%")
    
    if memory_info.percent > MEMORY_THRESHOLD:
        print(f"ALERT: High Memory Usage! Current usage is {memory_info.percent:.2f}%")

    if disk_info.percent > DISK_THRESHOLD:
        print(f"ALERT: High Disk Usage! Current usage is {disk_info.percent:.2f}%")

    num_processes = len(psutil.pids())
  
    if num_processes > 500: 
        print(f"ALERT: A large number of processes are running: {num_processes}")

if __name__ == "__main__":
    while True:
        check_system_health()
        time.sleep(60)  # Check every 60 seconds