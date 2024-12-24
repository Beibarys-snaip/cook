import time
import psuti

log_file = "system_log.txt"

# Мониторинг системных ресурсов
def monitor_system(interval=5):
    with open(log_file, "a") as file:
        while True:
            cpu = psutil.cpu_percent()
            memory = psutil.virtual_memory().percent
            file.write(f"CPU: {cpu}%, Memory: {memory}%\n")
            print(f"CPU: {cpu}%, Memory: {memory}%")
            time.sleep(interval)

monitor_system()

