import boto3
import os
from datetime import datetime


SOURCE_DIR = "/path/to/your/local/directory"  # Folder you want to backup
S3_BUCKET = "your-unique-s3-bucket-name"     # Your S3 bucket name
S3_PREFIX = "backups/"                        # Optional folder in S3


def backup_to_s3(local_folder, bucket_name):
    s3 = boto3.client('s3')  # Connect to S3
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    s3_folder = f"{S3_PREFIX}{timestamp}/"

    files_uploaded = 0

    # Go through all files in the folder
    for root, dirs, files in os.walk(local_folder):
        for file in files:
            local_path = os.path.join(root, file)  # Full file path
            relative_path = os.path.relpath(local_path, local_folder)  # Relative path
            s3_key = os.path.join(s3_folder, relative_path).replace("\\", "/")

            try:
                s3.upload_file(local_path, bucket_name, s3_key)
                print(f"✅ Uploaded: {relative_path}")
                files_uploaded += 1
            except Exception as e:
                print(f"❌ Failed: {relative_path} -> {e}")

    # Summary
    print("\n--- Backup Summary ---")
    print(f"Total files uploaded: {files_uploaded}")
    print(f"Backup location: s3://{bucket_name}/{s3_folder}")
    print("----------------------")

if __name__ == "__main__":
    print("Starting Backup...")
    backup_to_s3(SOURCE_DIR, S3_BUCKET)
    print("Backup Completed!")
