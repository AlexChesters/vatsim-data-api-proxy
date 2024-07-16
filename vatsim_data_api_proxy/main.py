import json
import os

import boto3
from aws_lambda_powertools import Logger
from aws_lambda_powertools import Tracer

logger = Logger()
tracer = Tracer()

@tracer.capture_lambda_handler
@logger.inject_lambda_context(log_event=True)
def handler(_event, _context):
    s3 = boto3.resource("s3")
    controllers_object = s3.Object(os.environ["BUCKET_NAME"], "controllers.json")

    controllers_object.put(
        Body=json.dumps({}).encode("utf-8")
    )
