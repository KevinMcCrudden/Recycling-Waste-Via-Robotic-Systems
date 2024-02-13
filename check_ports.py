import os
import subprocess

def check_and_kill_port(port):
    try:
        # Find process using the port
        cmd = f"lsof -ti:{port}"
        result = subprocess.check_output(cmd, shell=True).decode().strip()
        if result:
            print(f"Port {port} is in use by process ID(s): {result}")
            # Kill the process using the port
            os.system(f"kill -9 {result}")
            print(f"Killed process(es) {result} using port {port}.")
        else:
            print(f"Port {port} is available.")
    except subprocess.CalledProcessError:
        print(f"No process is using port {port}.")

ports_to_check = [5006, 8000]  # Add any other ports you want to check

for port in ports_to_check:
    check_and_kill_port(port)
