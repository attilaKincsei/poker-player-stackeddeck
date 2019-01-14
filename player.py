import json
import sys
from collections import namedtuple

class Player:
    VERSION = "0.1"

    def betRequest(self, game_state):
        sys.stderr.write("-------------------- STANDARD ERROR "
                         "WORKS ------------------")
        sys.stderr.write(game_state["players"])
        return 310

    def showdown(self, game_state):
        pass

