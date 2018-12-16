import os,unittest,time
from Report.HTMLTestRunner3 import HTMLTestRunner
import unittest
import time#以免每次生成的报告名称一样报告会被覆盖，所以引入时间命名报告，可以看到每次运行的报告
import os#用于查找最新report文件
from email.mime.multipart import MIMEMultipart
import datetime
from smtplib import SMTP
from smtplib import SMTPException
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header


now = time.strftime("%Y-%m-%d %H_%M_%S")
def create_suite():
    TestSuite = unittest.TestSuite()#测试集
    # test_dir = os.getcwd()+'\\TestCase\\'
    test_dir = os.path.realpath('TestCase')

    discover = unittest.defaultTestLoader.discover(
        start_dir=test_dir,
        pattern='test_*.py',
        top_level_dir=None
    )

    # print (discover)

    for test_case in discover:
        TestSuite.addTests(test_case)
    return TestSuite

def report():

    # report_name = os.getcwd()+'\\Report\\result.html'
    report_name = os.path.join(os.path.realpath("Report"), now + '_result.html')
    return report_name


def send_mail(file):

    try:
        email_client = SMTP('smtp.163.com')
        email_client.login('13730686357@163.com', 'hejing007')
        # msg = MIMEText(content, 'plain', 'utf-8')
        msg = MIMEMultipart()
        part_text = MIMEText('测试报告', 'plain', 'utf-8')
        msg.attach(part_text)
        msg['Subject'] = Header(f'UFO自动化测试报告_{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}', 'utf-8')
        msg['From'] = '13730686357@163.com'
        msg['To'] = 'yuanyi@testbird.com'
        f = open(file, 'rb')
        part_file = MIMEApplication(f.read())
        part_file.add_header('Content-Disposition', 'attachment', filename=report())
        msg.attach(part_file)
        email_client.sendmail('13730686357@163.com', 'yuanyi@testbird.com', msg.as_string())
        email_client.quit()
        print(u'测试报告邮件发送成功!')
    except SMTPException:
        print(u'测试报告邮件发送失败!')




if __name__ == '__main__':

    fp = open(report(), 'wb')

    TestSuite = create_suite()
    Runner = HTMLTestRunner(
        stream=fp,
        title='测试报告',
        description='测试用例执行情况'
    )
    Runner.run(TestSuite)
    fp.close()
    time.sleep(5)

    res = report()
    send_mail(res)

