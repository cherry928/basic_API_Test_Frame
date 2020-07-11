#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:get_access_token_cases.py
# @time:2020/7/5 4:43 下午

import requests
import unittest
from common import config
from common.log_utils import logger

class GetAccessTokenCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.URL
        self.session = requests.session()
    def tearDown(self) -> None:
        pass

    def test_get_access_token(self):
        logger.info('[case01] 正常获取access_token值测试')
        api_url = '/cgi-bin/token'
        get_params_data = {
            'grant_type': 'client_credential',
            'appid': 'wx5189359b0e0ddd89',
            'secret': '11d4de7719a2276becf27ab573263061'
        }
        respon_obj = self.session.get(url=self.hosts+api_url,
                                  params=get_params_data)
        self.assertEqual(respon_obj.content.decode('utf-8').__contains__('access_token'), True)   # 断言一
        # self.assertEqual(respon_obj.json()['expires_in'], 7200)  # 断言二
        # print(respon_obj.json())

    def test_appid_error(self):
        # self._testMethodDoc = '[case02] appid错误时的测试'
        logger.info('case02 appid错误时的测试')
        api_url = '/cgi-bin/token'
        get_params_data = {
            'grant_type': 'client_credential',
            'appid': 'x5189359b0e0ddd89',
            'secret': '11d4de7719a2276becf27ab573263061'
        }
        respon_obj = self.session.get(url=self.hosts + api_url,
                                  params=get_params_data)
        self.assertEqual(respon_obj.json()['errcode'],40013)

if __name__=="__main__":
    unittest.main()