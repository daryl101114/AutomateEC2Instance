#Create an EC2 instance using BOTO3
import boto3
import yaml

#Read the YAML file
with open("resources.yaml") as f:
    data = yaml.full_load(f)

#Bash Script to create user1
user_data = f'''
#!/bin/bash
apt-get install -y awscli
useradd {data["EC2Instance"]["Properties"]["users"][0]["login"]}
usermod -aG sudo {data["EC2Instance"]["Properties"]["users"][0]["login"]}
mkdir /home/{data["EC2Instance"]["Properties"]["users"][0]["login"]}/.ssh/


useradd {data["EC2Instance"]["Properties"]["users"][1]["login"]}
usermod -aG sudo {data["EC2Instance"]["Properties"]["users"][1]["login"]}
mkdir /home/{data["EC2Instance"]["Properties"]["users"][1]["login"]}/.ssh/


sudo -i
echo “user1 ALL=(ALL) NOPASSWD:ALL” >> /etc/sudoers
echo “user2 ALL=(ALL) NOPASSWD:ALL” >> /etc/sudoers
exit

apt-get update -y
'''

#Create an EC2 Instance
def create_instance():
    try:
        print("creating the instance")
        ec2_client = boto3.client("ec2")
        instances = ec2_client.run_instances(
            ImageId= data["EC2Instance"]["Properties"]["ImageId"],
            MinCount=1,
            MaxCount=1,
            InstanceType= data["EC2Instance"]["Properties"]["InstanceType"],
            KeyName= data["EC2Instance"]["Properties"]["KeyName"],
            BlockDeviceMappings= data["EC2Instance"]["Properties"]["BlockDeviceMappings"],
            UserData= user_data
    )
    except Exception as e:
        print(e)

create_instance()