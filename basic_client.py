import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri=uri) as websocket:
        name = input("What is u name? ")

        await websocket.send(name)
        greeting = await websocket.recv()
        print(f'{greeting}')

asyncio.get_event_loop().run_until_complete(hello())
