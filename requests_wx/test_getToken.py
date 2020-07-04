import requests


def test_getToken():
    corpid = "ww2cf4353188d4a3df"
    corpsecret = "81_TmjgePahaJra1gq0HdIZxD9uLkUryeYxMHrvpvVY"
    res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}",
                       verify=False)
    # print(res.json()["access_token"])
    return res.json()["access_token"]


# def test_get():
#     res = requests.get(f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={test_getToken()}&userid=abc",
#                        verify=False)
#     print(res.json()["name"])
#
#
# def test_create():
#     data = {
#         "userid": "zhangsan",
#         "name": "张三",
#         # "alias": "jackzhang",
#         "mobile": "13800000000",
#         "department": [1],
#     }
#     res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={test_getToken()}", json=data,
#                         verify=False)
#     print(res.json()["errcode"])
#     # assert res.json()["errcode"] == 0
#
#
# def test_updates():
#     data = {
#         "userid": "zhangsan",
#         "name": "lisi",
#         "mobile": "18818881888"
#     }
#     res = requests.post(f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={test_getToken()}", json=data,
#                         verify=False)
#     print(res.json())
#
#
# def test_delete():
#     userid = "zhangsan"
#     res = requests.post(
#         f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={test_getToken()}&userid={userid}", verify=False)
#     print(res.json())
