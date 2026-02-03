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


def validate_subnets_of_parent(parent, subnets):
    for subnet in subnets:
        net = subnet.subnet_of(parent)
        if not net:
            print(f"Invalid,{subnet} not a subnet of {parent} Outside the range")
            return False
        else:
            print(f"Valid,{subnet} is inside parent range")
    return True


def validate_overlab(subnets):
    print("\n Checking for overlapping...\n")
    for i in range(len(subnets)):
        for j in range(i + 1, len(subnets)):
            net1 = subnets[i]
            net2 = subnets[j]

            if net1.overlaps(net2):
                print(f"Invalid, detected overlap between {net1} and {net2}")
                return False
            else:
                print(f"No overlaps detected between {net1} and {net2}")
    return True


if __name__ == "__main__":
    path = load_plan("ip_plan.json")

    parent = validate_cidr(path["parent_range"])

    if not parent:
        print("Invalid parent range")
        exit(1)

    subnets = validate_all_subnet(path["subnets"])

    print("\n Checking subnets are inside the parent range...\n")

    if not validate_subnets_of_parent(parent, subnets):
        print("Invalid,Check the Ip plan")
        exit(1)

    if not validate_overlab(subnets):
        print("Invalid, Overlapping detected")
        exit(1)

    print("\n All subnets are inside the parent range\n")
