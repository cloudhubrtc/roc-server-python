import unittest
import sys

sys.path.append("../")


class TestToken(unittest.TestCase):
    def test_get_token(self):
        from cor.client import Client

        auth_key = 'testAuthKey'
        secret_key = 'testSecretKey'
        channel_name = 'testChannelName'
        user_id = 'testUserId'
        timestamp = 1594704891

        client = Client(auth_key, secret_key)
        token = client.get_token(channel_name, user_id, timestamp)

        token = str(token[0:-16])
        self.assertEqual(token,
                         'eyJ0b2tlbiI6IjBiNDkzZTVjN2FjMjM2OThkOWNkYTJhZmMzNGUyMTQyIiwidGltZXN0YW1wIjoxNTk0NzA0ODkxfQ==')


if __name__ == '__main__':
    unittest.main()
