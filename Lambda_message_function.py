import json
import boto3
from datetime import datetime


def lambda_handler(event, context):
    # send a message to sqs queue, taken from AWS documentation

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %p")
    # taken from python datetime documentation
    sqs = boto3.client('sqs')
    sqs.send_message(QueueUrl="https://sqs.us-east-2.amazonaws.com/383618969847/Shipped", MessageBody=current_time)
    # taken from boto3 documentation
    return {
        'statusCode': 200,
        'body': json.dumps(current_time)

    }