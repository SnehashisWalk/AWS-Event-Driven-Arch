import boto3
import os

def lambda_handler(event, context):
    try:
        # Extract the bucket and file key from the event
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']

        # Initialize an ECS client
        ecs = boto3.client('ecs')

        # Run an ECS task
        response = ecs.run_task(
            cluster='your-ecs-cluster',
            launchType='FARGATE',  # Or EC2, depending on your setup
            taskDefinition='your-task-definition',
            overrides={
                'containerOverrides': [
                    {
                        'name': 'your-container-name',
                        'environment': [
                            {'name': 'BUCKET_NAME', 'value': bucket_name},
                            {'name': 'FILE_KEY', 'value': file_key}
                        ]
                    },
                ]
            }
        )

        print(f"ECS Task Response: {response}")
        return {
            'statusCode': 200,
            'body': 'ECS task started successfully!'
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': f"Error: {e}"
        }
