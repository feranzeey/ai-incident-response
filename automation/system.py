import psutil

print("CPU")

print(psutil.cpu_percent())

print()

print("Memory")

print(psutil.virtual_memory())

print()

print("Disk")

print(psutil.disk_usage("/"))
import psutil

print("===== SYSTEM INFORMATION =====")

print(f"CPU Usage: {psutil.cpu_percent()} %")

print(f"Memory Usage: {psutil.virtual_memory().percent} %")

print(f"Disk Usage: {psutil.disk_usage('/').percent} %")