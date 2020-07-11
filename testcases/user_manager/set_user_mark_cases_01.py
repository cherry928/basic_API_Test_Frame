#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:set_user_mark_cases_01.py
# @time:2020/7/5 4:44 下午

import unittest
from common.log_utils import logger
from common.common_api import *

class SetUserMarkCases(unittest.TestCase):
    def setUp(self) -> None:
        self.session = requests.session()
    def tearDown(self) -> None:
        pass

    def test_set_user_mark(self):
        logger.info('[case01] 正常设置备注名')
        respon_obj = get_access_token_api(self.session,
                                            'client_credential',
                                            'wx5189359b0e0ddd89',
                                            '11d4de7719a2276becf27ab573263061')
        token_id = respon_obj.json()['access_token']
        post_param_data = {"openid":"oBoBIs3ORP0LQvAerd_FI7i4L4fk","remark":"cherrylalala"}
        respon_obj1 = updateremark_user_info_api(self.session,token_id,post_param_data)
        self.assertEqual(respon_obj1.json()['errcode'],0)

    def test_et_user_mark_openid_error(self):
        logger.info('[case02] 设置备注名appid错误')
        respon_obj = get_access_token_api(self.session,
                                          'client_credential',
                                          'wx5189359b0e0ddd89',
                                          '11d4de7719a2276becf27ab573263061')
        token_id = respon_obj.json()['access_token']
        post_param_data = {"openid": "oBoBIs3ORP0LQvAerd_FI7i4L4f", "remark": "cherrylalala"}
        respon_obj1 = updateremark_user_info_api(self.session, token_id, post_param_data)
        self.assertEqual(respon_obj1.json()['errcode'], 40003)

if __name__=="__main__":
    unittest.main()