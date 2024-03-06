from infra.api_wrapper import APIWrapper


class Returning_cards_to_the_deck:
    def __init__(self, api_ob):
        self.my_api = api_ob

    def return_cards_to_deck(self, deck_id, cards=None):
        url = f"https://deckofcardsapi.com/api/deck/{deck_id}/return/"
        params = {"cards": cards} if cards else None
        response = self.my_api.api_get_request_with_params(url, params)
        return response



    def return_cards_to_deck_from_pile(self, deck_id, pile_name, cards=None):
        url = f"https://deckofcardsapi.com/api/deck/{deck_id}/pile/{pile_name}/return/"
        params = {"cards": cards} if cards else None
        response = self.my_api.api_get_request_with_params(url, params)
        return response


