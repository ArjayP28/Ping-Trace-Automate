from concurrent.futures import ThreadPoolExecutor
import subprocess


PING_COMMAND = 'ping'
TRACEROUTE_COMMAND = 'tracert'
MAX_THREADS = 3

def run_command(command):

    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    return result.stdout

def ping_and_traceroute(host):
    ping_output = run_command(f'{PING_COMMAND} {host}')
    traceroute_output = run_command(f'{TRACEROUTE_COMMAND} {host}')

    return host, ping_output, traceroute_output

def ping_and_traceroute_multiple(hosts):
    with ThreadPoolExecutor(max_workers=MAX_THREADS) as executor:
        results = list(executor.map(ping_and_traceroute, hosts))

    return results

hosts = [ 'google.com','192.168.10.1', '180.232.152.97', '161.49.90.241']

results = ping_and_traceroute_multiple(hosts)


for host, ping_output, traceroute_output in results:
    print(f"Host: {host}\nPing Output: {ping_output}\nTraceroute Output: {traceroute_output}\n")

import time
time.sleep(120)
