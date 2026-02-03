import ipaddress
import json


def load_plan(f_path):
    with open(f_path, "r") as file:
        return json.load(file)


def validate_cidr(cidr_addr):
    try:
        return ipaddress.ip_network(cidr_addr)
    except ValueError:
        return None


def validate_all_subnet(subnets):
    valid_networks = []

    for subnet in subnets:
        net = validate_cidr(subnet["cidr"])
        if not net:
            print(f"Invalid subnet: {subnet['name']} ({subnet['cidr']})")
        else:
            print(f"Valid subnet:{subnet['name']} ({net})")
            valid_networks.append(net)

    return valid_networks


if __name__ == "__main__":
    path = load_plan("ip_plan.json")

    parent = validate_cidr(path["parent_range"])

    if not parent:
        print("Invalid parent range")
    else:
        print("Parent range is valid: ", parent)

    subnets = validate_all_subnet(path["subnets"])
    print(subnets)
