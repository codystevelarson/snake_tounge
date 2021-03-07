import asyncio
import pathlib
import ssl
import websockets

ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")


async def hello():
    uri = "wss://localhost:8765"
    async with websockets.connect(uri=uri, ssl=ssl_context) as websocket:
        name = input("what is your name?")

        await websocket.send(name)
        print(f'{name}')

        greeting = await websocket.recv()
        print(f'{greeting}')

asyncio.get_event_loop().run_until_complete(hello())
