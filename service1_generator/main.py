import random
import time
import json
import asyncio
from nats.aio.client import Client as NATS
from pydantic import BaseModel

class NumberEvent(BaseModel):
    number: int
    timestamp: float

async def run():
    nc = NATS()
    await nc.connect("nats://nats:4222")

    while True:
        number = random.randint(100, 999)  # Números de 3 dígitos
        event = NumberEvent(number=number, timestamp=time.time())
        await nc.publish("numbers", json.dumps(event.dict()).encode())
        await asyncio.sleep(0.01)  # ajuste a taxa conforme necessário


if __name__ == "__main__":
    asyncio.run(run())
