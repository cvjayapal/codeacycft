import boto3

def check_stack_resources(stack_name, expected_resources):
    """Check CloudFormation stack for expected resources."""
    client = boto3.client('cloudformation')
    response = client.describe_stack_resources(StackName=stack_name)
    stack_resources = [res['ResourceType'] for res in response['StackResources']]

    coverage = {}
    for resource in expected_resources:
        coverage[resource] = resource in stack_resources

    return coverage

if __name__ == "__main__":
    stack_name = "my-stack"
    expected_resources = [
        "AWS::EC2::VPC",
        "AWS::S3::Bucket",
        "AWS::IAM::Role"
    ]

    coverage_report = check_stack_resources(stack_name, expected_resources)
    print("Coverage Report:", coverage_report)
