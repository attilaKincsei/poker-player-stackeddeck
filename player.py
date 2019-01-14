import json
import sys
from collections import namedtuple

class Player:
    VERSION = "0.1"

    def betRequest(self, game_state):
        x = json.loads(game_state, object_hook=lambda d: namedtuple('X', d.keys())(*d.values()))
        sys.stderr.write(x["minimum_raise"])
        return 240

    def showdown(self, game_state):
        pass

