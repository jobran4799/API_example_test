# This is a sample Python script.
import unittest

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import requests

from infra.api_wrapper import APIWrapper
from logic.Cards_Shuffle import CardsShuffle
from logic.Draw_Card import DrawCard
from logic.Returning_cards_to_the_deck import Returning_cards_to_the_deck
from logic.house_endpoints import HouseEndPoints


class MainTester(unittest.TestCase):
    def setUp(self):
        self.my_api = APIWrapper()


    def test_get_card_shuffle_request(self):
        c_shuffle = CardsShuffle(self.my_api)
        my_c_api=c_shuffle.get_CardsShuffle(1)
        json_response = my_c_api.json()
        success_param = json_response.get('success')
        self.assertTrue(my_c_api.ok, "noy ok")
        self.assertTrue(success_param,"did not success")


    def test_post_card_shuffle_request(self):
        c_draw = DrawCard(self.my_api)
        data = {
            "success": True,
            "deck_id": "kn5q12zrbod9",
            "remaining": 50,
            "shuffled": True
        }
        my_c_api = c_draw.post_Cards_BY_Deck(data, 'kxozasf3edqu',2)
        json_response = my_c_api.json()
        success_param = json_response.get('success')
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertTrue(success_param, "did not success")

    def test_get_Cards_BY_Deck_ID(self):
        c_draw = DrawCard(self.my_api)
        my_c_api = c_draw.get_Cards_BY_Deck_ID('kxozasf3edqu', 2)
        json_response = my_c_api.json()
        cards_param = json_response.get('cards')
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertTrue(cards_param, "did not success")
        for cards in cards_param:
            print(cards)

    def test_post_Cards_BY_Deck_request(self):
        c_draw = DrawCard(self.my_api)
        updated_cards = [
            {
                "code": "6H",
                "image": "https://deckofcardsapi.com/static/img/6H.png",
                "images": {
                    "svg": "https://deckofcardsapi.com/static/img/6H.svg",
                    "png": "https://deckofcardsapi.com/static/img/6H.png"
                },
                "value": "6",
                "suit": "HEARTS"
            },
            {
                "code": "5S",
                "image": "https://deckofcardsapi.com/static/img/5S.png",
                "images": {
                    "svg": "https://deckofcardsapi.com/static/img/5S.svg",
                    "png": "https://deckofcardsapi.com/static/img/5S.png"
                },
                "value": "5",
                "suit": "SPADES"
            }
        ]
        my_c_api = c_draw.post_Cards_BY_Deck(updated_cards, 'kxozasf3edqu', 2)
        json_response = my_c_api.json()
        success_param = json_response.get('success')
        self.assertTrue(my_c_api.ok, "not ok")
        self.assertTrue(success_param, "did not success")
        for card in json_response.get('cards'):
            print(card)

    def test_return_cards_to_deck(self):
        cards_to_the_deck = Returning_cards_to_the_deck(self.my_api)
        deck_id = "kxozasf3edqu"
        pile_name = "piles"
        response = cards_to_the_deck.return_cards_to_deck(deck_id, pile_name)
        json_response = response.json()
        success_param = json_response.get('success')
        self.assertTrue(response.ok, "not ok")
        self.assertTrue(success_param, "did not success")
        print(response)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_api = APIWrapper()
    res = my_api.api_get_request('https://wizard-world-api.herokuapp.com/Houses')
    print(res.status_code)
    data = res.json()
    print(data["name"])
    my_api = APIWrapper()
    result = my_api.api_get_request('https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
