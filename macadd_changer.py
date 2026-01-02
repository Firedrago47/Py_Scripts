import subprocess


interface = input("Enter the Interface:")
#subprocess.call("ip a show dev " + interface,shell=True)
#subprocess.call("ip link set dev " + interface + " down",shell)
#subprocess.call("ip link set dev " + interface + " address " + macaddr,shell=True)
#subprocess.call("ip link set " + interface + " up",shell=True)

subprocess.call(["ip","a","show","dev",interface])

macaddr = input("Enter the Address:")

subprocess.call(["ip","link","set","dev",interface,"down"])

subprocess.call(["ip","link","set","dev",interface,"address",macaddr])

subprocess.call(["ip","link","set",interface,"up"])
