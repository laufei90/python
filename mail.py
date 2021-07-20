#!/usr/bin/python
# -*- coding: UTF-8 -*-

#导入发送邮件API
import yagmail

#链接邮箱服务器
yag = yagmail.SMTP(user="laufei90@163.com", password="CXOZGDCNZYNOKCCU", host='smtp.163.com')
#添加邮件标题
subject = "这是一个测试邮件"
# 邮箱正文
contents = '测试邮件内容'
#添加发送人
email_name = ['niufee@qq.com','laufei90@163.com']
# 发送邮件
yag.send(email_name, subject, contents)
#关闭链接
yag.close()
