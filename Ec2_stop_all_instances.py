import boto3
import json

region = "us-east-2"
client = boto3.client('ec2', region_name=region)

response = client.stop_instances(
# grab the instance id from the running Ec2 instance in the AWS console
    InstanceIds=[
        'i-0b7f11f1e91484142',
    ],
# can be true or false
    Hibernate=False,
# Dryrun is to essentially simulate to see what the code will do.
    DryRun=False,
# Only use force if all other means have failed to stop the instance
    Force=False
)
# for pretty printing ( sort key would be for alphabetical order
print(json.dumps(response, indent=2))