import boto3

ec2 = boto3.client('ec2')
# List of private IP addresses # example: ['10.0.0.1', '10.0.0.2', '10.0.0.3']
private_ips = ['10.0.0.1', '10.0.0.2', '10.0.0.3']

# Get a list of all EC2 instances with the specified private IP addresses
instances = ec2.describe_instances(Filters=[
    {
        'Name': 'private-ip-address',
        'Values': private_ips
    }
])['Reservations']

# Loop through each instance
for reservation in instances:
    instance = reservation['Instances'][0]
    
    # Extract the required information
    iam_role = instance.get('IamInstanceProfile', {}).get('Arn', 'N/A')
    availability_zone = instance['Placement']['AvailabilityZone']
    instance_id = instance['InstanceId']
    instance_name = next((item['Value'] for item in instance['Tags'] if item['Key'] == 'Name'), 'N/A')
    instance_state = instance['State']['Name']
    instance_type = instance['InstanceType']
    public_ip = instance.get('PublicIpAddress', 'N/A')
    public_dns_name = instance.get('PublicDnsName', 'N/A')
    private_ip = instance.get('PrivateIpAddress', 'N/A')
    private_dns_name = instance.get('PrivateDnsName', 'N/A')
    storage = instance.get('BlockDeviceMappings', 'N/A')
    vpc = instance['VpcId']
    vpc_name = next((item['Value'] for item in instance['Tags'] if item['Key'] == 'VPC_Name'), 'N/A')
    subnet_id = instance['SubnetId']
    security_groups = instance['SecurityGroups']
    platform = instance.get('Platform', 'N/A')
    route_table = instance.get('RouteTableId', 'N/A')
    tags = instance.get('Tags', 'N/A')
    
    # Print the information
    print("Private IP:", private_ip)
    print("Public IP:", public_ip)
    print("Instance Name:", instance_name)
    print("Instance State:", instance_state)
    print("Instance Type:", instance_type)
    print("Public DNS Name:", public_dns_name)
    print("Private DNS Name:", private_dns_name)
    print("IAM Role:", iam_role)
    print("Availability Zone:", availability_zone)
    print("Instance ID:", instance_id)
    print("Storage:", storage)
    print("VPC Name:", vpc_name)
    print("VPC ID:", vpc)
    print("Subnet ID:", subnet_id)
    print("Security Groups:", security_groups)
    print("Platform:", platform)
    print("Route Table:", route_table)
    print("Tags:", tags)
    print("\n")
