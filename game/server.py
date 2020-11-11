import asyncio
import websockets
from game import *
import demjson
import random


connected = set()
pgn = []
test_pgn = []
games = {"1": [], "0": []}
pool = [1, 0]
game = Game()
player = 1


async def server(websocket, path):
    global games, pool, pgn, test_pgn, player
    connected.add(websocket)
    pool = pool[::-1]
    games[str(pool[-1])].append(websocket)
    test_pgn = pgn
    print(games)

    await websocket.send(str(pool[-1]))

    try:
        async for data in websocket:
            player = not player
            move = demjson.decode(data)["move"]
            print(move)
            test_pgn.append(move)

            if game.analyse(test_pgn) == True:
                pgn = test_pgn
                print(pgn)
                await games[str(int(player))][-1].send("{move: true}")

    finally:
        connected.remove(websocket)


start_server = websockets.serve(server, "localhost", 5555)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
