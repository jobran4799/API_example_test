from infra.api_wrapper import APIWrapper


class DrawCard:
    def __init__(self, api_ob):
        self.my_api = api_ob

    def get_Cards_BY_Deck_ID(self, id, num):
        my_api = APIWrapper()
        if num > 0 and num < 7:
            res = my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/{id}/draw/?count={num}')
            return res

    def post_Cards_BY_Deck(self, body, id, num):
        my_api = APIWrapper()
        if num > 0 and num < 7:
            res = my_api.make_post_request(f'https://deckofcardsapi.com/api/deck/{id}/draw/?count={num}', body)
            return res
