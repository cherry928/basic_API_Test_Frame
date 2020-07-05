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

class GetCreateTagCases(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.URL
        self.session = requests.session()
    def tearDown(self) -> None:
        pass

    def test_create_tag(self):
        logger.info('[case01] 正常创建标签')
        get_token_url = '/cgi-bin/token'
        get_params_data = {
            'grant_type': 'client_credential',
            'appid': 'wx5189359b0e0ddd89',
            'secret': '11d4de7719a2276becf27ab573263061'
        }
        respon_obj = self.session.get(url=self.hosts+get_token_url,
                                  params=get_params_data)
        token_id = respon_obj.json()['access_token']
        create_tag_url = '/cgi-bin/tags/create'
        get_param_data = {'access_token': token_id}
        post_param_data = {"tag": {"name": "新建标签0013"}}
        respon_obj1 = self.session.post(url=self.hosts + create_tag_url,
                                   params=get_param_data,
                                   json=post_param_data)
        print(respon_obj1.json()['tag']['name'].encode('utf-8').decode('unicode_escape'))
        tag_name = respon_obj1.json()['tag']['name'].encode('utf-8').decode('unicode_escape')
        self.assertEqual(tag_name, "新建标签0013")
        # self.assertEqual(respon_obj1.json()['tag']['name'], "新建标签0008")

if __name__=="__main__":
    unittest.main()