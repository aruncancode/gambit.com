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
player = {}


async def server(websocket, path):
    global games, pool, pgn, player, test_pgn
    connected.add(websocket)
    pool = pool[::-1]
    games[str(pool[-1])].append(websocket)
    player[websocket] = str(pool[-1])
    print(games)

    await websocket.send(str(pool[-1]))

    try:
        async for data in websocket:
            colour = player[websocket]
            # print(websocket, colour, not int(colour))
            move = demjson.decode(data)["move"]
            test_pgn.append(move)
            print(test_pgn)
            if game.analyse(test_pgn) == True:
                pgn.append(move)
                await games[str(int(not int(colour)))][-1].send("{\"move\":\"%s\"}" % move)
            elif game.analyse(test_pgn) == False:
                test_pgn.pop(-1)
                await games[str(int(colour))][-1].send("{\"invalid\": %s}" % pgn)
            game.reset()
            # print(test_pgn)


    finally:
        connected.remove(websocket)


start_server = websockets.serve(server, "localhost", 5555)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
