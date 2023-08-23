import requests
from classes.writer import Writer


class UserScrapper:

    def __init__(self, user_id, token, version) -> None:
        self.user_id = user_id
        self.token = token
        self.version = version

    def get_user_id(self):
        response = requests.get('https://api.vk.com/method/friends.get',
                                params={
                                    'access_token': self.token,
                                    'user_ids': self.user_id,
                                    'v': self.version,
                                })

        data = response.json()['response']['items']
        l_data = []
        for i in data:
            i = f'vk.com/id{i}'
            l_data.append(i)
        Writer(self.user_id, l_data).file_writer()
        print(data)