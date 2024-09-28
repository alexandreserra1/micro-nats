import asyncio
import json
from nats.aio.client import Client as NATS
from pydantic import BaseModel

class NumberEvent(BaseModel):
    number: int
    timestamp: float

async def is_palindrome(n):
    s = str(n)
    return s == s[::-1]

async def run():
    nc = NATS()
    await nc.connect("nats://nats:4222")

    async def message_handler(msg):
        data = json.loads(msg.data.decode())
        event = NumberEvent(**data)
        print(f"Recebido número: {event.number}")  # Log de depuração
        if await is_palindrome(event.number):
            print(f"Número palíndromo detectado: {event.number}")  # Log de depuração
            await nc.publish("subscribe_palindrome", json.dumps(event.dict()).encode())

    await nc.subscribe("numbers", cb=message_handler)

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(run())
