# SendEmail #

一个用于发送邮件的Python程序

## 配置邮件信息

config.py

      mail_host 设置服务器 如 "smtp.163.com"
  
      mail_user 用户名 如 "test"
  
      mail_pass 口令 如 "test"
  
      mail_postfix 发件箱类型 如 "163"、"qq"

## 使用说明
      
SendEmail().send_Emails(YourName, NameList, Subject, Content)
      
      YourName    你想定义的发送者名字
      NameList    邮件收件人 如 NameList = ['A','B']
      Subject     发送邮件的主题
      Content     想要发送邮件内容
