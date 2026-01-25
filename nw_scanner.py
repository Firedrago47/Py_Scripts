import scapy.all as sp


def scan(ip):
    # sp.arping(ip)
    sp.sr(sp.IP(dst=ip) / sp.ICMP(), timeout=2)


scan("192.168.1.1/24")
