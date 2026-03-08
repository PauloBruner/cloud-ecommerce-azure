import os
from azure.storage.blob import BlobServiceClient

BLOB_CONNECTION_STRING = os.getenv("BLOB_CONNECTION_STRING")
CONTAINER_NAME = os.getenv("CONTAINER_NAME")

def upload_image(file):
    blob_service = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
    container_client = blob_service.get_container_client(CONTAINER_NAME)

    blob_client = container_client.get_blob_client(file.name)
    blob_client.upload_blob(file, overwrite=True)

    return blob_client.url