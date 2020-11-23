# -*- coding: UTF-8 -*-
# @Date    : 20120-09-01
# @Author  : cfz
# @Version : Python3.6
from service.dto.dto_base import DBHandler

class ScIntention(DBHandler):

    def __init__(self,id=None,
                 name=None,
                 utterances=None,
                 keywords=None,
                 description=None,
                 create_time=None,
                 update_time=None,
                 intention_relation_nodes=[]):
        self.id=id
        self.name=name
        self.utterances=utterances
        self.keywords=keywords
        self.description=description
        self.create_time=create_time
        self.update_time=update_time
        self.intention_relation_nodes=intention_relation_nodes

    def build_entity(self, data_tuple=None):
        if data_tuple is not None and len(data_tuple) > 0:
            return ScIntention(data_tuple[0],data_tuple[1],data_tuple[2],data_tuple[3],data_tuple[4],data_tuple[5],data_tuple[6])
        return None

    def insert(self):
        sql = """
        insert into sc_intention(id,name,utterances,keywords,description,create_time,update_time) values (%s,%s,%s,%s,%s,%s,%s)
        """
        if self is not None and self.id is not None:
            self.excute(sql, (self.id,self.name,self.utterances,self.keywords,self.description,self.create_time,self.update_time))
        return self

    def find_list(self):
        sql = """
        select id,name,utterances,keywords,description,create_time,update_time from sc_intention
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
            
            if self.utterances is not None:
                condition_sql = condition_sql + ' and utterances=%s '
                data_list.append(self.utterances)
            
            if self.keywords is not None:
                condition_sql = condition_sql + ' and keywords=%s '
                data_list.append(self.keywords)
            
            if self.description is not None:
                condition_sql = condition_sql + ' and description=%s '
                data_list.append(self.description)
            
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
    #yl添加
    def build_dic(self):
        intent_dic = {}
        for each in self.find_list():
            if str(each.id).endswith('01'):
                intent_dic[each.id] = each.name
        return  intent_dic

    def find_by_id(self):
        sql = """
        select id,name,utterances,keywords,description,create_time,update_time from sc_intention where id=%s
        """
        if self is not None and self.id is not None:
            d = self.query(sql, self.id)
            return self.build_entity(d)
        return None

    def update_by_id(self):
        pass

    def delete_by_id(self):
        pass


