import pymysql
from DBUtils.PooledDB import PooledDB
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('./'))
template = env.get_template("dto_tpl.txt")

class conDB(object):
    def __init__(self, *args):
        self.conPool = PooledDB(
            pymysql,
            8,
            host='localhost',
            port=3306,
            user='root',
            passwd='root',
            db='robot_outbound',
            charset='utf8')

class Table(object):
    def __init__(self,name=None,comment=None,rows=None):
        self.name = name
        self.comment = comment
        self.rows = rows

class TableRow(object):
    def __init__(self,num=None,column_name=None,column_pri=None,column_type=None,column_nullable=None,column_remarkes=None):
        self.num = num
        self.column_name = column_name
        self.column_pri = column_pri
        self.column_type = column_type
        self.column_nullable = column_nullable
        self.column_remarkes = column_remarkes

def export(pool,database,table_name,class_name):
    conn = pool.connection()
    cursor = conn.cursor()
    table_sql = """
        SELECT 
            ORDINAL_POSITION num,
            COLUMN_NAME column_name,
            IF(COLUMN_KEY='PRI', '是', '否') column_pri,
            COLUMN_TYPE column_type,
            IF(IS_NULLABLE='YES', '是', '否') column_nullable,
            COLUMN_COMMENT column_remarkes 
        FROM information_schema.COLUMNS
        WHERE TABLE_SCHEMA = '%s'
        AND table_name = '%s';
    """

    sql = table_sql % (database, table_name)
    cursor.execute(sql)
    rows = cursor.fetchall()
    export_rows = []
    for row in rows:
        export_rows.append(TableRow(row[0],row[1],row[2],row[3],row[4],row[5]))
    table = Table(table_name,None,export_rows)
    print(table)
    data = { 'class_name' : class_name, 'table' : table}
    with open(table_name + '.py', 'w') as fout:
        content = template.render(data)
        fout.write(content)

if __name__=="__main__":
    conPool = conDB().conPool
    export(conPool, 'robot_outbound', 'sc_instance','ScInstance')
    conPool.close()