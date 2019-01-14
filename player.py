import json
import sys
from collections import namedtuple


def check_bad_card(game_state):
    good_card_list = ["10", "J", "K", "Q", "A"]
    is_fold = True
    for player in game_state["players"]:
        if player["name"] == "StackedDeck" and player.get("hole_cards") is \
                not None:
            card1_rank = player.get("hole_cards")[0]["rank"]
            card1_suit = player.get("hole_cards")[0]["suit"]
            card2_rank = player["hole_cards"][1]["rank"]
            card2_suit = player["hole_cards"][1]["suit"]

            if card2_rank == card1_rank:
                is_fold = False

            if card1_rank in good_card_list and card2_rank in good_card_list:
                is_fold = False

        # else:
        #     card1_rank = None
        #     card1_suit = None
        #     card2_rank = None
        #     card2_suit = None
    return is_fold


def place_bet(game_state):
    is_Fold = check_bad_card(game_state)
    if game_state["bet_index"] == 0:
        bet = int(game_state["current_buy_in"])
    else:
        bet = int(game_state["current_buy_in"]) + int(game_state["minimum_raise"])

    if not is_Fold:
       bet = 0


    return bet


class Player:
    VERSION = "0.3.1"

    def betRequest(self, game_state):
        sys.stderr.write("-------------------- STANDARD ERROR "
                         "WORKS ------------------")
        bet = 1000
        try:
            sys.stderr.write("SD new round")
            bet = place_bet(game_state)
        except:
            bet = 1000
        return bet

    def showdown(self, game_state):
        pass


def print_dictionary(dictionary):
    for k, v in dictionary.items():
        print "%s: %s" % (k, v)


def main():
    all_data_json = '{"tournament_id":"550d1d68cd7bd10003000003",' \
                    '"game_id":"550da1cb2d909006e90004b1","round":0,' \
                    '"bet_index":0,"small_blind":10,"current_buy_in":320,' \
                    '"pot":400,"minimum_raise":240,"dealer":1,"orbits":7,' \
                    '"in_action":1,"players":[{"id":0,"name":"akarki",' \
                    '"status":"active","version":"Default random player",' \
                    '"stack":1010,"bet":320},{"id":1,"name":"StackedDeck",' \
                    '"status":"active","version":"0.2",' \
                    '"stack":1590,"bet":80,"hole_cards":[{"rank":"6",' \
                    '"suit":"hearts"},{"rank":"K","suit":"spades"}]},{"id":2,' \
                    '"name":"Chuck","status":"out","version":"Default random ' \
                    'player","stack":0,"bet":0}],"community_cards":[{' \
                    '"rank":"4","suit":"spades"},{"rank":"A",' \
                    '"suit":"hearts"},{"rank":"6","suit":"clubs"}]}'
    all_data_dictionary = json.loads(all_data_json)
    # print_dictionary(all_data_dictionary)
    place_bet(all_data_dictionary)


if __name__ == '__main__':
    main()
