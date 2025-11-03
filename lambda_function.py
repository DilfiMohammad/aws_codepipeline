def lambda_handler(event, context):
    print("codebuilt test")
    return {
        'statusCode': 200,
        'body': 'Hello from automated Lambda deployment!'
    }
