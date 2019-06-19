# coding: utf-8
from main.Generate_group_plus import Generate_group_plus
from tools.grouptool import filter_group_person, printer_group_person_analyzeid



class function_group_faceobj_batch:
    def __init__(self,faceobj_list,batch_size=500):
        self.faceobj_list=faceobj_list
        self.batch_size=batch_size
        self.batch_num=len(self.faceobj_list)//batch_size
        
        self.group_list=[]
        
    def generate_group(self):
        for i in range(self.batch_num):
            print("begin batch>>>",(i+1))
            faceobj_list_batch=self.faceobj_list[i*self.batch_size:(i+1)*self.batch_size]
            
            
            gg_obj=Generate_group_plus(self.group_list,faceobj_list_batch,0.7,0.65,False,True)
            gg_obj.archive_group()
            new_groups,old_group=gg_obj.get_group()
            #print(len(new_groups))
            self.group_list=old_group+new_groups
            
    def filter_min_person_number(self,min_limit_person_num):
        self.group_list=filter_group_person(self.group_list,min_limit_person_num)
        
    def get_group(self):
        return self.group_list
    
    def print_group(self):
        for group in self.group_list:
            print("-------------------------one group-------------------------")
            printer_group_person_analyzeid(group)
    
    
        
        
        
        
        
        
    
    
    
    