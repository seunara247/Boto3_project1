import boto3
s3 = boto3.client('s3')

#create object
bucket_name = 'seunfunmispecialbucket'
s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': "ap-south-1"})
print('bucket is created')

#upload object
file_name = 'boto3.1.png'
s3.upload_file(file_name, bucket_name, file_name)
print('file has been uploaded')

#download object
s3.download_file(bucket_name, file_name, 'download-boto3.1.png')
print('file downloaded')

# Create a temporary link that lasts 1 hour
url = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': file_name},
    ExpiresIn=4200  # 4200 seconds = 2 hour
)

# Show the link
print("Here is your temporary download link:")
print(url)




