# -*- coding:utf-8 -*-
import json
import os
import importlib.util
import importlib
import inspect
from importlib import import_module
from SkiFramwork.log import logger
from SkiFramwork.SkiCommonData import SkiCoreData
import time
import datetime

class RunObject():
    def run(self,kw_path,*arg,**kws):
            try:
                modules=self.__getModules(kw_path)
            
            except Exception:
                logger.error("error,does not find  modules")
                return None
            
            fun_list=kw_path[len(modules)+1:].split('.')
            
            return self.__getObject(modules,fun_list)(*arg,**kws)

    def __getObject(self,modules,fun_list):
        
        obj= import_module(modules)
        child_obj=getattr(obj,fun_list[0])
        temp_cls_name=fun_list[0]
        for key in fun_list[1:]:
            if inspect.isclass(child_obj):
                # print("this is a class")
                temp_cls=SkiCoreData().get_step_class_instance(temp_cls_name)
                if temp_cls is None:
                    child_obj=child_obj()
                    SkiCoreData().set_step_class_instance(temp_cls_name,child_obj)
                else:
                    child_obj=temp_cls
            child_obj=getattr(child_obj,key)
            temp_cls_name=key
        return child_obj

    def __getModules(self,kw_path):
        # print(kw_path)
        if kw_path.find('.')==-1:
            if self.__ismodule(kw_path):
                return modules
            else:
                raise Exception("all error,does not find  modules")
        kw=kw_path.split('.')[-1]
        modules=kw_path[0:kw_path.rindex(kw)-1]  #rindex 为了应对报名重名 从后向前计算
        flag=self.__ismodule(modules)
        # print(flag)
        if flag:
            # print(modules)
            return modules
        else:
            # print(modules)
            return self.__getModules(modules)

    def __ismodule(self,module_name):

        # print("++++++ is module ++++")
        # print(module_name)
        # print("====== is module =====")
        module_spec=None
        try:
            module_spec = importlib.util.find_spec(module_name)
        except Exception as error:
            # print(error)
            print("error",error)
            
            return False
        if module_spec is None:
            # print("Module :{} not found".format(module_name))
            print("false")
            return False

        else:
            # print("Module:{} can be imported!".format(module_name))
            print("true")
            return True

class SkiTime():
    def __init__(self):
        self.time_points=SkiCoreData().get_time_point_dics()
        
    def get_format_time_now(self):
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    def culate_elapsed_time(self,time_mark_ame):
        tnow=datetime.datetime.now()
        # logger.debug(type(tnow))
        if time_mark_ame in self.time_points:
            k=tnow-self.time_points[time_mark_ame]
            return k.total_seconds()
        else:
            return None
    # 设置时间检查点
    def mark_time_point(self,name):
        self.time_points[name]=datetime.datetime.now()
        



    