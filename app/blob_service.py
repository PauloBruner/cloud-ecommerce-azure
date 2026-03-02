from azure.storage.blob import BlobServiceClient
from app.config import *

def upload_image(file):
    blob_service = BlobServiceClient.from_connection_string(BLOB_CONNECTION_STRING)
    blob_client = blob_service.get_blob_client(container=CONTAINER_NAME, blob=file.name)

    blob_client.upload_blob(file, overwrite=True)

    return blob_client.url