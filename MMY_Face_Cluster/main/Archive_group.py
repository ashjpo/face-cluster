# coding: utf-8
"""
用于faceobj归入group中【不创建】


"""
from model.people_group import people_group

class Archive_group:
    def __init__(self,generated_group_list,faceobj_list,max_face_th,max_up_limit_percentage,if_debug=False):
        self.if_debug=if_debug
        self.max_face_th=max_face_th
        self.max_up_limit_percentage=max_up_limit_percentage
        
        self.faceobj_list=faceobj_list
        #self.similar=similar
        
        #未归档的faceobj
        self.no_grouped_faceobj=self.faceobj_list
        
        
        
        self.generated_group_list=generated_group_list
        
    def to_group(self):
        for i in range(len(self.no_grouped_faceobj)):
            faceobj=self.no_grouped_faceobj[i]
            for group in self.generated_group_list:
                if_add=self.if_add_to_group(group,faceobj)
                
                if if_add==True:
                    group.set_faceobj(faceobj)
                    break
            
    def if_add_to_group(self,group,faceobj):
        """
            用于判断是否将faceobj加入group
        """
        if_add_group,face_up_percentage,face_up_number,face_low_number,average_th=group.compare_with_group(faceobj,self.max_up_limit_percentage)
        #暂时
        return if_add_group
        
        
        
    
    
    
    
    
    
    