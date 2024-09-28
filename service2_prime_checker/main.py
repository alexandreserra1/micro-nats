import asyncio
import json
from nats.aio.client import Client as NATS
from pydantic import BaseModel

# Modelo Pydantic para validação dos dados
class NumberEvent(BaseModel):
    number: int
    timestamp: float

async def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    # verifica apenas até a raiz quadrada de n
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


async def run():
    nc = NATS()
    await nc.connect("nats://nats:4222")

    async def message_handler(msg):
        data = json.loads(msg.data.decode())
        event = NumberEvent(**data)
        asyncio.create_task(process_number(event, nc))

    async def process_number(event, nc):
        if await is_prime(event.number):
            await nc.publish("subscribe_prime", json.dumps(event.dict()).encode())

    await nc.subscribe("numbers", cb=message_handler)

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(run())

