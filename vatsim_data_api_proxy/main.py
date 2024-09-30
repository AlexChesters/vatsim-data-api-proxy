import json
import os
import asyncio

import boto3
from aws_lambda_powertools import Logger, Tracer

from vatsim_data_api_proxy.networking.api_client import fetch_data

logger = Logger()
tracer = Tracer()

@tracer.capture_lambda_handler(capture_response=False) # https://github.com/aws-powertools/powertools-lambda-python/issues/476
@logger.inject_lambda_context(log_event=True)
def handler(_event, _context):
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(os.environ["BUCKET_NAME"])

    data = asyncio.run(fetch_data())

    if not data:
        return

    bucket.put_object(
        Body=json.dumps(data["pilots"]).encode("utf-8"),
        Key="pilots.json",
        CacheControl="max-age=60",
        ContentType="application/json"
    )
    bucket.put_object(
        Body=json.dumps(data["controllers"]).encode("utf-8"),
        Key="controllers.json",
        CacheControl="max-age=60",
        ContentType="application/json"
    )
