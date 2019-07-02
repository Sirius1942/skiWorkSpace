# -*- coding:utf-8 -*-
import json
import os
import importlib.util
import importlib
import inspect
from importlib import import_module
from SkiFramwork.SkiCommonData import SkiCoreData
from SkiFramwork.log import logger
from SkiFramwork.api import RunObject

class Ski():
    class case():
        def __init__(self):
            # print('__case init__')
            scd=SkiCoreData()
        def __call__(self,func):
                def __deco(self,*arg,**kws):
                    # 执行执行用例前需要执行的方法

                    result=func(self,*arg,**kws)
                    # 执行用例执行后需要执行的方法
                    return result
                return __deco

    class step():
        def __init__(self,keyword,*arg,**kws):
            scd=SkiCoreData()
            conf=scd.get_setting_data()
            full_modules=conf[keyword]
            self.result=self.__run(full_modules,*arg,**kws)
            logger.info(self.result)
            
        def __run(self,keyword,*arg,**kws):
            ro=RunObject().run(keyword,*arg,**kws)
            return ro
        
