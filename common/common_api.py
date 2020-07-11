#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:common_api.py
# @time:2020/7/8 8:48 下午

import requests
from common import config

def get_access_token_api(session,grant_type,appid,secret):
    get_params_data = {
        'grant_type': grant_type,
        'appid': appid,
        'secret': secret
    }
    response = session.get(url=config.URL+'/cgi-bin/token',
                            params=get_params_data)
    return response

def create_user_tag_api(session,access_token,tag_json):   # 方式一  推荐用
    get_param_data = {'access_token': access_token}
    post_param_data = tag_json
    response = session.post(url=config.URL + '/cgi-bin/tags/create',
                            params=get_param_data,
                            json=post_param_data)
    return response

# def create_user_tag_api(session,access_token,tag):   # 方式一
#     get_param_data = {'access_token': access_token}
#     post_param_data = {"tag": {"name": tag}}
#     response = session.post(url=config.URL + '/cgi-bin/tags/create',
#                             params=get_param_data,
#                             json=post_param_data)

def delete_user_tag_api(session,access_token,tagid_json):
    get_param_data = {'access_token': access_token}
    post_param_data = tagid_json
    response = session.post(url=config.URL + '/cgi-bin/tags/delete',
                            params=get_param_data,
                            json=post_param_data)
    return response

def update_user_tag_api(session,access_token,tagid_json):
    get_param_data = {'access_token': access_token}
    post_param_data = tagid_json
    response = session.post(url=config.URL + '/cgi-bin/tags/update',
                            params=get_param_data,
                            json=post_param_data)
    return response

def updateremark_user_info_api(session,access_token,tagid_json):
    get_param_data = {'access_token': access_token}
    post_param_data = tagid_json
    response = session.post(url=config.URL + '/cgi-bin/user/info/updateremark',
                            params=get_param_data,
                            json=post_param_data)
    return response
