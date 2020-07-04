import re
import requests
import requests_wx.test_getToken as getToken


class TestMailList:
    # 获取部门列表
    def test_get_department(self):
        res = requests.get(
            f"https://qyapi.weixin.qq.com/cgi-bin/department/list?access_token={getToken.test_getToken()}",
            verify=False)
        print(res.json())
        if res.json()["errcode"] == 0:
            assert res.json()["errmsg"] == "ok"

    # 创建部门
    def test_create_department(self):
        data = {
            "name": "研发部门",
            "parentid": "1"
        }
        res = requests.post(
            f"https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token={getToken.test_getToken()}",
            json=data, verify=False)
        print(res.json())
        if res.json()["errcode"] == 0:
            assert res.json()["errmsg"] == "created"
        elif res.json()["errcode"] == 60008:
            msg = re.match("department existed", res.json()["errmsg"]).group()
            assert msg == "department existed"

    # 更新部门
    def test_updates_department(self):
        data = {
            "name": "测试开发小组02",
            "id": "4"
        }
        res = requests.post(
            f"https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token={getToken.test_getToken()}",
            json=data, verify=False)
        print(res.json())
        if res.json()["errcode"] == 0:
            assert res.json()["errmsg"] == "updated"

    # 删除部门
    def test_delete_department(self):
        departmentId = "4"
        res = requests.post(
            f"https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token={getToken.test_getToken()}&id={departmentId}",
            verify=False)
        print(res.json())
        if res.json()["errcode"] == 0:
            assert res.json()["errmsg"] == "deleted"
        elif res.json()["errcode"] == 60123:
            msg = re.match("invalid party id", res.json()["errmsg"]).group()
            assert msg == "invalid party id"
