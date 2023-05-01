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

# Get username and hostname
username = os.getlogin()
hostname = socket.gethostname()

# Generate ASCII logo
logo = pyfiglet.figlet_format("VBM")
logo = f"{Fore.CYAN}{logo}" # Change logo color to cyan
os_name = platform.release()

def process_command(command):
    if command == "neofetch":
        # Get system information
        system = platform.system()
        cpu = cpuinfo.get_cpu_info()['brand_raw']
        memory = psutil.virtual_memory()
        disk = psutil.disk_usage('/')

        # Format output with colors
        system_line = f"{Fore.CYAN}System:{Fore.WHITE} {system}\n"
        version_line = f"{Fore.CYAN}Version:{Fore.WHITE} {os_name}\n"
        cpu_line = f"{Fore.CYAN}CPU:{Fore.WHITE} {cpu}\n"
        memory_line = f"{Fore.CYAN}Memory:{Fore.WHITE} {memory.percent}% used ({psutil._common.bytes2human(memory.used)} used / {psutil._common.bytes2human(memory.total)} total)\n"
        disk_line = f"{Fore.CYAN}Disk:{Fore.WHITE} {disk.percent}% used ({psutil._common.bytes2human(disk.used)} used / {psutil._common.bytes2human(disk.total)} total)\n"

        # Concatenate logo and neofetch output
        final_output = ""
        final_output += f"{system_line}{version_line}{cpu_line}{memory_line}{disk_line}".center(os.get_terminal_size().columns)
        final_output = f"{Fore.CYAN}{logo}\n{final_output}"

        # Print output with colors
        print(final_output)
    elif command == "clear":
        os.system('cls' if os.name == 'nt' else 'clear')  # clear the screen
    elif command == "execute WintypePRO-executor.roblox":
        print("Successfully opened WintypePRO Executor")
    elif command == "exit":
        return False  # exit the loop and end the program
    elif command == "help":
        print("Available commands:\n"
              "neofetch - Show system information\n"
              "clear - Clear the screen\n"
              "exit - Exit the program\n"
              "help - Show this help message")
    else:
        print(f"Command '{command}' not recognized.")
    return True


# Main loop
while True:
    # Prompt for input
    command = input(f"{username}@{hostname}$ ")

    # Process the command
    if not process_command(command):
        break  # exit the loop and end the program
