import ipaddress

def find_non_overlapping(existing_ranges, subnet_size=24):                      # give subnet size
    # Convert existing ranges to set of ip_networks
    existing_networks = set([ipaddress.ip_network(r) for r in existing_ranges])
    # Define the IP address space to search
    ip_network = ipaddress.ip_network('192.166.0.0/16')                        # GIve your cidr range as reqirement
    # Divide the IP address space into subnets of size subnet_size
    subnets = list(ip_network.subnets(new_prefix=subnet_size))
    # Check each subnet for overlap with existing ranges
    for subnet in subnets:
        if not any(subnet.overlaps(n) for n in existing_networks):
            return str(subnet)
    # If no non-overlapping subnet is found, raise an error
    raise ValueError('No non-overlapping CIDR range found')


# execute

existing_ranges = ['10.120.0.0/16', '172.16.179.0/24']                              # give existing ips

non_overlapping_range = find_non_overlapping(existing_ranges)

print('new non overlap range', non_overlapping_range)



# def divide_subnets(subnet, num_subnets):
#     """
#     Divide a subnet into a given number of subnets.

#     Args:
#         subnet (str): The subnet to divide, in CIDR notation (e.g. '192.168.0.0/24').
#         num_subnets (int): The number of subnets to divide the subnet into.

#     Returns:
#         A list of strings representing the subnets.
#     """
#     # Parse the input subnet.
#     subnet_obj = ipaddress.ip_network(subnet)

#     # Calculate the size of each subnet.
#     subnets_size = int(subnet_obj.num_addresses / num_subnets)

#     # Create a list of subnets.
#     subnets = [subnet_obj.subnet(subnets_size)]

#     # If there are more subnets than the initial division created, split each subnet recursively.
#     while len(subnets) < num_subnets:
#         subnet_to_split = subnets.pop(0)
#         subnets.extend(subnet_to_split.subnets())

#     # Convert the subnets to strings and return the list.
#     return [str(subnet) for subnet in subnets]

# subnets = divide_subnets('192.168.0.0/24', 4)
# print(subnets)
