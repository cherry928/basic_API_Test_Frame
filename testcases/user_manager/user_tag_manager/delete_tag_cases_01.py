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

class DeleteTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
    def tearDown(self) -> None:
        pass

    def test_delete_tag(self):
        logger.info('[case01] 正常删除标签')
        respon_obj = get_access_token_api(self.session,
                                            'client_credential',
                                            'wx5189359b0e0ddd89',
                                            '11d4de7719a2276becf27ab573263061')
        token_id = respon_obj.json()['access_token']
        post_param_data = {   "tag":{        "id" : 176   } }
        respon_obj1 = delete_user_tag_api(self.session,token_id,post_param_data)
        self.assertEqual(respon_obj1.json()['errcode'],0)

    def test_delete_tag_by_sys(self):
        logger.info('[case02] 删除系统默认标签')
        respon_obj = get_access_token_api(self.session,
                                            'client_credential',
                                            'wx5189359b0e0ddd89',
                                            '11d4de7719a2276becf27ab573263061')
        token_id = respon_obj.json()['access_token']
        post_param_data = {   "tag":{        "id" : 0   } }
        respon_obj1 = delete_user_tag_api(self.session,token_id,post_param_data)
        self.assertEqual(respon_obj1.json()['errcode'],45058)

if __name__=="__main__":
    unittest.main()