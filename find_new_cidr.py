import ipaddress

def find_non_overlapping(existing_ranges, subnet_size=24):
    # Convert existing ranges to set of ip_networks
    existing_networks = set([ipaddress.ip_network(r) for r in existing_ranges])
    # Define the IP address space to search
    ip_network = ipaddress.ip_network('192.166.0.0/16')
    # Divide the IP address space into subnets of size subnet_size
    subnets = list(ip_network.subnets(new_prefix=subnet_size))
    # Check each subnet for overlap with existing ranges
    for subnet in subnets:
        if not any(subnet.overlaps(n) for n in existing_networks):
            return str(subnet)
    # If no non-overlapping subnet is found, raise an error
    raise ValueError('No non-overlapping CIDR range found')


# execute

existing_ranges = ['10.120.0.0/16', '172.16.179.0/24']

non_overlapping_range = find_non_overlapping(existing_ranges)

print('new non overlap range', non_overlapping_range)
