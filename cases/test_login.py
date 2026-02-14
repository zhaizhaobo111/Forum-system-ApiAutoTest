#登录接口设计测试用例

import pytest
from jsonschema import validate
from utils.request_util import host, Request

@pytest.mark.order(1)
class TestLogin:
    url=host+"user/login"
    schema={
    "type": "object",
    "required":["code","message","data"],
    "additionalProperties": False,
    "properties": {
        "code": {
            "type": "integer"
        },
        "message": {
            "type": "string"
        },
        "data": {
            "type": "null"
        }
    },
}

    # 异常登录
    @pytest.mark.parametrize("login", [
        # 错误的账号密码
        {
            "username": "user",
            "password": "123123",
            "message":"参数校验失败"
        },
        # 错误的账号
        {
            "username": "username10086",
            "password": "123456",
            "message": "参数校验失败"
        },
        # 错误的密码
        {
            "username": "username",
            "password": "123123",
            "message": "用户名或密码错误"
        },
        # 不存在的账号
        {
            "username": "niuniuniu",
            "password": "123123",
            "message": "参数校验失败"
        },
        # 空的账号和面码
        {
            "username": " ",
            "password": " ",
            "message": "参数校验失败"
        },
    ])

    def test_login_fail(self, login):
        data = {
            "username": login["username"],
            "password": login["password"]
        }
        r = Request().post(url=self.url, data=data)
        validate(instance=r.json(), schema=self.schema)
        assert r.json()["message"]==login["message"]

    # 正常登录
    @pytest.mark.parametrize("login", [
        {
            "username": "username",
            "password": "123456",
        },
        {
            "username": "username02",
            "password": "123456",
        }
    ])
    def test_login_success(self,login):
        data={
            "username": login["username"],
            "password": login["password"]
            }
        r = Request().post(url=self.url,data=data)
        validate(instance=r.json(),schema=self.schema)

        assert  r.json()["code"]==0
        # assert  re.match('S{100,}',r.json()['data'])