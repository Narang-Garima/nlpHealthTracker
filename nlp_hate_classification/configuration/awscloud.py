import os

class AWSS3Sync:
    def sync_file_to_s3(self, s3_bucket_url, filepath, filename):
        """
        Upload a local file to an S3 bucket.
        """
        command = f"aws s3 cp {filepath}/{filename} s3://{s3_bucket_url}/"
        os.system(command)

    def sync_file_from_s3(self, s3_bucket_url, filename, destination):
        """
        Download a file from an S3 bucket to local destination.
        """
        command = f"aws s3 cp s3://{s3_bucket_url}/{filename} {destination}/{filename}"
        os.system(command)
    def sync_directory_to_s3(self, s3_bucket_url, directory):
        """
        Upload a local directory to an S3 bucket.
        """
        command = f"aws s3 cp {directory} s3://{s3_bucket_url}/ --recursive"
        os.system(command)