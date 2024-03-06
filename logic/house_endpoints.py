from infra.api_wrapper import APIWrapper


class HouseEndPoints:
    def __init__(self, api_ob):
        self.my_api = api_ob


    def house_api(self):
        my_api = APIWrapper()
        res = my_api.api_get_request(f'https://wizard-world-api.herokuapp.com/Houses')
        return res

    def house_api_by_id(self, id):
        my_api = APIWrapper()
        res = my_api.api_get_request(f'https://wizard-world-api.herokuapp.com/Houses/{id}')
        return res.json()