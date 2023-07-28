import json
import awswrangler as wr

def lambda_handler(event, context):
    # TODO implement
    print(wr.__version__)
    print(wr.__description__)
    print(wr.__message__)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
