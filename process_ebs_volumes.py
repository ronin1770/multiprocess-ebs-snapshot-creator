import boto3
from multiprocessing import Pool
import sys

session = boto3.Session()

def get_ebs_volumes(region):
    ret = []
    # Create a Boto3 client for the EC2 service
    ec2_client = boto3.client('ec2', region_name=region)

    # Retrieve the list of EBS volumes
    response = ec2_client.describe_volumes()

    # Extract the volume information from the response
    volumes = response['Volumes']

    # Print the volume details
    for volume in volumes:
        volume_id = volume['VolumeId']
        volume_type = volume['VolumeType']
        volume_state = volume['State']
        #  print(f"Volume ID: {volume_id}")
        #  print(f"Volume Type: {volume_type}")
        #  print(f"Volume State: {volume_state}\n")

        if volume_state == "available":
            ret.append(volume_id)
    return ret

def create_snapshot(count, item):
    hello = item[0]
    volume_id= item[1]

    print(f"Creating the snapshot for volume_id: {volume_id}")
    # Create a Boto3 resource for the EC2 service using the session
    ec2_resource = session.resource('ec2')

    # Create a snapshot of the specified volume
    response = ec2_resource.create_snapshot(
        VolumeId=volume_id,
        Description='Snapshot created using Boto3'
    )   

    # Extract the snapshot ID from the response
    snapshot_id = response.id

    # Print the snapshot ID
    print(f"Snapshot ID: {snapshot_id} created for Volume_id: {volume_id}")


if __name__ == "__main__":
    region = "us-east-1"
    items = []

    volume_ids = get_ebs_volumes(region)

    count = 0

    for volume_id in volume_ids:
        ind = { }
        ind = (count, ["hello", volume_id])
        items.append(ind)
        count += 1

    
    # Create a multiprocessing pool
    
    with Pool() as pool:
        result = pool.starmap(create_snapshot, items)


    print("Done")