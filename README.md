# IAM User Management Automation Tool

## Overview

The IAM User Management Automation Tool is a Python-based solution designed to streamline AWS IAM tasks using the powerful `boto3` library. This tool automates the management of IAM users, policies, and groups, making it an ideal choice for administrators who need to efficiently manage IAM tasks at scale.

## Key Features

- **Bulk IAM User Creation**: Automate the creation of multiple IAM users from a CSV file, reducing manual efforts.
- **Policy Management**: Attach and detach policies to/from IAM users for flexible permission management.
- **User Tagging**: Organize and manage users effectively by adding tags.
- **Group Management**: Create IAM groups, manage group memberships, and automate group-related tasks.
- **Policy Deletion**: Automate the cleanup of outdated or unnecessary policies.
- **User and Tag Listing**: Easily list all IAM users and their associated tags for quick reference.

## Requirements

- Python 3.x
- `boto3` library
- AWS credentials properly configured

## Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/iam-user-management-automation.git
cd iam-user-management-automation
```
**Install Dependencies**

Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

**Configure AWS Credentials**

Ensure your AWS credentials are configured correctly. You can use the AWS CLI to set them up:

```bash
aws configure
```
## Usage

### Step 1: Prepare the CSV File

Create a CSV file named `users.csv` with the following structure:
```bash
UserName,PolicyArn,TagKey,TagValue,GroupName
alice,arn:aws:iam::aws:policy/AdministratorAccess,Department,IT,Admins
bob,arn:aws:iam::aws:policy/ReadOnlyAccess,Department,HR,Viewers
```

 ### Step 2: Run the Main Script

Execute the main script to perform the IAM tasks specified in the CSV file:

```bash
python main.py
```

### Step 3: List Users and Tags

To list all IAM users and their tags, include the function call in the main script.

## Project Architecture Overview

### **AWS IAM Service**

The core service utilized for managing identities and permissions within AWS. The project interacts directly with IAM to perform tasks such as user creation, policy management, and group administration.

### **Python Scripts**

- **`utils.py`**: Contains all the core functions for AWS IAM operations, including creating users, managing policies, tagging users, and handling groups.
- **`main.py`**: The primary script that orchestrates the IAM tasks by reading data from the CSV file, executing operations, and logging the results.

### **CSV File (`users.csv`)**

The input data source that contains user information, policy ARNs, tags, and group names.

### **Logging**

Integrated logging captures and reports the outcome of each operation. Logs are essential for monitoring script execution, tracking success messages, and identifying any errors encountered.

### **Dependencies (`requirements.txt`)**

Lists the necessary Python packages required to run the scripts, including `boto3` for AWS SDK interactions and `logging` for event capturing.

## Workflow Overview

1. **Load Data**: Read user data from the `users.csv` file.
2. **Resource Creation**: Automate the creation of IAM users and groups.
3. **Policy Management**: Attach and detach policies to/from users as specified.
4. **User Tagging**: Add tags to users for enhanced organization.
5. **Group Management**: Handle group memberships by adding or removing users from groups.
6. **Logging and Monitoring**: Log all actions for transparency and troubleshooting.

## Detailed Functionality

### 1. **Creating IAM Users**

```python
def create_user(user_name):
    # Code to create IAM user
```

### 2. **Attaching and Detaching Policies**

```python
def attach_policy(user_name, policy_arn):
    # Code to attach policy

def detach_policy(user_name, policy_arn):
    # Code to detach policy
```

### 3. Tagging Users

```python
def tag_user(user_name, tag_key, tag_value):
    # Code to tag IAM user
```

### 4. Creating and Managing Groups

```python
def create_group(group_name):
    # Code to create group
 
def add_user_to_group(user_name, group_name):
    # Code to add user to group
  
def remove_user_from_group(user_name, group_name):
    # Code to remove user from group
```

### 5. Deleting Policies

```python
def delete_policy(policy_arn):
    # Code to delete policy
```

### 6. Listing Users and Tags

```python
def list_users_and_tags():
    # Code to list IAM users and their tags
```

## Contributing

We welcome contributions! Please fork this repository, make your changes, and submit a pull request. Whether you’re adding new features, improving existing functionality, or fixing bugs, your help is appreciated.

