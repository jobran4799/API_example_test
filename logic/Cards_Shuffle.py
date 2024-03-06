from infra.api_wrapper import APIWrapper


class CardsShuffle:
    def __init__(self, api_ob):
        self.my_api = api_ob

    def get_CardsShuffle(self, num):
        my_api = APIWrapper()
        if num > 0 and num < 7:
            res = my_api.api_get_request(f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={num}')
            return res

    def post_CardsShuffle(self, body, num):
        my_api = APIWrapper()
        if num > 0 and num < 7:
            res = my_api.make_post_request(f'https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count={num}', body)
            return res
