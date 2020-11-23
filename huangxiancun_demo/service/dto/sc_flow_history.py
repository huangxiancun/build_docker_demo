# -*- coding: UTF-8 -*-
# @Date    : 20120-09-01
# @Author  : cfz
# @Version : Python3.6
from service.dto.dto_base import DBHandler

class ScFlowHistory(DBHandler):

    def __init__(self,id=None,instance_id=None,flow_id=None,node_id=None,intention_id=None,question=None,answer=None,create_time=None):
        self.id=id
        self.instance_id=instance_id
        self.flow_id=flow_id
        self.node_id=node_id
        self.intention_id=intention_id
        self.question=question
        self.answer=answer
        self.create_time=create_time
    
    def build_entity(self, data_tuple=None):
        if data_tuple is not None and len(data_tuple) > 0:
            return ScFlowHistory(data_tuple[0],data_tuple[1],data_tuple[2],data_tuple[3],data_tuple[4],data_tuple[5],data_tuple[6],data_tuple[7])
        return None

    def insert(self):
        sql = """
        insert into sc_flow_history(id,instance_id,flow_id,node_id,intention_id,question,answer,create_time) values (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        if self is not None and self.id is not None:
            self.excute(sql, (self.id,self.instance_id,self.flow_id,self.node_id,self.intention_id,self.question,self.answer,self.create_time))
        return self

    def find_list(self):
        sql = """
        select id,instance_id,flow_id,node_id,intention_id,question,answer,create_time from sc_flow_history
        """
        if self is not None:
            data_list = []
            condition_sql = ''
            
            if self.id is not None:
                condition_sql = condition_sql + ' and id=%s '
                data_list.append(self.id)
            
            if self.instance_id is not None:
                condition_sql = condition_sql + ' and instance_id=%s '
                data_list.append(self.instance_id)
            
            if self.flow_id is not None:
                condition_sql = condition_sql + ' and flow_id=%s '
                data_list.append(self.flow_id)
            
            if self.node_id is not None:
                condition_sql = condition_sql + ' and node_id=%s '
                data_list.append(self.node_id)
            
            if self.intention_id is not None:
                condition_sql = condition_sql + ' and intention_id=%s '
                data_list.append(self.intention_id)
            
            if self.question is not None:
                condition_sql = condition_sql + ' and question=%s '
                data_list.append(self.question)
            
            if self.answer is not None:
                condition_sql = condition_sql + ' and answer=%s '
                data_list.append(self.answer)
            
            if self.create_time is not None:
                condition_sql = condition_sql + ' and create_time=%s '
                data_list.append(self.create_time)
            
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
        select id,instance_id,flow_id,node_id,intention_id,question,answer,create_time from sc_flow_history where id=%s
        """
        if self is not None and self.id is not None:
            d = self.query(sql, self.id)
            return self.build_entity(d)
        return None

    def update_by_id(self):
        pass

    def delete_by_id(self):
        pass