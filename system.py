import psutil
import platform
import GPUtil
import cpuinfo

def cpu_count():
    return psutil.cpu_count()

def gpu_info():
    gpus = GPUtil.getGPUs()
    for gpu in gpus:
        return f"GPU ID: {gpu.id}\nGPU Name: {gpu.name}\nGPU Load: {gpu.load*100}%\nGPU Memory: {gpu.memoryTotal}MB"
    
def cpu_info():
    info = cpuinfo.get_cpu_info()
    return f"CPU Model: {info['brand_raw']}\nCPU Frequency: {info['hz_actual']}\nCPU Architecture: {info['arch']}"

def os():
    return platform.system()