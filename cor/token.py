import json
import base64
import random
import string


class Token:
    token = ''
    timestamp = 0
    user_account = ''
    role = ''

    def __init__(self, token, timestamp, user_account, role):
        self.token = token
        self.timestamp = timestamp
        self.user_account = user_account
        self.role = role

    def get_base64_str(self):
        data = {
            'token': self.token,
            'timestamp': self.timestamp,
            'useraccount': self.user_account,
            'role': self.role
        }

        json_encode = json.dumps(data, separators=(',', ':')).encode(encoding='utf-8')
        return base64.b64encode(json_encode).decode(encoding='utf-8')


def get_random_str(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
