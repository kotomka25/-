import platform
import sys
import os
import getpass
import json
from datetime import datetime

def detect_os():
    system = platform.system()
    if system == "Linux":
        return "Linux"
    elif system == "Darwin":
        return "macOS"
    elif system == "Windows":
        return "Windows"
    else:
        return f"Unknown ({system})"

def collect_os_info():
    return {
        "system": platform.system(),
        "friendly_name": detect_os(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "is_64bit": sys.maxsize > 2 ** 32,
        "hostname": platform.node(),
        "platform_tag": sys.platform
    }

def collect_python_info():
    return {
        "version": platform.python_version(),
        "implementation": platform.python_implementation(),
        "compiler": platform.python_compiler(),
        "executable": sys.executable,
        "encoding_default": sys.getdefaultencoding()
    }

def collect_process_info():
    return {
        "pid": os.getpid(),
        "user": getpass.getuser(),
        "cwd": os.getcwd()
    }

def collect_system_info():
    return {
        "collected_at": datetime.now().isoformat(timespec="seconds"),
        "os": collect_os_info(),
        "python": collect_python_info(),
        "process": collect_process_info()
    }

def save_to_json(data, filename="os_info.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    return filename

def main():
    data = collect_system_info()
    print(f"Текущая ОС: {data['os']['friendly_name']}")
    save_to_json(data)

if __name__ == "__main__":
    main()