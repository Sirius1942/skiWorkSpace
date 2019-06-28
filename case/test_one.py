# coding=utf-8
import time
import unittest

class TestSendMessage(unittest.TestCase):
    def setUp(self):
       print("I'm in test_one setUP")

    def tearDown(self):
        
        print("I'm in test_one setUP")

    def test_send(self):
        print("I'm in test_one test_send")
        self.assertEqual("a","a")
        self.assertTrue(True)
