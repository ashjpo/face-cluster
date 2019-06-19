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
    
faceobj_list=generate_faceobj(0,300)
gg_obj=Generate_group(faceobj_list,0.7,0.8,True)
gg_obj.archive_group()
groups=gg_obj.get_group()

print(len(groups))

min_limit_person_num=2
groups=filter_group_person(groups,min_limit_person_num)
print(len(groups))



'''for group in groups:
    print("-------------------------one group-------------------------")
    printer_group_person_analyzeid(group)'''
    
    



#验证
index=0
get_num=300
group_list=[]
for folder in os.listdir(faceid_root_path):
    person_src_folder=faceid_root_path+"\\"+folder
    temp={}
    temp['name']=folder
    temp['file']=[]
    for file in os.listdir(person_src_folder):
        temp['file'].append(file)
        
    group_list.append(temp)
    
def search_in_file_group(group_list,file_name):
    for group in group_list:
        for fname in group['file']:
            if fname==file_name:
                return group['name']
            
    return None

def search_in_group(group_list,name):
    for group in group_list:
        if group['name']==name:
            return group['file']
            
    return None


#测试generate_group_plus
faceobj_list=generate_faceobj(301,100)
gg_obj=Generate_group_plus(groups,faceobj_list,0.7,0.8,False,True)
gg_obj.archive_group()
new_groups,old_group=gg_obj.get_group()
print(len(new_groups),len(old_group))
new_groups=filter_group_person(new_groups,min_limit_person_num)
print(len(new_groups),len(old_group))

for group in old_group:
    print("-------------------------one group-------------------------")
    printer_group_person_analyzeid(group)

