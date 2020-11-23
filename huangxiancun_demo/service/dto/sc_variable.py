# -*- coding: UTF-8 -*-
# @Date    : 20120-09-01
# @Author  : cfz
# @Version : Python3.6
from service.dto.dto_base import DBHandler

class ScVariable(DBHandler):

    def __init__(self,id=None,code=None,decription=None):
        self.id=id
        self.code=code
        self.decription=decription
    
    def build_entity(self, data_tuple=None):
        if data_tuple is not None and len(data_tuple) > 0:
            return ScVariable(data_tuple[0],data_tuple[1],data_tuple[2])
        return None

    def insert(self):
        sql = """
        insert into sc_variable(id,code,decription) values (%s,%s,%s)
        """
        if self is not None and self.id is not None:
            self.excute(sql, (self.id,self.code,self.decription))
        return self

    def find_list(self):
        sql = """
        select id,code,decription from sc_variable
        """
        if self is not None:
            data_list = []
            condition_sql = ''
            
            if self.id is not None:
                condition_sql = condition_sql + ' and id=%s '
                data_list.append(self.id)
            
            if self.code is not None:
                condition_sql = condition_sql + ' and code=%s '
                data_list.append(self.code)
            
            if self.decription is not None:
                condition_sql = condition_sql + ' and decription=%s '
                data_list.append(self.decription)
            
            if len(condition_sql) > 0:
                sql = sql + ' where ' + condition_sql[4:]

            tuple_list = list(self.query_all(sql, tuple(data_list)))
            ret_list = []
            for d in tuple_list:
                build_entity = self.build_entity(d)
                if build_entity is not None:
                    ret_list.append(build_entity)
            return ret_list
        return []

    def find_by_id(self):
        sql = """
        select id,code,decription from sc_variable where id=%s
        """
        if self is not None and self.id is not None:
            d = self.query(sql, self.id)
            return self.build_entity(d)
        return None

    def update_by_id(self):
        pass

    def delete_by_id(self):
        pass