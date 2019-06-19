# coding: utf-8
"""
用于记录一个人脸对象


"""
class faceobj:
    def __init__(self,analyze_id,faceid,province=None,city=None,region=None,person_table=None):
        #用于判断是否每次参与判断剔除(用于已经判断是同一个人)
        self.if_scan=True
        
        self.analyze_id=analyze_id
        self.person_table=person_table
        
        #和检索相关属性
        self.faceid=faceid
        self.province=province
        self.city=city
        self.region=region
        
    def get_analyze_id(self):
        return self.analyze_id
    
    def get_faceid(self):
        return self.faceid
    
    def set_if_scan_false(self):
        self.if_scan=False
        
    def get_if_scan(self):
        return self.if_scan
        
        
        
