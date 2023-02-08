import boto3

ec2 = boto3.client("ec2")

private_ips = ["private_ip_1", "private_ip_2", "private_ip_3"]

# Find the instance IDs using the private IP addresses
instance_ids = []
for private_ip in private_ips:
    response = ec2.describe_instances(Filters=[{'Name': 'private-ip-address', 'Values': [private_ip]}])
    instance_id = response['Reservations'][0]['Instances'][0]['InstanceId']
    instance_ids.append(instance_id)

# Prompt for confirmation before stopping and terminating the instances
confirmation = input(f"Are you sure you want to stop and terminate the following instances?\n{instance_ids}\nEnter 'yes' to confirm: ")
if confirmation != "yes":
    print("Operation cancelled")
    exit()

# Stop the instances
ec2.stop_instances(InstanceIds=instance_ids)
print(f"Instances {instance_ids} are stopping")

# Wait for the instances to stop
waiter = ec2.get_waiter("instance_stopped")
waiter.wait(InstanceIds=instance_ids)

# Terminate the instances
ec2.terminate_instances(InstanceIds=instance_ids)
print(f"Instances {instance_ids} are terminating")
