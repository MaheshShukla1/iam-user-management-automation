# IAM User Management Automation Tool

## Overview

The IAM User Management Automation Tool is a Python-based project that automates several AWS IAM tasks using the `boto3` library. This tool simplifies the management of IAM users, policies, and groups, making it easier to handle IAM tasks in bulk.

## Features

- **Create IAM Users in Bulk**: Automate the creation of multiple IAM users from a CSV file.
- **Attach and Detach User Policies**: Attach and detach policies to/from users to manage permissions.
- **Tag Users**: Add tags to users for better organization and management.
- **Create and Manage Groups**: Create IAM groups, add users to groups, and remove users from groups.
- **Delete Policies**: Automate the deletion of policies.
- **List Users and Tags**: List all IAM users and their tags.

## Requirements

- Python 3.x
- `boto3` library
- AWS credentials configured

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/iam-user-management-automation.git
    cd iam-user-management-automation
    ```

2. **Install the required packages:**

    ```bash
    pip install -r requirements.txt
    ```

3. **Configure your AWS credentials:**
   
    Ensure you have your AWS credentials configured. You can use the AWS CLI to configure your credentials:

    ```bash
    aws configure
    ```

## Usage

1. **Prepare the CSV File:**

    Create a CSV file named `users.csv` with the following columns:

    ```csv
    UserName,PolicyArn,TagKey,TagValue,GroupName
    alice,arn:aws:iam::aws:policy/AdministratorAccess,Department,IT,Admins
    bob,arn:aws:iam::aws:policy/ReadOnlyAccess,Department,HR,Viewers
    ```

2. **Run the Main Script:**

    Execute the main script to perform the IAM tasks specified in the CSV file:

    ```bash
    python main.py
    ```

3. **List Users and Tags:**

    To list all IAM users and their tags, ensure that the function call is included in the main script.

## Project Architecture Overview

#### **AWS IAM Service**
The core service used for managing identities and permissions within AWS. The project interacts with IAM to perform tasks such as user management, policy attachment, and group management.

#### **Python Scripts**

* utils.py: Contains functions for AWS IAM operations such as creating users, attaching/detaching policies, tagging users, managing groups, and deleting policies.
* main.py: The entry point for the project that orchestrates the operations by reading input data from a CSV file, executing the necessary IAM actions, and providing logging for visibility.
* CSV File (users.csv)

**Contains user information, including user names, policy ARNs, tags, and group names. This file serves as the input data source for the scripts.
Logging**

**Integrated logging to capture and report the outcomes of each operation. Logs are used to monitor script execution, success messages, and any errors encountered.
Dependencies (requirements.txt)**

#### **Lists the necessary Python packages required to run the scripts, including boto3 for AWS SDK and logging for capturing events.**
#### **Workflow:**

* Load Data: Read user data from users.csv.
* Create Resources: Create IAM users and groups.
* Attach Policies: Apply policies to users.
* Tag Users: Add tags to users.
* Manage Groups: Add or remove users from groups.
* Logging and Monitoring: Log all actions and handle errors.

## Functionality

### 1. **Creating IAM Users**

```python
def create_user(user_name):
```

### 2. **Attaching and Detaching Policies**

```python
def attach_policy(user_name, policy_arn):

def detach_policy(user_name, policy_arn):
```

### 3. **Tagging Users**

```python
def tag_user(user_name, tag_key, tag_value):
```

### 4. **Creating and Managing Groups**

```python
def create_group(group_name):
 
def add_user_to_group(user_name, group_name):
  
def remove_user_from_group(user_name, group_name):
```

### 5. **Deleting Policies**

```python
def delete_policy(policy_arn):
```

### 6. **Listing Users and Tags**

```python
def list_users_and_tags():
```

## Contributing
Contributions are welcome! Please fork this repository and submit a pull request for any features, enhancements, or bug fixes.

## Acknowledgments
The project utilizes the [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) library for AWS interactions.
Thanks to AWS for providing comprehensive documentation and tools for developers.
