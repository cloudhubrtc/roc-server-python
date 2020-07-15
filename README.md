## 概述

该项目是 PAAS 层服务器对服务器 SDK。

平台为用户发放的 `AuthKey` 与 `SecretKey` 请使用者妥善保管，不要泄露给其他人，否则将遭受一定的经济损失。

## 文档 

[API文档 - Token生成](http://apidoc.roadofcloud.net/#/token)

## 安装

### 手动安装

将 roc 文件夹中文件拷贝到项目路径即可。

### pip 安装

请稍等片刻

## 使用

### 获取进入房间的 Token

```python
client = Client(auth_key, secret_key)
auth_token = client.get_token(channel_name, user_id, timestamp)
print(auth_token)

```
或者在 `main.py` 中配置好参数后直接运行 `python3 main.py` 也可以查看生成的结果。

**参数说明**

* `auth_key`  认证公钥，平台发放，例如 `WbykCN****8pwd3`
*  `secret_key` 认证秘钥，是平台发放，可以修改，例如 `23423****dfsfs`
* `channel_name` 是要加入的频道名称，例如 `1234567****shao`
* `user_id` 是用户的 `id`，例如 `159****91766-10**26`
* `timestamp` 是过期的时间，如果传 `0` 有效期将会是 24 小时，该时间戳为秒级时间戳，例如 `1594704891`

## 测试

单元测试用例使用 `unittest`

安装完 Composer 后，在项目根目录执行

```bash
cd tests && python -m unittest token_test.py
```


