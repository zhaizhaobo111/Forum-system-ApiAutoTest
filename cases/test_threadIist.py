import pytest
from jsonschema import validate
from utils.request_util import host, Request
from utils.yaml_util import read_yaml

@pytest.mark.order(2)
class TestThreadList:
    url=host+"article/getAllByBoardId"
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
                    "type": ["array","null"],
                    "items": {
                        "type": "object",
                        "properties": {
                            "id": {
                                "type": "integer"
                            },
                            "boardId": {
                                "type": "integer"
                            },
                            "userId": {
                                "type": "integer"
                            },
                            "title": {
                                "type": "string"
                            },
                            "visitCount": {
                                "type": "integer"
                            },
                            "replyCount": {
                                "type": "integer"
                            },
                            "likeCount": {
                                "type": "integer"
                            },
                            "state": {
                                "type": "integer"
                            },
                            "createTime": {
                                "type": "string"
                            },
                            "updateTime": {
                                "type": "string"
                            },
                            "user": {
                                "type": "object",
                                "properties": {
                                    "id": {
                                        "type": "integer"
                                    },
                                    "nickname": {
                                        "type": "string"
                                    },
                                    "avatarUrl": {
                                        "type": ["string", "null"]
                                    }
                                },
                                "additionalProperties": False,
                                "required": [
                                    "id",
                                    "nickname"
                                ]
                            }
                        },
                        "required": [
                            "id",
                            "boardId",
                            "userId",
                            "title",
                            "visitCount",
                            "replyCount",
                            "likeCount",
                            "state",
                            "createTime",
                            "updateTime",
                            "user"
                        ]
                    }
                }
            },
            "required": [
                "code",
                "message",
                "data"
            ]
        }


    @pytest.mark.parametrize("thread_list", [
        # 正常场景：存在的板块ID
        {
            "boardId": 3,
            "expect_code": 0,
            "expect_message": "成功"
        },
        # 异常场景：不存在的板块ID
        {
            "boardId": 999,
            "expect_code": 0,
            "expect_message": "成功"
        },
        # 异常场景：空的板块ID
        {
            "boardId": "",
            "expect_code": 1000,
            "expect_message": "参数校验失败"
        }
    ])
    def test_thread_list(self,thread_list):
        cookie_str = read_yaml("data.yml", "cookie")
        headers = {
            "Cookie": cookie_str,
            "Accept": "application/json",
        }

        json = {
            "boardId": thread_list["boardId"]
        }

        # 发送GET请求
        r = Request().get(url=self.url, json=json,headers=headers)

        res = r.json()
        # assert res["code"] == thread_list["expect_code"]
        # assert res["message"] == thread_list["expect_message"]
        # 校验响应
        validate(instance=r.json(), schema=self.schema)