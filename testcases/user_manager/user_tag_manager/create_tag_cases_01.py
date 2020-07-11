#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:create_tag_cases.py
# @time:2020/7/5 4:42 下午

import unittest
import requests
import json
from common import config
from common.log_utils import logger
from common.common_api import *

class CreateTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.URL
        self.session = requests.session()
    def tearDown(self) -> None:
        pass

    def test_create_tag(self):
        logger.info('[case01] 正常创建标签')
        respon_obj = get_access_token_api(self.session,
                                            'client_credential',
                                            'wx5189359b0e0ddd89',
                                            '11d4de7719a2276becf27ab573263061')
        token_id = respon_obj.json()['access_token']
        post_param_data = {"tag": {"name": "新建标签0018"}}
        respon_obj1 = create_user_tag_api(self.session,token_id,post_param_data)
        print(respon_obj1.json()['tag']['name'].encode('utf-8').decode('unicode_escape'))
        tag_name = respon_obj1.json()['tag']['name'].encode('utf-8').decode('unicode_escape')
        self.assertEqual(tag_name, "新建标签0018")
        # self.assertEqual(respon_obj1.json()['tag']['name'], "新建标签0008")

    def test_create_tag_name_repeat(self):
        logger.info('[case02] 创建标签名重复')
        respon_obj = get_access_token_api(self.session,
                                            'client_credential',
                                            'wx5189359b0e0ddd89',
                                            '11d4de7719a2276becf27ab573263061')
        token_id = respon_obj.json()['access_token']
        post_param_data = {"tag": {"name": "新建标签0017"}}
        respon_obj1 = create_user_tag_api(self.session,token_id,post_param_data)
        self.assertEqual(respon_obj1.json()['errcode'],45157)

if __name__=="__main__":
    unittest.main()