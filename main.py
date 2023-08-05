#!/usr/bin/python

import socket
from termcolor import colored
import concurrent.futures

def get_host_info(target):
    try:
        ip_address = socket.gethostbyname(target)
        return ip_address
    except socket.gaierror:
        return "Unknown IP"

def get_service_name(port):
    try:
        service_name = socket.getservbyport(port)
        return service_name
    except:
        return "Unknown"

def portscanner(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex((target, port))
    sock.close()

    if result == 0:
        service_name = get_service_name(port)
        print(colored(f"Port {port} is open - Service: {service_name}", 'green'))

def main():
    target = input("[*] Enter the Domain Name or IP Address to Scan: ")
    ip_address = get_host_info(target)

    print(f"Scanning ports for {target} ({ip_address})\n")

    # Increase the number of workers based on your system's capabilities
    max_workers = 50

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        port_range = range(1, 1000)
        executor.map(lambda port: portscanner(ip_address, port), port_range)

if __name__ == "__main__":
    main()
