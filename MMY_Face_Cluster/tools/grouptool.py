# coding: utf-8
import numpy as np
def filter_group_person(group_list,min_peroson_num=2):
    """
        筛选有一定人数的group
    """
    return_group_list=[]
    for group in group_list:
        faceobj_list=group.get_group_faceobj()
        if len(faceobj_list)>=min_peroson_num:
            return_group_list.append(group)
    return return_group_list

def printer_group_person_analyzeid(group):
    """
        打印组内faceobj的analyze_id
    """
    faceobj_list=group.get_group_faceobj() 
    for faceobj in faceobj_list:
        
        print("analyzeid>>",faceobj.get_analyze_id())
        

    

