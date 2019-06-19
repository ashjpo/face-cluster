# coding: utf-8
import numpy as np
from tools.facetool import compute_faceid_dist_t1
"""
用于计算人脸的相似矩阵


"""

class Generate_face_similar:
    def __init__(self):
        self.similar=None
        self.faceobj_list=[]
        
    def get_similar(self):
        return self.similar
    
    def set_faceobj_list(self,faceobj_list):
        self.faceobj_list=faceobj_list
    
    def compute_similar(self):
        self.similar=np.zeros([len(self.faceobj_list),len(self.faceobj_list)])
        index_o=0
        for obj1 in self.faceobj_list:
            index_i=0
            for obj2 in self.faceobj_list:
                dist=compute_faceid_dist_t1(obj1,obj2)
                self.similar[index_o][index_i]=dist
                index_i+=1
            index_o+=1
    
    
    
    
    
    
    
    