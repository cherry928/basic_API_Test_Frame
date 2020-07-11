#!usr/bin/env python
# encoding: utf-8
# @author: cherry
# @file:start_runner.py
# @time:2020/7/5 5:05 下午

import os,time
import unittest
import HTMLTestRunner
from common import config
from common import HTMLTestReportCN

def get_all_cases_suite():
    discover = unittest.defaultTestLoader.discover(start_dir='./testcases',
                                                   pattern='*_cases_01.py',
                                                   top_level_dir='./testcases')
    all_suite = unittest.TestSuite()
    all_suite.addTest(discover)
    return all_suite

# 方式一
# now_time = time.strftime('%Y_%m_%d_%H_%M_%S')
# html_report = os.path.join(config.REPORT_PATH, 'result_%s.html'% now_time)
# file = open(html_report, 'wb')
# html_runner = HTMLTestRunner.HTMLTestRunner(stream=file,
#                                             title='API测试',
#                                             description='测试描述')
# html_runner.run(get_all_cases_suite())

# 方式二
report_dir = HTMLTestReportCN.ReportDirectory(config.REPORT_PATH)
report_dir.create_dir("API_TEST")
dir_path = HTMLTestReportCN.GlobalMsg.get_value('dir_path')
report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
fp = open(report_path, 'wb')
runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                         title="API_TEST",
                                         description='测试描述',
                                         tester='cherry')
runner.run(get_all_cases_suite())
fp.close()