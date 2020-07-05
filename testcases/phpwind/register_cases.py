#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:get_access_token_cases.py
# @time:2020/7/5 4:43 下午

import requests
import unittest
import re
from common.log_utils import logger

class RegisterCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = 'http://47.107.178.45'
        self.session = requests.session()
    def tearDown(self) -> None:
        pass

    def test_register(self):
        logger.info('[case01] 论坛注册用户测试')
        api_url = '/phpwind'
        respon_obj = self.session.get(url=self.hosts+api_url)
        body = respon_obj.content.decode('utf-8')
        token = re.findall('name="csrf_token" value="(.+?)"/>', body)[0]

        api_url = '/phpwind/index.php'
        get_data = {'m': 'u', 'c': 'register', 'a': 'dorun'}
        form_data = {'username': 'cherry_06',
                     'password': '123456',
                     'repassword': '123456',
                     'email': 'cherry_06@163.com',
                     'csrf_token': token}
        headerinfos = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                       'X-Requested-With': 'XMLHttpRequest',
                       'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'}

        respon_obj = self.session.post( url=self.hosts+api_url,
                                        params=get_data,
                                        data=form_data,
                                        headers=headerinfos)
        self.assertEqual(respon_obj.status_code,200)

if __name__=="__main__":
    unittest.main()