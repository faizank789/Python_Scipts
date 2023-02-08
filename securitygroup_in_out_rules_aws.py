import boto3

ec2 = boto3.client("ec2")

security_group_id = "your_security_group_id"

# List the inbound rules
inbound_rules = ec2.describe_security_groups(GroupIds=[security_group_id])['SecurityGroups'][0]['IpPermissions']
print("Inbound rules:")
for rule in inbound_rules:
    print(rule)

# List the outbound rules
outbound_rules = ec2.describe_security_groups(GroupIds=[security_group_id])['SecurityGroups'][0]['IpPermissionsEgress']
print("Outbound rules:")
for rule in outbound_rules:
    print(rule)
