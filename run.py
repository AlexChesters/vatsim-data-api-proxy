from dataclasses import dataclass

from vatsim_data_api_proxy.main import handler

@dataclass
class LambdaContext:
    function_name: str = "vatsim-data-api-proxy"
    memory_limit_in_mb: int = 128
    invoked_function_arn: str = "arn:aws:lambda:eu-west-1:809313241:function:vatsim-data-api-proxy"
    aws_request_id: str = "52fdfc07-2182-154f-163f-5f0f9a621d72"

handler({}, LambdaContext())
