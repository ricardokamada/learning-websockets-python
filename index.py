import websockets
import asyncio

'''
url-test: https://sync-chasing-ball.glitch.me/
msg: show the current position in the mouse
'''

async def listen():
    url = 'ws://simple-websocket-server-echo.glitch.me/'

    async with websockets.connect(url) as ws:
        while True:
            msg =  await ws.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())