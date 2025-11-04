def lambda_handler(event, context):
    print("Lambda function updated successfully!")
    return {"statusCode": 200, "body": "Hello from Lambda!"}
