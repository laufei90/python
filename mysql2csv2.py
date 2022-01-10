import pymysql
import csv
import time

class View:
    def __init__(self):
        # 数据库配置
        self.host = 'localhost'
        self.database = 'testbt'
        self.table = 'websites'
        self.user = 'phpmyadmin'
        self.password = 'phpmyadmin'
        self.port = 3306

        # csv储存
        self.path = '.'
        self.inputfilename = 'input.csv'
        self.csvfilename = 'datas.csv'
        self.logfilename = 'run.log'


    def run(self):
        strat = time.time()
        rows=self.get_input()
        print(len(rows))

        with open('{}/{}'.format(self.path, self.csvfilename), 'a', encoding='utf_8_sig', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)

        # for row in rows:
        #     self.save_data(row)

        end = time.time()

        self.runtime = end - strat

    def get_input(self):
        # 打开数据库连接
        db = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database, port=self.port)

        # 使用 cursor() 方法创建一个游标对象 cursor
        cursor = db.cursor()

        # 使用 execute()  方法执行 SQL 查询
        cursor.execute("SELECT * from {}".format(self.table))

        # 使用 fetchone() 方法获取单条数据.
        results = cursor.fetchall()

        # 关闭数据库连接
        db.close()
        return results

    def save_data(self, item):
        '''
        保存文件
        '''
        print('-', end='')
        with open('{}/{}'.format(self.path, self.csvfilename), 'a', encoding='utf_8_sig', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(item)

    @property
    def time(self):
        return '总共用时：{}秒'.format(self.runtime)


if __name__ == '__main__':
    view = View()  # 实例化对象
    view.run()
    print(view.time)
