import json
import boto3
import os

def lambda_handler(event, context):
	dynamodb = boto3.resource('dynamodb')
	table = dynamodb.Table(os.environ['TABLE_NAME'])
	response = table.scan()
	return {
		"statusCode": 200,
		"body": json.dumps(response['Items']),
	}
