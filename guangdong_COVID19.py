#通过Requests获取广东的疫情数据的Json请求，然后通过Matplotlib绘制图表。
import time
import json
import requests
import matplotlib.pyplot as plt 
import numpy as np

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
#print(url)
# 抓取腾讯疫情实时json数据
data = json.loads(requests.get(url=url).json()['data'])

# 打印最后更新时间
print(data['lastUpdateTime'])

# 统计省份信息
num = data['areaTree'][0]['children']

# 广东省总数据
gdong = num[1]
#print(gdong)
print(gdong['total'])

gdong_children_total_data = {}
for item in gdong['children']:
    if item['name'] not in gdong_children_total_data:
        gdong_children_total_data.update({item['name']:0})
    gdong_children_total_data[item['name']] += int(item['total']['nowConfirm']) 
#print(gdong_children_total_data)

gd_names = gdong_children_total_data.keys()
gd_numbers = gdong_children_total_data.values()

# 广东plt绘图
# 用来正常显示中文标签
plt.rcParams['font.sans-serif'] = ['simhei']   
plt.figure(figsize=[10,6])
plt.bar(gd_names,gd_numbers,color='green')
plt.xlabel("地区", size=12)
plt.ylabel("确诊人数", fontproperties='SimHei', rotation=90, size=12)
plt.title("广东省不同地区疫情现存确诊数对比图", size=16)
plt.xticks(list(gd_names), rotation=90, size=12)    
plt.show()




