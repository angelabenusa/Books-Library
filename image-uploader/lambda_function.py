import json
import os

import boto3
import requests

AWS_ACCESS_KEY_ID = os.environ.get("BOOKS_AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("BOOKS_AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.environ.get("BOOKS_AWS_REGION")
BUCKET_NAME = os.environ["BUCKET_NAME"]

s3_client = boto3.client(
    service_name="s3",
    region_name=AWS_REGION,
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
)


class Book:
    def __init__(self, id, title, author, url):
        self.id = id
        self.title = title
        self.author = author
        self.url = url


def lambda_handler(event, context):
    for message in event["Records"]:
        process_message(message)
    print("done")


def process_message(message):
    print("message", message)
    payload = message["body"]

    body = json.loads(payload)
    book = Book(
        id=body.get("id"),
        title=body.get("title"),
        author=body.get("author"),
        url=body.get("url"),
    )
    print("book", book)

    try:
        print("downloading image from:", book.url)
        img_data = requests.get(book.url).content
        with open(f"/tmp/{book.id}.jpg", "wb") as handler:
            handler.write(img_data)
        print("image downloaded from:", book.url)

        print("files in /tmp:", os.listdir("/tmp"))
    except Exception as e:
        print(e)
        return e

    upload_file(f"/tmp/{book.id}.jpg", BUCKET_NAME, f"{book.id}.jpg")


def upload_file(file_name, bucket, object_name):
    try:
        print("uploading file to s3")
        s3_client.upload_file(file_name, bucket, object_name)
        print("file uploaded to s3")
    except Exception as e:
        print(e)
        return e
