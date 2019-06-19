#-*- encoding=utf-8 -*-
import os
import numpy as np
from model.faceobj import faceobj
from main.Generate_group import Generate_group
from tools.grouptool import filter_group_person, printer_group_person_analyzeid
import random
from main.Generate_group_plus import Generate_group_plus

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
    
    
all_number=300
faceobj_list=generate_faceobj(0,all_number)
random.shuffle(faceobj_list)
print("generate faceobj finish")

batch_size=2
batch_num=all_number//batch_size

group_list=[]
for i in range(batch_num):
    print("begin batch>>>",(i+1))
    faceobj_list_batch=faceobj_list[i*batch_size:(i+1)*batch_size]
    
    
    gg_obj=Generate_group_plus(group_list,faceobj_list_batch,0.7,0.8,False,True)
    gg_obj.archive_group()
    new_groups,old_group=gg_obj.get_group()
    print(len(new_groups))
    group_list=old_group+new_groups
    
min_limit_person_num=2
groups=filter_group_person(group_list,min_limit_person_num)
print(len(groups))
for group in groups:
    print("-------------------------one group-------------------------")
    printer_group_person_analyzeid(group)






