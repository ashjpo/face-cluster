#-*- encoding=utf-8 -*-
import os
import numpy as np
import random
from model.faceobj import faceobj
from function.function_group_faceobj_batch import function_group_faceobj_batch
from sqlalchemy.sql.expression import all_
import time


faceid_root_path="D:\\dev\\lfw_faceid_unlimit"

def generate_faceobj(begin,get_num):
    main_list=[]
    index=0
    for folder in os.listdir(faceid_root_path):
        person_src_folder=faceid_root_path+"\\"+folder
        
        for file in os.listdir(person_src_folder):
            temp={}
            temp["person"]=folder
            temp["path"]=file
            temp["faceid"]=np.load(person_src_folder+"\\"+file)
            if index>=begin:
                main_list.append(temp)
    
            index+=1
            
            
            if index>begin+get_num:
                break
            
        if index>begin+get_num:
                break
    random.shuffle(main_list)
    #组成faceobj
    faceobj_list=[]
    for temp in main_list:
        faceid=temp["faceid"]
        analyze_id=temp["path"]
        fobj=faceobj(analyze_id,faceid)
        faceobj_list.append(fobj)
    return faceobj_list


if __name__ == '__main__':
    all_number=800
    faceobj_list=generate_faceobj(0,all_number)
    random.shuffle(faceobj_list)
    print("generate faceobj finish")
    
    batch_size=600
    
    begin_time=time.time()
    fgfb_obj=function_group_faceobj_batch(faceobj_list,batch_size)
    fgfb_obj.generate_group()
    all_group=fgfb_obj.get_group()
    stop_time=time.time()
    print("use time>>>",str(stop_time-begin_time))
    print(len(all_group))
    #min_limit_person_num=2
    #fgfb_obj.filter_min_person_number(min_limit_person_num)
    #filter_group=fgfb_obj.get_group()
    #print(len(filter_group))
    fgfb_obj.print_group()
    
    
    
    #验证
    '''index=0
    in_error=0
    person_name_list=[]
    in_error_list=[]
    for g in all_group:
        group_name=None
        if_error=True
        for f in g.get_group_faceobj():
            analyze_id=f.get_analyze_id()
            tmp=analyze_id.split("_")[-1]
            name=analyze_id.replace(tmp,"")
            if group_name is None:
                group_name=name
                person_name_list.append(group_name)
            else:
                if group_name!=name:
                    if_error=False
            index+=1     
        if if_error==False:
            in_error=in_error+1
            
    out_error=0
    del_list=[]
    for name in person_name_list:
        if name not in del_list:
            if person_name_list.count(name)>1:
                #print(name,person_name_list.count(name))
                del_list.append(name)
                out_error=out_error+(person_name_list.count(name)-1)
        
    print("in_error",in_error,len(person_name_list),str(round((len(person_name_list)-in_error)/len(person_name_list),2)*100)+"%")
    print("out_error",out_error,len(person_name_list),str(round((len(person_name_list)-out_error)/len(person_name_list),2)*100)+"%")
    
    
    
    min_limit_person_num=2
    fgfb_obj.filter_min_person_number(min_limit_person_num)
    filter_group=fgfb_obj.get_group()
    all_group=filter_group
    #验证
    index=0
    in_error=0
    person_name_list=[]
    in_error_list=[]
    for g in all_group:
        group_name=None
        if_error=True
        for f in g.get_group_faceobj():
            analyze_id=f.get_analyze_id()
            tmp=analyze_id.split("_")[-1]
            name=analyze_id.replace(tmp,"")
            if group_name is None:
                group_name=name
                person_name_list.append(group_name)
            else:
                if group_name!=name:
                    if_error=False
            index+=1     
        if if_error==False:
            in_error=in_error+1
            
    out_error=0
    del_list=[]
    for name in person_name_list:
        if name not in del_list:
            if person_name_list.count(name)>1:
                #print(name,person_name_list.count(name))
                del_list.append(name)
                out_error=out_error+(person_name_list.count(name)-1)
        
        
    print("filter min 2 people")
    print("in_error",in_error,len(person_name_list),str(round((len(person_name_list)-in_error)/len(person_name_list),2)*100)+"%")
    print("out_error",out_error,len(person_name_list),str(round((len(person_name_list)-out_error)/len(person_name_list),2)*100)+"%")'''
    
                    
    
            
            
    
    
