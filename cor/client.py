import hashlib
from cor.token import Token
from cor.token import get_random_str


class Client:
    auth_key = ''
    secret_sey = ''

    def __init__(self, auth_key, secret_key):
        self.auth_key = auth_key
        self.secret_sey = secret_key

    def get_token(self, channel_name, user_id, expire_time):
        body_str = self.auth_key + "authkey" + self.auth_key + "channame" + channel_name + "timestamp" + str(
            expire_time) + "userid" + user_id

        # body hash
        body_hl = hashlib.md5()
        body_hl.update(body_str.encode(encoding='utf-8'))
        encode_body = body_hl.hexdigest()

        # secret hash
        secret_hl = hashlib.md5()
        secret_hl.update(self.secret_sey.encode(encoding='utf-8'))
        encode_secret = secret_hl.hexdigest()

        # all hash
        all_hl = hashlib.md5()
        all_hl.update((encode_body + encode_secret).encode(encoding='utf-8'))
        encode_all = all_hl.hexdigest()

        # create token
        token = Token(encode_all, expire_time, 'reserve', 'reserve')
        auth_token = token.get_base64_str() + get_random_str(16)

        return auth_token
