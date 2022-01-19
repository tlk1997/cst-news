import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header

def send_email(info):
# 1. 连接邮箱服务器
    con = smtplib.SMTP_SSL('smtp.163.com', 465)

    # 2. 登录邮箱
    con.login('send_email', 'passwd') 

    # 2. 准备数据
    # 创建邮件对象
    msg = MIMEMultipart()

    # 设置邮件主题
    subject = Header('新消息', 'utf-8').encode()
    msg['Subject'] = subject

    # 设置邮件发送者
    msg['From'] = 'send_email <send_email>'

    # 设置邮件接受者
    msg['To'] = 'receive_email'

    # 添加文字内容
    text = MIMEText(info, 'plain', 'utf-8')
    msg.attach(text)
    # 3.发送邮件
    con.sendmail('send_email', 'receive_email', msg.as_string())
    con.quit()
