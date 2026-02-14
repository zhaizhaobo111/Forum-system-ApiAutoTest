import pytest

from jsonschema import validate
from utils.request_util import host, Request
from utils.yaml_util import read_yaml


class TestPost:
    url=host+"article/create"
    schema={
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "code": {
            "type": "integer"
        },
        "message": {
            "type": "string"
        },
        "data": {
            "type": ["string","null"]
        }
    },
    "required": [
        "code",
        "message",
        "data"
    ]
}
    def test_post_nologin(self):
        params = {"boardId": "null", "title": " ", "content": " p"}
        r = Request().post(url=self.url, params=params)
        assert r.status_code == 200
    # 发表帖子
    @pytest.mark.parametrize("post",[
        # 发表帖子成功
        {
            "boardId": 1,
            "title": "test",
            "content": "test"
        },
        # # 板块id为空
        {
            "boardId": "",
            "title": "test",
            "content": "test"
        },
        # {
        #     "boardId": 1,
        #     "title": "test",
        #     "content": "test"
        # },
        ])
    def test_post(self,post):
        cookie_str = read_yaml("data.yml", "cookie")
        headers={
            "content-type":"application/json",
            "cookie":cookie_str,
        }
        json={
            "boardId": post["boardId"],
            "title": post["title"],
            "content": post["content"]
        }
        r=Request().post(url=self.url,json=json,headers=headers)
        # 验证Jasonshema
        validate(instance=r.json(),schema=self.schema)