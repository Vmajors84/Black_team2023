import json
import boto3
# this is taken directly from the boto3 resource page
client = boto3.client('sqs')
response = client.create_queue(
    QueueName='Shipped',
    tags={
        'project': 'project_10',
        'source': 'boto3'
    }
)

# pretty printing in json formatting
print(json.dumps(response, indent=2))