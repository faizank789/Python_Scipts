import math

def cidr_from_hosts(hosts, network):
    # Convert network address to a list of octets
    octets = network.split('.')
    # Calculate the number of bits required to represent the number of hosts
    bits = int(math.ceil(math.log(hosts+2, 2)))
    # Calculate the CIDR notation by combining the network address and the number of bits
    cidr = ".".join(octets) + '/' + str(32-bits)
    return cidr

# Example usage
hosts = int(input("Enter number of hosts required: "))
network = input("Enter network address (e.g. 192.168.0.0): ")
cidr = cidr_from_hosts(hosts, network)
print("CIDR notation:", cidr)
