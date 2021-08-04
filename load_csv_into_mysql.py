import csv
from collections import namedtuple
#import MySQLdb as db
import pymysql as db

def get_data(file_name):
    with open(file_name) as f:
        f_csv = csv.reader(f)
        headings = next(f_csv)
        Row = namedtuple('Row', headings)
        for r in f_csv:
            yield Row(*r)

def execute_sql(conn, sql):
    with conn.cursor() as cur:
        cur.execute(sql)

def main():
    conn=db.connect(host='192.168.1.32', user='phpmyadmin', passwd='phpmyadmin', db='testbt')    
    SQL_FORMAT = """insert into student values({0}, '{1}', {2})"""
    for t in get_data('data.csv'):
        sql = SQL_FORMAT.format(t.sno, t.sname, t.sage)
        execute_sql(conn, sql)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    main()
