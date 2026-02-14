import pytest
from jsonschema import validate
from utils.request_util import host, Request
from utils.yaml_util import read_yaml


class TestReplyList:
    url = host + "reply/getReplies"

    schema = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "code": {"type": "integer"},
            "message": {"type": "string"},
            "data": {
                "type": ["array","null"],
                "items": {
                    "type": "object",
                    "additionalProperties": False,
                    "properties": {
                        "id": {"type": "integer"},
                        "articleId": {"type": "integer"},
                        "postUserId": {"type": "integer"},
                        "content": {"type": "string"},
                        "likeCount": {"type": "integer"},
                        "state": {"type": "integer"},
                        "createTime": {"type": "string"},
                        "updateTime": {"type": "string"},
                        "user": {
                            "type": "object",
                            "additionalProperties": False,
                            "properties": {
                                "id": {"type": "integer"},
                                "nickname": {"type": "string"},
                                "avatarUrl": {"type": ["string", "null"]}
                            },
                            "required": ["id", "nickname", "avatarUrl"]
                        }
                    },
                    "required": [
                        "id", "articleId", "postUserId", "content",
                        "likeCount", "state", "createTime", "updateTime", "user"
                    ]
                }
            }
        },
        "required": ["code", "message", "data"]
    }

    # 测试用例：不同articleId获取回复列表
    @pytest.mark.parametrize("reply_list", [
        # 正常场景：存在的帖子ID（如Postman里的articleId=1）
        {
            "articleId": 1,
            "expect_code": 0,
            "expect_message": "成功"
        },
        # 异常场景：不存在的帖子ID
        {
            "articleId": 999,
            "expect_code": 0,
            "expect_message": "成功"
        },
        # 异常场景：空的帖子ID
        {
            "articleId": "",
            "expect_code": 1000,
            "expect_message": "参数校验失败"
        }
    ])
    def test_get_reply_list(self, reply_list):
        cookie_str = read_yaml("data.yml", "cookie")
        headers = {
            "Cookie": cookie_str,
            "Accept": "application/json"
        }

        params = {"articleId": reply_list["articleId"]}
        r = Request().get(url=self.url, params=params, headers=headers)

        res = r.json()

        # assert res["code"] == reply_list["expect_code"]
        # assert res["message"] == reply_list["expect_message"]

        validate(instance=res, schema=self.schema)