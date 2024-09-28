import asyncio
import json
from nats.aio.client import Client as NATS
from pydantic import BaseModel

class NumberEvent(BaseModel):
    number: int
    timestamp: float

async def run():
    nc = NATS()
    await nc.connect("nats://nats:4222")

    async def prime_handler(msg):
        data = json.loads(msg.data.decode())
        event = NumberEvent(**data)
        print(f"Número primo recebido: {event.number}")

    async def palindrome_handler(msg):
        data = json.loads(msg.data.decode())
        event = NumberEvent(**data)
        print(f"Número palíndromo recebido: {event.number}")

    await nc.subscribe("subscribe_prime", cb=prime_handler)
    await nc.subscribe("subscribe_palindrome", cb=palindrome_handler)
    print("Inscrito nos assuntos 'subscribe_prime' e 'subscribe_palindrome'")

    while True:
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(run())
