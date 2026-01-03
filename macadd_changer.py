import subprocess
import optparse

def get_options():
    parse = optparse.OptionParser()
    parse.add_option("-i","--interface",dest="interface",help="Used to select interface")
    parse.add_option("-m","--mac",dest="macaddr",help="Used to select New mac address")
    (option,argument) = parse.parse_args()
    if not option.interface:
        parse.error("Interface not specified")
    elif not option.macaddr:
        parse.error("Mac Address not specified")
    return option


def mac_change(interface,macaddr):
    print("Mac Address of "+ interface + " Changing to "+ macaddr)
    subprocess.call(["ip","link","set","dev",interface,"down"])
    subprocess.call(["ip","link","set","dev",interface,"address",macaddr])
    subprocess.call(["ip","link","set",interface,"up"])

option = get_options()
mac_change(option.interface,option.macaddr)
