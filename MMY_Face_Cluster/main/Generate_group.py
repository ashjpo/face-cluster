# coding: utf-8
"""
用于将faceobj归档


"""
from model.people_group import people_group


class Generate_group:
    def __init__(self,faceobj_list,max_face_th,max_up_limit_percentage,if_debug=False):
        """
                传入faceobj对象列表
        """
        self.if_debug=if_debug
        self.max_face_th=max_face_th
        self.max_up_limit_percentage=max_up_limit_percentage
        
        self.faceobj_list=faceobj_list
        #self.similar=similar
        
        #未归档的faceobj
        self.no_grouped_faceobj=self.faceobj_list
        
        #组列表
        self.group_list=[]
        
    
    
    
    def search_index_in_faceobj_list(self,faceobj):
        """
                在faceobj_list中查找faceobj的index
        """
        index=0
        for tmp_faceobj in self.faceobj_list:
            if tmp_faceobj==faceobj:
                return index
            else:
                pass
            
            index+=1
        return None
    
    def get_group(self):
        return self.group_list
            

        
    def archive_group(self):
        """
                用户归档
        """
        archive_batch=0
        while len(self.no_grouped_faceobj)!=0:
            '''if self.if_debug==True:
                print("archive_batch>>>",archive_batch)
                deal_with_num=len(self.faceobj_list)-len(self.no_grouped_faceobj)
                deal_with_percentage=round(deal_with_num/len(self.faceobj_list),2)
                print("deal with>>>",deal_with_percentage)'''
            
            this_batch_add_nogroup_faceobj=[]  #在这个batch完成之后处理
            this_batch_add_group_faceobj=[]  #在这个batch完成之后处理
            for i in range(len(self.no_grouped_faceobj)):
                faceobj=self.no_grouped_faceobj[i]
                #***
                if faceobj in this_batch_add_group_faceobj:
                    continue
                #创建组
                #if self.if_debug==True:
                    #print("create group")
                group_obj=people_group(self.max_face_th)
                self.group_list.append(group_obj)
                this_batch_add_group_faceobj.append(faceobj)
                group_obj.set_faceobj(faceobj)
                
                for j in range(len(self.no_grouped_faceobj)):
                    compare_faceobj=self.no_grouped_faceobj[j]
                    #***
                    if compare_faceobj in this_batch_add_group_faceobj or faceobj==compare_faceobj:
                        continue
                    
                    if_add=self.if_add_to_group(group_obj,compare_faceobj)
                    if if_add==True:
                        group_obj.set_faceobj(compare_faceobj)
                        this_batch_add_group_faceobj.append(compare_faceobj)
                        #计算组内
                        remove_faceobj_list=group_obj.group_self_compare(self.max_up_limit_percentage)
                        this_batch_add_nogroup_faceobj=this_batch_add_nogroup_faceobj+remove_faceobj_list
                      
                
            self.no_grouped_faceobj=self.no_grouped_faceobj+this_batch_add_nogroup_faceobj        
            for fobj in this_batch_add_group_faceobj:
                self.no_grouped_faceobj.remove(fobj)
            archive_batch+=1
    
    def if_add_to_group(self,group,faceobj):
        """
            用于判断是否将faceobj加入group
        """
        if_add_group,face_up_percentage,face_up_number,face_low_number,average_th=group.compare_with_group(faceobj,self.max_up_limit_percentage)
        #暂时
        return if_add_group
        
    
    
    
    
    
    
    
    
    