
# coding=utf-8
import time
import unittest
from  RequestsLibrary import RequestsLibrary
from  Selenium2Library import Selenium2Library
from importlib import import_module
import inspect

class TestSendMessage(unittest.TestCase):
    def setUp(self):
       print("I'm in test_one setUP")

    def tearDown(self):
        
        print("I'm in test_one tesrDown")

    # def test_send(self):
    #     print("I'm in test_one test_send")
    #     rl=RequestsLibrary()
    #     rl.create_session("baidu","http://www.baidu.com")
    #     res=rl.get_request("baidu","/")
    #     self.assertEqual(res.status_code,200)
    #     self.assertEqual("a","a")
    #     self.assertTrue(True)

    # def test_selenium(self):
    #     sl=Selenium2Library()
    #     sl.open_browser("http://www.baidu.com","chrome")
    #     sl.input_text("id=kw","test_robot")
    #     sl.click_button("id=su")

    def test_rf(self):
        obj=import_module("RequestsLibrary")
        if inspect.isclass(obj):
            print("this is a class")
        if hasattr(obj,"RequestsLibrary"):
            rl=getattr(obj,'RequestsLibrary')
            if inspect.isclass(rl):
                print("rl is a class")
            else:
                print("rl is not a class")
            inst=rl()
            cs=getattr(inst,"create_session")("baidu","http://www.baidu.com")
            res=getattr(inst,"get_request")("baidu","/")
            self.assertEqual(res.status_code,200)
        else:
            print("404")
        
        

if __name__ == '__main__':
    unittest.main()
    