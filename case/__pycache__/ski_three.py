# coding=utf-8
import time
import unittest
from common.Ski import Ski

class TestSendMessage(unittest.TestCase):

    def setUp(self):
       print("I'm in setUP")
    def tearDown(self):
        print("I'm in setUP")

    @Ski.testStep(todo="sendmessage",
    	          modle="",
    	          data={ "datatype":"free",
    	                 "url":"http://www.baidu.com",
    	                 })
    def test_send(self):
        print("I'm in test_send")
        print(self.ski_step_result.status_code)
        self.assertEqual(200,self.ski_step_result.status_code)
        self.assertTrue(True)