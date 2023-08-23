import json


class Writer:

    def __init__(self, user_id, user_friends) -> None:
        self.user_id = user_id
        self.user_friends = user_friends

    def file_writer(self):
        with open(f'user_{self.user_id}', 'w') as file:
            json.dump(self.user_friends, file, indent=4)
