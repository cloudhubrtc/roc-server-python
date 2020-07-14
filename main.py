# main.py

from cor.token import Token
from cor.client import Client

auth_key = 'Wbyk*****Q8pwd3'
secret_key = '234****3sdfsfs'
channel_name = '1234****9qiushao'
user_id = '15947****766-101726'
timestamp = 1594704891

# Demo Only
# 请使用自己的 AuthKey 和 SecretKey
# AuthKey: WbykCN****8pwd3
# SecretKey: 23423****dfsfs
# ChannelName: 1234567****shao
# UserId: 159****91766-10**26
# ExpireTime: 1594704891
# AuthToken: eyJ0b2tlbiI6ImZlNTdkNzUzMDI1ZDIwMzdlNGZjMDdhMmRkYTBhZmMxIiwidGltZXN0YW1wIjoxNTk0NzA0ODkxLCJ1c2VyYWNjb3VudCI6InJlc2VydmUiLCJyb2xlIjoicmVzZXJ2ZSJ9lADPXbcGTTuoSBvn

client = Client(auth_key, secret_key)
auth_token = client.get_token(channel_name, user_id, timestamp)
print(auth_token)
