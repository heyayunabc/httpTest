import json

import requests
from jsonpath import jsonpath
from hamcrest import *
from jsonschema import validate
from requests.auth import HTTPBasicAuth


class TestDemo:
    def test_get(self):
        r = requests.get('http://httpbin.testing-studio.com/get')
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200

    def test_query(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.get("http://httpbin.testing-studio.com/get", params=payload)
        print(r.text)
        assert r.status_code == 200

    def test_post(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("http://httpbin.testing-studio.com/post", data=payload)
        print(r.text)
        assert r.status_code == 200

    def test_heard(self):
        r = requests.get("http://httpbin.testing-studio.com/get", headers={"h": "head demo"})
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert r.status_code == 200
        assert r.json()['headers']['H'] == 'head demo'

    def test_post_json(self):
        payload = {
            "level": 1,
            "name": "seveniruby"
        }
        r = requests.post("http://httpbin.testing-studio.com/post", json=payload)
        print(r.text)
        assert r.status_code == 200
        assert r.json()['json']['level'] == 1

    def test_json(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号'
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号'

    def test_hamcrest(self):
        r = requests.get("https://ceshiren.com/categories.json")
        print(r.text)
        assert r.status_code == 200
        assert_that(r.json()['category_list']['categories'][0]['name'] == '霍格沃兹测试学院公众号')
        print(jsonpath(r.json(), '$..name'))
        assert jsonpath(r.json(), '$..name')[0] == '霍格沃兹测试学院公众号'

    def test_get_login_jsonschema(self):
        url = "https://testerhome.com/api/v3/topics.json"
        data = requests.get(url, params={'limit:': '2'}).json()
        schema = json.load(open("topic_schema.json"))
        validate(data, schema=schema)

    def test_header(self):
        url = 'http://httpbin.testing-studio.com/cookies'
        header = {
            "Cookie": "test=aaaa",
            'User-Agent': 'testaaaa'
        }
        r = requests.get(url=url, headers=header)
        print(r.request.headers)

    def test_cookies(self):
        url = 'http://httpbin.testing-studio.com/cookies'
        header = {
            # "Cookie": "test=aaaa",
            'User-Agent': 'testaaaa'
        }
        cookie_data = {
            "testaaaa": "school"
        }
        r = requests.get(url=url, headers=header, cookies=cookie_data)
        print(r.request.headers)

    def test_auth(self):
        r = requests.get("http://httpbin.testing-studio.com/basic-auth/banana/123",
                         auth=HTTPBasicAuth("banaba", "123"))
        print(r.text)
