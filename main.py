import csv
import logging
from utils import (
    create_user, attach_policy, detach_policy, tag_user, create_group,
    add_user_to_group, remove_user_from_group, delete_policy,
    list_user_and_tags, delete_user
)

logging.basicConfig(level=logging.INFO)

def load_users_from_csv(file_path):
    users = []
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users.append(row)
    return users

def main():
    users = load_users_from_csv('users.csv')
    
    group_names = set()
    for user in users:
        group_names.add(user['GroupName'])

    for group_name in group_names:
        create_group(group_name)

    for user in users:
        user_name = user['UserName']
        policy_arn = user['PolicyArn']
        tag_key = user['TagKey']
        tag_value = user['TagValue']
        group_name = user['GroupName']

        create_user(user_name)
        add_user_to_group(user_name, group_name)
        attach_policy(user_name, policy_arn)
        tag_user(user_name, tag_key, tag_value)

    list_user_and_tags()

    # Example: detach policy, remove user from group, delete user, delete policy
    # detach_policy('alice', 'arn:aws:iam::aws:policy/AdministratorAccess')
    # remove_user_from_group('alice', 'Admins')
    # delete_user('alice')
    # delete_policy('arn:aws:iam::aws:policy/AdministratorAccess')

if __name__ == "__main__":
    main()
