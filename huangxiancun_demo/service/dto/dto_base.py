# -*- coding: UTF-8 -*-
# @Date    : 20120-09-01
# @Author  : cfz
# @Version : Python3.6

import pymysql
import threading
from DBUtils.PooledDB import PooledDB
from service.config.config import cfg

class DBHandler(object):
    __instance_lock = threading.Lock()
    __pool = PooledDB(pymysql,
                     mincached=cfg.DBCONFIG.MINCACHED,
                     maxcached=cfg.DBCONFIG.MAXCACHED,
                     maxconnections=cfg.DBCONFIG.MAXCONNECTIONS,
                     blocking=cfg.DBCONFIG.BLOCKING,
                     maxshared=cfg.DBCONFIG.MAXSHARED,
                     host=cfg.DBCONFIG.HOST,
                     port=cfg.DBCONFIG.PORT,
                     user=cfg.DBCONFIG.USER ,
                     passwd=cfg.DBCONFIG.PASSWD,
                     db=cfg.DBCONFIG.DBNAME,
                     charset=cfg.DBCONFIG.CHARSET)

    def __init__(self):
        print("DBHandler init.")

    def __new__(cls, *args, **kwargs):
        if not hasattr(DBHandler, "__instance"):
            with DBHandler.__instance_lock:
                if not hasattr(DBHandler, "__instance"):
                    DBHandler.__instance = object.__new__(cls)
        return DBHandler.__instance

    @staticmethod
    def get_pool():
        return DBHandler.__pool

    @staticmethod
    def set_pool(custom_pool):
        with DBHandler.__instance_lock:
            DBHandler.__pool = custom_pool

    def query_one(self, query, args=None):
        conn = DBHandler.__pool.connection()
        cursor = conn.cursor()
        try:
            # print('DataBae log, sql: %s, params: %s' % (query, str(args)))
            cursor.execute(query, args)
            conn.commit()
            return cursor.fetchone()
        except Exception as e:
            conn.rollback()
            print('Database query_one Error: ', e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def query_all(self, query, args=None):
        conn = DBHandler.__pool.connection()
        cursor = conn.cursor()
        try:
            # print('DataBae log, sql: %s, params: %s' % (query, str(args)))
            cursor.execute(query, args)
            conn.commit()
            return cursor.fetchall()
        except Exception as e:
            conn.rollback()
            print('Database query_all Error: ', e)
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def query(self, query, args=None, one=True):
        if one:
            return self.query_one(query, args)
        return self.query_all(query, args)


    def excute(self, query, args=None):
        conn = DBHandler.__pool.connection()
        cursor = conn.cursor()
        try:
            # print('DataBae log, sql: %s, params: %s' % (query, str(args)))
            cursor.execute(query, args)
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            print('Database excute Error: ', e)
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()

    def excute_many(self, query, args=None, batch_size=100):
        conn = DBHandler.__pool.connection()
        cursor = conn.cursor()
        try:
            # print('DataBae log, sql: %s, params: %s' % (query, str(args)))
            num = 0
            list = []
            for d in args:
                num = num + 1
                list.append(d)
                if num == batch_size:
                    cursor.executemany(query, list)
                    conn.commit()
                    num = 0
                    list.clear()
            return True
        except Exception as e:
            conn.rollback()
            print('Database excute Error: ', e)
            return False
        finally:
            if cursor:
                cursor.close()
            if conn:
                conn.close()