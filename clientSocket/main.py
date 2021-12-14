# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import pickle
import socket
import time

import speedtest
import requests

import psutil

HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 65431  # Port to listen on (non-privileged ports are > 1023)


def get_cpu_usage_pct():
    """
    Obtains the system's average CPU load as measured over a period of 500 milliseconds.
    :returns: System CPU load as a percentage.
    :rtype: float
    """
    return psutil.cpu_percent(interval=0.5, percpu=True)


def get_ram_usage():
    list_obj = [get_size(psutil.virtual_memory().total), psutil.virtual_memory().percent,
                get_size(psutil.virtual_memory().free)]
    return list_obj


"""
    t p f
    fer__> current
    disk_usage__> tpf
    Obtains the absolute number of RAM bytes currently in use by the system.
    :returns: System RAM usage in bytes.
    :rtype: int
    """


def disk_usage():
    return [get_size(psutil.disk_usage('/').total), psutil.disk_usage('/').percent,
            get_size(psutil.disk_usage('/').free)]


def cpu_ferq():
    return psutil.cpu_freq().current


def get_net_io():
    """
bytes_sent – number of bytes sent
bytes_recv – number of bytes received
packets_sent – number of packets sent
packets_recv – number of packets received
errin – total number of errors while receiving
errout – total number of errors while sending
dropin – total number of incoming packets which were dropped
dropout – total number of outgoing packets which were dropped
    :return:
    """
    return [get_size(psutil.net_io_counters().bytes_recv), get_size(psutil.net_io_counters().bytes_sent)]


def get_IP():
    return requests.get('https://api.ipify.org').text


def calc_ul_dl():
    speedtester = speedtest.Speedtest()
    speedtester.get_best_server()
    ul = get_size(speedtester.upload())
    dl = get_size(speedtester.download())
    return [ul, dl]


"""
complete it to the code
"""


def get_size(bytes, suffix="B"):
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    data = {
        'cpu_usage_pct': get_cpu_usage_pct(),
        'ram_usage_total': get_ram_usage()[0],
        'ram_usage_pct': get_ram_usage()[1],
        'ram_usage_free': get_ram_usage()[2],
        'cpu_ferq_current': cpu_ferq(),
        'disk_usage_total': disk_usage()[0],
        'disk_usage_usage': disk_usage()[1],
        'disk_usage_free': disk_usage()[2],
        'net_io_bytes_sent': get_net_io()[0],
        'net_io_bytes_receive': get_net_io()[1],
        'IP': get_IP(),
        'ul': calc_ul_dl()[0],
        'dl': calc_ul_dl()[1],

    }
    print(json.dumps(data).encode('utf-8'))
    s.send(json.dumps(data).encode('utf-8'))
