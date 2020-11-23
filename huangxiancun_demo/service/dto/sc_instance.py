# -*- coding: UTF-8 -*-
# @Date    : 20120-09-02
# @Author  : cfz
# @Version : Python3.6

from service.dto.dto_base import DBHandler

class ScInstance(DBHandler):

    def __init__(self,id=None,user_name=None,category=None,phone_number=None,content=None,flow_content=None,status=None,create_time=None):
        self.id=id
        self.user_name = user_name
        self.category=category
        self.phone_number=phone_number
        self.content=content
        self.flow_content=flow_content
        self.status=status,
        self.create_time=create_time
    
    def build_entity(self, data_tuple=None):
        if data_tuple is not None and len(data_tuple) > 0:
            return ScInstance(data_tuple[0],data_tuple[1],data_tuple[2],data_tuple[3],data_tuple[4],data_tuple[5],data_tuple[6],data_tuple[7])
        return None

    def insert(self):
        sql = """
        insert into sc_instance(id,user_name,category,phone_number,content,flow_content,status,create_time) values (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        if self is not None and self.id is not None:
            self.excute(sql, (self.id,self.user_name,self.category,self.phone_number,self.content,self.flow_content,self.status,self.create_time))
        return self

    def find_list(self):
        sql = """
        select id,user_name,category,phone_number,content,flow_content,status,create_time from sc_instance
        """
        if self is not None:
            data_list = []
            condition_sql = ''
            
            if self.id is not None:
                condition_sql = condition_sql + ' and id=%s '
                data_list.append(self.id)

            if self.user_name is not None:
                condition_sql = condition_sql + ' and category=%s '
                data_list.append(self.user_name)
            
            if self.category is not None:
                condition_sql = condition_sql + ' and category=%s '
                data_list.append(self.category)
            
            if self.phone_number is not None:
                condition_sql = condition_sql + ' and phone_number=%s '
                data_list.append(self.phone_number)
            
            if self.content is not None:
                condition_sql = condition_sql + ' and content=%s '
                data_list.append(self.content)
            
            if self.flow_content is not None:
                condition_sql = condition_sql + ' and flow_content=%s '
                data_list.append(self.flow_content)

            if self.status is not None:
                condition_sql = condition_sql + ' and status=%s '
                data_list.append(self.status)
            
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
        select id,user_name,category,phone_number,content,flow_content,status,create_time from sc_instance where id=%s
        """
        if self is not None and self.id is not None:
            d = self.query(sql, self.id)
            return self.build_entity(d)
        return None


    def update_by_id(self):
        """
        更新数据
        :return:
        """

        sql = """
         UPDATE sc_instance SET content="%s",flow_content="%s"
        """
        sql_update = sql % (self.content, self.flow_content) + 'where user_name=%s and phone_number=%s ;'



        if self is not None and self.user_name is None and self.phone_number is None:
            self.excute(sql_update, (self.user_name,self.phone_number))
        return None



    def delete_by_id(self):
        pass