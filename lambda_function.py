def lambda_handler(event, context):
    print("test dilfi ji")
    return {
        'statusCode': 200,
        'body': 'Hello from automated Lambda deployment!'
    }
