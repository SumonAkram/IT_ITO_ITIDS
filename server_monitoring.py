import psutil
import platform

def get_system_info():
    # Get system information
    system_info = {
        "Platform": platform.system(),
        "Platform Release": platform.release(),
        "Architecture": platform.machine(),
        "Total Memory": psutil.virtual_memory().total,
        "Available Memory": psutil.virtual_memory().available,
        "CPU Usage": psutil.cpu_percent(interval=1),
        "Disk Usage": psutil.disk_usage("/").percent,
        "Network Stats": psutil.net_io_counters(),
    }
    return system_info

def main():
    system_info = get_system_info()
    print("System Information:")
    for key, value in system_info.items():
        print(f"{key}: {value}")

if __name__ == "__main__":
    main()
