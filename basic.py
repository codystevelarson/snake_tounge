import asyncio
import websockets


async def ello_mate(websocket, path):
    name = await websocket.recv()
    print(f'{name}')

    greeting = f'ello mate, {name}'

    await websocket.send(greeting)
    print(f'{greeting}')


start_server = websockets.serve(ello_mate, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
