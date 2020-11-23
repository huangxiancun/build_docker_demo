# -*- coding: utf-8 -*-

# Author : 'hxc'

# Time: 2020/9/3 2:08 PM

# File_name: 'sc_node_intention.py'

"""
Describe: node  and  intention relations
"""


from service.dto.dto_base import DBHandler

class ScNodeIntention(DBHandler):

    def __init__(self, intention_id=None,
                 node_id=None,
                 name=None,
                 intention_relation_nodes=[]):
        self.intention_id = intention_id
        self.node_id = node_id
        self.name = name
        self.intention_relation_nodes = intention_relation_nodes

    def build_entity(self, data_tuple=None):
        if data_tuple is not None and len(data_tuple) > 0:
            return ScNodeIntention(data_tuple[0], data_tuple[1], data_tuple[2])
        return None

    def insert(self):
        sql = """
        insert into sc_node_intention(intention_id,node_id,name) values (%s,%s,%s)
        """
        if self is not None and self.intention_id is not None:
            self.excute(sql, (self.intention_id, self.node_id, self.name))
        return self

    def find_list(self):
        sql = """
        select intention_id, node_id, name from sc_node_intention
        """
        if self is not None:
            data_list = []
            condition_sql = ''

            if self.intention_id is not None:
                condition_sql = condition_sql + ' and intention_id=%s '
                data_list.append(self.intention_id)

            if self.node_id is not None:
                condition_sql = condition_sql + ' and node_id=%s '
                data_list.append(self.node_id)

            if self.name is not None:
                condition_sql = condition_sql + ' and name=%s '
                data_list.append(self.name)

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

    # def find_by_id(self):
    #     sql = """
    #     select intention_id,node_id,name from sc_node_intention where node_id=%s
    #     """
    #     if self is not None and self.node_id is not None:
    #         d = self.query(sql, self.node_id)
    #         return self.build_entity(d)
    #     return None
    def find_by_intention_id(self):
        """
        寻找intention_id
        :return:
        """

        sql = """
        SELECT intention_id,name FROM sc_node_intention WHERE node_id=%s
        """
        if self is not None and self.node_id is not None:
            d = self.query(sql, self.node_id,one=False)
            return d
        return None

    def update_by_id(self):
        pass

    def delete_by_id(self):
        pass