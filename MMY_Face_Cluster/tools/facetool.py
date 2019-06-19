# coding: utf-8
import numpy as np
def compute_faceid_dist_t1(faceobj1,faceobj2):
    """
        计算只含有一个faceid的faceobj的距离
    """
    faceid1=faceobj1.get_faceid()
    faceid2=faceobj2.get_faceid()
    dist = np.sum(np.square(faceid1-faceid2))
    return dist

def compute_faceid_dist_t2(faceobj,people_group):
    """
        计算faceobj和people_group中所有faceobj的距离平均值
    """
    all_dist=0
    faceobj_list=people_group.get_group_faceobj()
    for faceobj1 in faceobj_list:
        dist=compute_faceid_dist_t1(faceobj1,faceobj)
        all_dist=all_dist+dist
    
    return all_dist/len(faceobj_list)

def compute_faceid_dist_t3(faceobj,people_group,face_max_th=0.7):
    """
        计算faceobj在group中超出阈值的数量和比例
    """
    face_up_number=0
    faceobj_list=people_group.get_group_faceobj()
    for faceobj1 in faceobj_list:
        dist=compute_faceid_dist_t1(faceobj1,faceobj)
        if dist>face_max_th:
            face_up_number+=1
    face_up_percentage=face_up_number/len(faceobj_list)
    face_low_number=len(faceobj_list)-face_up_number
    return face_up_percentage,face_up_number,face_low_number

def compute_faceid_dist_t4(people_group1,people_group2):
    """
        返回两个组之间的平均距离
    """
    all_dist=0
    faceobj_list_1=people_group1.get_group_faceobj()
    faceobj_list_2=people_group2.get_group_faceobj()
    index=0
    for faceobj1 in faceobj_list_1:
        for faceobj2 in faceobj_list_2:
            dist=compute_faceid_dist_t1(faceobj1,faceobj2)
            all_dist=all_dist+dist
            index+=1
    
    return all_dist/index


