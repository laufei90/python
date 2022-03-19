import pymysql
import csv
import time

class Mysql2csv:
    def __init__(self):
        # 数据库配置
        self.__host = 'localhost'
        self.__database = 'testbt'
        self.__table = 'websites'
        self.__user = 'phpmyadmin'
        self.__password = 'phpmyadmin'
        self.__port = 3306
        #查询sql语句
        self.__query_sql = "SELECT * from {}".format(self.__table)
        self.__header = ['id','name','url','alexa','country']
        # csv储存文件
        self.__path = '.'
        self.__csvfilename = time.strftime("UPS_Battery_%Y%m%d%H%M%S.csv", time.localtime())


    def run(self):
        strat = time.time()
        rows=self.get_input()
        print("读取Mysql监控数据库")
        print("UPS电池数据行数：",len(rows))
        
        with open('{}/{}'.format(self.__path, self.__csvfilename), 'a', encoding='utf_8_sig', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.__header)
            writer.writerows(rows)
        print("写入csv文件中，保存路径:{}\{}".format(self.__path,self.__csvfilename))
        
        end = time.time()
        self.runtime = end - strat

    def get_input(self):
        db = pymysql.connect(host=self.__host, user=self.__user, password=self.__password, database=self.__database, port=self.__port)
        cursor = db.cursor()
        cursor.execute(self.__query_sql)
        results = cursor.fetchall()
        db.close()
        return results

    @property
    def time(self):
        return '总共用时：{:.2f}秒'.format(self.runtime)


if __name__ == '__main__':
    mysql2csv = Mysql2csv()  
    mysql2csv.run()
    print(mysql2csv.time)
