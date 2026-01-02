import subprocess


interface = input("Enter the Interface:")
subprocess.call("ip a show dev " + interface,shell=True)
macaddr = input("Enter the Address:")
subprocess.call("ip link set dev " + interface + " down",shell=True)
subprocess.call("ip link set dev " + interface + " address " + macaddr,shell=True)
subprocess.call("ip link set " + interface + " up",shell=True)


