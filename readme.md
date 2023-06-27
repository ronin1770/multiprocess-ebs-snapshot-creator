
# AWS Snapshot Creator

This project creates the Snapshots for the 'Available' EBS Volumes for the given region


## Authors

- Farhan Munir 
[@ronin1770](https://github.com/ronin1770)

[FAMRO-LLC](https://famro-llc.com)

[Upwork-Profile](https://www.upwork.com/freelancers/~01a0bd1946b84dc45d?viewMode=1)

[Fiverr-Profile](https://www.fiverr.com/ronin1770?public_mode=true)




## Pre-requisites

To run this project, you will need to add the following environment variables to your .env file

1. AWS Credentials
Depending on your system, you must have either AWS CLI interface installed on your machine or got AWS Credentials file.

On Ubuntu, it is located in:

~/.aws/Credentials

You will need to have AWS Programmatic Access available (that is you must  have AWS API Key and Key Secret)

2. Required Python and its Libraries:
You must have Python 3.6+ installed on your machine. You will need only Boto3 library installed to make this work.

You can install Boto3 library by using the following command:

pip3 install boto3


## Deployment

Copy the process_ebs_volume.py to the folder of your choice. 

Inside the code,  you will need to change the AWS Region of your choice. Currently, it is set as 'us-east-1'.

## How to Execute the Command

You can issue the following command to execute the program:

python3 process_ebs_volumes.py

or 

python process_ebs_volumes.py

## Output

Upon execution you will see the output as follows:

```
Creating the snapshot
Creating the snapshot
Creating the snapshot
Snapshot ID: snap-0c887de9dfad7aeb0 created for Volume_id: vol-0cc91dc2ac17481b7
Snapshot ID: snap-08142f5fc01b8b4b7 created for Volume_id: vol-091398ba178b0f267
Snapshot ID: snap-0b6d646d7b7f454ef created for Volume_id: vol-0ec96e40d0c4f6194
Done

```



