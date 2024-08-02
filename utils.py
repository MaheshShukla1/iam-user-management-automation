import logging
import boto3

logging.basicConfig(level=logging.INFO)

iam_client = boto3.client('iam')

def create_user(user_name):
    try:
        response = iam_client.create_user(UserName=user_name)
        logging.info(f'User {user_name} created successfully.')
        return response
    except Exception as e:
        logging.error(f'Error creating user {user_name}: {e}')

def attach_policy(user_name, policy_arn):
    try:
        response = iam_client.attach_user_policy(UserName=user_name, PolicyArn=policy_arn)
        logging.info(f'Policy {policy_arn} attached to user {user_name} successfully.')
        return response
    except Exception as e:
        logging.error(f'Error attaching policy {policy_arn} to user {user_name}: {e}')

def detach_policy(user_name, policy_arn):
    try:
        response = iam_client.detach_user_policy(UserName=user_name, PolicyArn=policy_arn)
        logging.info(f'Policy {policy_arn} detached from user {user_name} successfully.')
        return response
    except Exception as e:
        logging.error(f'Error detaching policy {policy_arn} from user {user_name}: {e}')

def tag_user(user_name, tag_key, tag_value):
    try:
        response = iam_client.tag_user(UserName=user_name, Tags=[{'Key': tag_key, 'Value': tag_value}])
        logging.info(f'Tag {tag_key}: {tag_value} added to user {user_name} successfully.')
        return response
    except Exception as e:
        logging.error(f'Error tagging user {user_name}: {e}')

def create_group(group_name):
    try:
        response = iam_client.create_group(GroupName=group_name)
        logging.info(f'Group {group_name} created successfully.')
        return response
    except Exception as e:
        logging.error(f'Error creating group {group_name}: {e}')

def add_user_to_group(user_name, group_name):
    try:
        response = iam_client.add_user_to_group(UserName=user_name, GroupName=group_name)
        logging.info(f'User {user_name} added to group {group_name} successfully.')
        return response
    except Exception as e:
        logging.error(f'Error adding user {user_name} to group {group_name}: {e}')

def remove_user_from_group(user_name, group_name):
    try:
        response = iam_client.remove_user_from_group(UserName=user_name, GroupName=group_name)
        logging.info(f'User {user_name} removed from group {group_name} successfully.')
        return response
    except Exception as e:
        logging.error(f'Error removing user {user_name} from group {group_name}: {e}')

def delete_policy(policy_arn):
    try:
        response = iam_client.delete_policy(PolicyArn=policy_arn)
        logging.info(f'Policy {policy_arn} deleted successfully.')
        return response
    except Exception as e:
        logging.error(f'Error deleting policy {policy_arn}: {e}')

def list_users_and_tags():
    try:
        users = iam_client.list_users()['Users']
        for user in users:
            user_name = user['UserName']
            tags = iam_client.list_user_tags(UserName=user_name)['Tags']
            logging.info(f'User: {user_name}, Tags: {tags}')    
    except Exception as e:
        logging.error(f'Error listing users and tags: {e}')

def delete_user(user_name):
    try:
        policies = iam_client.list_attached_user_policies(UserName=user_name)['AttachedPolicies']
        for policy in policies:
            iam_client.detach_user_policy(UserName=user_name, PolicyArn=policy['PolicyArn'])
            logging.info(f'Detached policy {policy["PolicyArn"]} from user {user_name}')
        response = iam_client.delete_user(UserName=user_name)
        logging.info(f'User {user_name} deleted successfully.')
        return response
    except Exception as e:
        logging.error(f'Error deleting user {user_name}: {e}')
        return None
