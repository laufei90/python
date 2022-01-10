import pymysql
from pprint import pprint
import pandas
class Test_myqsl(object):
    #运行数据库和建立游标对象
    def __init__(self):
        self.connect = pymysql.connect(host="127.0.0.1", port=3306, user="phpmyadmin", password="phpmyadmin", database="testbt",
                                  charset="utf8")
        # 返回一个cursor对象,也就是游标对象
        self.cursor = self.connect.cursor(cursor=pymysql.cursors.DictCursor)
    #关闭数据库和游标对象
    def __del__(self):
        self.connect.close()
        self.cursor.close()
    def write(self):
        #将数据转化成DataFrame数据格式
        data = pandas.DataFrame(self.read())
        #把id设置成行索引
        data_1 = data.set_index("id",drop=True)
        #写写入数据数据
        pandas.DataFrame.to_csv(data_1,"./mysql.csv",encoding="utf_8_sig")
        print("写入成功")
    def read(self):
        #读取数据库的所有数据
        data = self.cursor.execute("""select * from websites""")
        field_2 = self.cursor.fetchall()
        #pprint(field_2)
        return field_2
#封装
def main():
    write = Test_myqsl()
    write.write()

if __name__ == '__main__':
    main()

