import unittest
from lib.HTMLTestRunner import HTMLTestRunner
import time
import sys
import logging

def get_test_cases(dirpath):
    test_cases = unittest.TestSuite()
    # 测试用例使用"ski_"开头命名
    suites = unittest.defaultTestLoader.discover(dirpath, 'ski_*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases

if __name__ == '__main__':
    # logging.basicConfig(level=logging.DEBUG,
    #  format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    #  datefmt='%a, %d %b %Y %H:%M:%S',
    #  filename='test1.log',
    #  filemode='w')
    # logger = logging.getLogger("RobotFramework")
    # handler1 = logging.StreamHandler()
    # handler2 = logging.FileHandler(filename="test.log")

    # logger.setLevel(logging.DEBUG)
    # handler1.setLevel(logging.WARNING)
    # handler2.setLevel(logging.DEBUG)

    # formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s %(message)s")
    # handler1.setFormatter(formatter)
    # handler2.setFormatter(formatter)

    # logger.addHandler(handler1)
    # logger.addHandler(handler2)

    cases = get_test_cases('./case')
    now = time.strftime("%Y-%m-%d %H_%M_%S")  # 报告生成时间
    test_reports_address = '../report'      # 测试报告存放位置
    filename = './report/' + now + 'report.html'  # 设置报告文件名
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'Ski自动化测试', description=u'详细测试结果如下:')
    # runner = unittest.TextTestRunner()
    runner.run(cases)
    fp.close()


