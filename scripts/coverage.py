import boto3

def check_resource(resource_type):
    """Check if a specific resource type exists in the deployed stack."""
    client = boto3.client('cloudformation')
    response = client.describe_stack_resources(StackName='my-stack')
    resources = [r['ResourceType'] for r in response['StackResources']]
    return resource_type in resources

def main():
    resources_to_check = ['AWS::EC2::VPC', 'AWS::S3::Bucket']
    coverage = {resource: check_resource(resource) for resource in resources_to_check}
    print("Coverage Results:", coverage)

if __name__ == '__main__':
    main()
