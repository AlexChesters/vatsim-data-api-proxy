import aiohttp
from aws_lambda_powertools import Logger, Tracer
from aws_lambda_powertools.tracing import aiohttp_trace_config

logger = Logger()
tracer = Tracer()

@tracer.capture_method
async def fetch_data() -> dict:
    async with aiohttp.ClientSession(trace_configs=[aiohttp_trace_config()]) as session:
        async with session.get("https://data.vatsim.net/v3/vatsim-data.json") as resp:
            return await resp.json()
