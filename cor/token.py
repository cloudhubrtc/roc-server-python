import json
import base64
import random
import string


class Token:
    token = ''
    timestamp = 0

    def __init__(self, token, timestamp):
        self.token = token
        self.timestamp = timestamp

    def get_base64_str(self):
        data = {
            'token': self.token,
            'timestamp': self.timestamp
        }

        json_encode = json.dumps(data, separators=(',', ':')).encode(encoding='utf-8')
        return base64.b64encode(json_encode).decode(encoding='utf-8')


def get_random_str(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
