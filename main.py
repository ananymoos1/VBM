import os
import socket
import subprocess
import platform
import cpuinfo
import psutil
import distro
from colorama import init, Fore, Back, Style
import pyfiglet

os.system('cls' if os.name == 'nt' else 'clear')

init()

username = os.getlogin()
hostname = socket.gethostname()

logo = pyfiglet.figlet_format("VBM")
logo = f"{Fore.CYAN}{logo}"
os_name = platform.release()

def neofetch(args):
    system = platform.system()
    cpu = cpuinfo.get_cpu_info()['brand_raw']
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    system_line = f"{Fore.CYAN}System:{Fore.WHITE} {system}\n"
    version_line = f"{Fore.CYAN}Version:{Fore.WHITE} {os_name}\n"
    cpu_line = f"{Fore.CYAN}CPU:{Fore.WHITE} {cpu}\n"
    memory_line = f"{Fore.CYAN}Memory:{Fore.WHITE} {memory.percent}% used ({psutil._common.bytes2human(memory.used)} used / {psutil._common.bytes2human(memory.total)} total)\n"
    disk_line = f"{Fore.CYAN}Disk:{Fore.WHITE} {disk.percent}% used ({psutil._common.bytes2human(disk.used)} used / {psutil._common.bytes2human(disk.total)} total)\n"

    final_output = ""
    final_output += f"{system_line}{version_line}{cpu_line}{memory_line}{disk_line}".center(os.get_terminal_size().columns)
    final_output = f"{Fore.CYAN}{logo}\n{final_output}"

    print(final_output)

def clear(args):
    os.system('cls' if os.name == 'nt' else 'clear')

def exit(args):
    return False
commands = {
    "neofetch": neofetch,
    "clear": clear,
    "exit": exit,
}

def handleCommand(command):
    parts = command.split(" ")
    cmd = parts[0]
    args = parts[1:]

    if cmd in commands:
        commands[cmd](args)
    else:
        print("That command doesnt exist")

while True:
    command = input(f"{username}@{hostname}$ ")
    handleCommand(command)
