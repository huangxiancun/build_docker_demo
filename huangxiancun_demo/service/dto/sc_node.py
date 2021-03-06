# -*- coding: UTF-8 -*-
# @Date    : 20120-09-01
# @Author  : cfz
# @Version : Python3.6
from service.dto.dto_base import DBHandler

class ScNode(DBHandler):

    def __init__(self,id=None,
                 name=None,
                 description=None,
                 action=None,
                 create_time=None,
                 update_time=None,
                 node_speechcrafts=[],
                 node_intentions=[]):
        self.id=id
        self.name=name
        self.description=description
        self.action=action
        self.create_time=create_time
        self.update_time=update_time
        self.node_speechcrafts=node_speechcrafts
        self.node_intentions=node_intentions

    def build_entity(self, data_tuple=None):
        if data_tuple is not None and len(data_tuple) > 0:
            return ScNode(data_tuple[0],data_tuple[1],data_tuple[2],data_tuple[3],data_tuple[4],data_tuple[5])
        return None

    def insert(self):
        sql = """
        insert into sc_node(id,name,description,action,create_time,update_time) values (%s,%s,%s,%s,%s,%s)
        """
        if self is not None and self.id is not None:
            self.excute(sql, (self.id,self.name,self.description,self.action,self.create_time,self.update_time))
        return self

    def find_list(self):
        sql = """
        select id,name,description,action,create_time,update_time from sc_node
        """
        if self is not None:
            data_list = []
            condition_sql = ''
            
            if self.id is not None:
                condition_sql = condition_sql + ' and id=%s '
                data_list.append(self.id)
            
            if self.name is not None:
                condition_sql = condition_sql + ' and name=%s '
                data_list.append(self.name)
            
            if self.description is not None:
                condition_sql = condition_sql + ' and description=%s '
                data_list.append(self.description)
            
            if self.action is not None:
                condition_sql = condition_sql + ' and action=%s '
                data_list.append(self.action)
            
            if self.create_time is not None:
                condition_sql = condition_sql + ' and create_time=%s '
                data_list.append(self.create_time)
            
            if self.update_time is not None:
                condition_sql = condition_sql + ' and update_time=%s '
                data_list.append(self.update_time)
            
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
        select id,name,description,action,create_time,update_time from sc_node where id=%s
        """
        if self is not None and self.id is not None:
            d = self.query(sql, self.id)
            return self.build_entity(d)
        return None

    def update_by_id(self):
        pass

    def delete_by_id(self):
        pass