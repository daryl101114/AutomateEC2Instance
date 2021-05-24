# AutomateEC2Instance
Automate creation of a cloud EC2 instance using Python and Boto3

Requirements:

    1. Must have a Keypair in local computer
        - I provided a key pair inside the folder for use.
    2. Change the Keyname in "resources.yaml to the name of your key pair
    3. Running on Python3.9 environment
    4. pip install AWSCLI
    5. configure AWS credential by typing "aws configure" on the terminal
    6. pip install BOTO3

What to expect in the script:

    -The script that I've made would create an ec2 instance using the configuration in resources.yaml.
    -It would also create user1 and user2 in the EC2 instance using the bash script.

What I couldn't do:

    -let user1 and user2 ssh into the ec2 instance.

What I've learned in the assignment:

    Going into the assignment I had knowledge with cloudformation and terraform. However, this assignment required using python and boto3. It was challenging because I had no prior experience coding in python.
    I was not familliar with BOTO3 aswell. I did alot of reading into BOTO3 documentation and found the technology really interesting. transitioning from JAVA to python was not really hard. By doing so, I was able to see the power of Python
    and what it can do. I enjoyed working on this assignment. I learned how to utilize python and boto3 to automate provisioning AWS resources. 
