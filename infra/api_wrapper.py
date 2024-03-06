import requests


class APIWrapper:
    def __init__(self):
        self.response = None
        url = None
        self.myrequest = requests

    def api_get_request(self, url):
        self.response = self.myrequest.get(url)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def api_get_request_with_params(self, url, params):
        self.response = self.myrequest.get(url, params=params)
        return self.response

    import requests

    def make_post_request(self, url, data=None):
        self.response = self.myrequest.post(url, json=data)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def make_put_request(self, url, data=None):
        self.response = self.myrequest.put(url, json=data)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def make_patch_request(self, url, data=None):
        self.response = self.myrequest.patch(url, json=data)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    def make_delete_request(self, url):
        self.response = self.myrequest.delete(url)
        if self.response.ok:
            return self.response
        else:
            return self.response.status_code

    