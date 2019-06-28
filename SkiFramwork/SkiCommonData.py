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
    
    def get_step_class_instance(self,cls_name):

        if cls_name in self.classes:
            return self.classes[cls_name]
        else:
            return None
            
    def set_step_class_instance(self,cls_name,cls):
        self.classes[cls_name]=cls

    
         
