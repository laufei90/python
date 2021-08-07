import logging
import queue
import time
import pymysql

LOG = logging.getLogger(__name__)

class ConnectionPool(object):

    def __init__(self, **kwargs):

        self.size = kwargs.get('size', 10)
        self.kwargs = kwargs
        self.conn_queue = queue.Queue(maxsize=self.size)

        for i in range(self.size):
            self.conn_queue.put(self._create_new_conn())

    def _create_new_conn(self):
        return pymysql.connect(host=self.kwargs.get('host', '127.0.0.1'),
                               user=self.kwargs.get('user'),
                               password=self.kwargs.get('password'),
                               port=self.kwargs.get('port', 3306),
                               connect_timeout=5)

    def _put_conn(self, conn):
        self.conn_queue.put(conn)

    def _get_conn(self):
        conn = self.conn_queue.get()
        if conn is None:
            self._create_new_conn()
        return conn

    def exec_sql(self, sql):
        conn = self._get_conn()
        try:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
        except pymysql.ProgrammingError as e:
            LOG.error("execute sql ({0}) error {1}".format(sql, e))
            raise e
        except pymysql.OperationalError as e:
            # create connection if connection has interrupted
            conn = self._create_new_conn()
            raise e
        finally:
            self._put_conn(conn)

    def __del__(self):
        try:
            while True:
                conn = self.conn_queue.get_nowait()
                if conn:
                    conn.close()
        except queue.Empty:
            pass

mysql_conn_pools=ConnectionPool(size=5,host='192.168.31.40',user='phpmyadmin',password='phpmyadmin')
print("查询数据库版本：")
rows1=mysql_conn_pools.exec_sql('SELECT VERSION()')
for row in rows1:
    print(row)

print("查询数据库testbt中的表单hosts：")
rows2=mysql_conn_pools.exec_sql('SELECT * FROM testbt.hosts')
for row in rows2:
    print(row)

print("查询数据库的PROCESSLIST：")
rows3=mysql_conn_pools.exec_sql('SHOW PROCESSLIST')
for row in rows3:
    print(row)

time.sleep(30)
mysql_conn_pools.__del__()
