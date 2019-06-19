# coding: utf-8
"""
用于记录一个组的信息


"""
from tools.facetool import compute_faceid_dist_t1




class people_group:
    
    def __init__(self,face_max_th):
        self.face_max_th=face_max_th
        self.face_obj_list=[]
        
    def compare_with_group(self,out_face_obj,max_up_limit_percentage=0.7):
        """
                在组中比较已有的faceobj和加入的新faceobj的距离，返回大于/小于face_max_th的数量
        out_face_obj 输入的faceobj
        max_up_limit_percentage 大于阈值的faceid占总数的百分比 
        
                返回：是否加入,face_up_percentage,face_up_number,face_low_number,average_th
        """
        face_up_number=0
        all_dist=0
        index=0
        for in_face_obj in self.face_obj_list:
            if out_face_obj!=in_face_obj:
                face_dist=compute_faceid_dist_t1(in_face_obj,out_face_obj)
                all_dist=all_dist+face_dist
                index+=1
                if face_dist>self.face_max_th:
                    face_up_number+=1
        face_low_number=index-face_up_number
        face_up_percentage=face_up_number/index
        average_th=all_dist/index
        if face_up_percentage>max_up_limit_percentage:
            return False,face_up_percentage,face_up_number,face_low_number,average_th
        else:
            return True,face_up_percentage,face_up_number,face_low_number,average_th
    
    
    
    def group_self_compare(self,max_up_limit_percentage=0.7):
        """
                当加入新faceobj时候组内再重新检测一遍
        max_up_limit_percentage 大于阈值的faceid占总数的百分比
                
                返回：是否加入,从组中删除的faceobj列表
        """
        remove_faceobj_list=[]
        for faceobj in self.face_obj_list:
            face_up_number=0
            for t_faceobj in self.face_obj_list:
                face_dist=compute_faceid_dist_t1(faceobj,t_faceobj)
                if face_dist>self.face_max_th:
                    face_up_number+=1
            face_up_percentage=face_up_number/len(self.face_obj_list)
            if face_up_percentage>max_up_limit_percentage:
                remove_faceobj_list.append(faceobj)
                
        for remove_faceobj in remove_faceobj_list:
            self.face_obj_list.remove(remove_faceobj)
            
        return remove_faceobj_list

    
    def get_group_average_th(self):
        """
                获取组内的平均阈值
        """
        all_dist=0
        faceobj_list_1=self.face_obj_list
        faceobj_list_2=self.face_obj_list
        index=0
        for faceobj1 in faceobj_list_1:
            for faceobj2 in faceobj_list_2:
                dist=compute_faceid_dist_t1(faceobj1,faceobj2)
                all_dist=all_dist+dist
                index+=1
        
        return all_dist/index

    def get_group_faceobj(self):
        """
                获取组内所有faceobj
        """
        return self.face_obj_list
    
    def set_faceobj(self,faceobj):
        """
                向组内设置faceobj
        """
        self.face_obj_list.append(faceobj)
                    
    def merge_group(self,groupobj):
        """
                将其他组和这个组合并
        """
        to_face_obj_list=groupobj.get_group_faceobj()
        for faceobj in to_face_obj_list:
            self.face_obj_list.append(faceobj)
                    
        
        
        
        
        
    
    