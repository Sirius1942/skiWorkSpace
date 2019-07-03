import json
import os
class Singleton(object): 
    def __init__(self, cls): 
        self._cls = cls 
    def __call__(self, *args, **kwargs): 
        try: 
            return self._instance 
        except AttributeError: 
            self._instance = self._cls() 
            return self._instance 
@Singleton
class SkiCoreData(object):

    def __init__(self):
        self.classes={}
        self.set_data=self.__get_conf_data()
        self.time_points={}
        self.globalVariable=self.__get_conf_data()['globalVariable']
    
    def get_step_class_instance(self,cls_name):

        if cls_name in self.classes:
            return self.classes[cls_name]
        else:
            return None

    def set_step_class_instance(self,cls_name,cls):
        self.classes[cls_name]=cls
    def get_setting_data(self):
        return self.set_data['routers']
        
    def __get_conf_data(self):
        f= open("./SkiSetting.json")
        conf=json.load(f)
        return conf
    def get_time_point_dics(self):
        return self.time_points
    def get_global_variable(self):
        return self.globalVariable


        

    
         
