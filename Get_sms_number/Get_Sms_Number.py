#!/usr/bin/env python
#coding:utf-8

global sms_content
sms_content=[]
import sms
import sys,os
import xml.etree.ElementTree as Etree

def Get_Sms_Number(SMS_Config):
  #  print SMS_Config
    uid=SMS_Config['uid']
    key=SMS_Config['key']
    url=SMS_Config['url']
    zucp_url='http://sdk.entinfo.cn:8060/webservice.asmx'
    weimi_url='http://api.weimi.cc/2/sms/send.html'
    webchinese_url='http://utf8.sms.webchinese.cn'
    dhsturl='http://3tong.net/http/sms/Submit'
    itrigourl='http://221.122.112.136:8080/sms/mt.jsp'
    mandaourl='http://sdk2.entinfo.cn:8061/mdsmssend.ashx'
    zyerurl='http://sdk.zyer.cn/SmsService/SmsService.asmx/SendEx'
    emayurl='http://sdk999ws.eucp.b2m.cn:8080/sdk/SDKService?wsdl'
    chinacomurl='http://sms.chinacomservice.net:8069/GeneralWs/services/DkfServices?wsdl'

    if SMS_Config['url']==zucp_url or url==mandaourl:
        sms.zucp(uid,key)
    elif SMS_Config['url']==weimi_url:
        sms.weimi(uid,key)
    elif SMS_Config['url']==webchinese_url:
        sms.webchinese(uid,key)
    elif url==dhsturl:
        sms.dhst(uid,key)
    elif url==itrigourl:
        sms.itrigo(uid,key)
    elif url==zyerurl:
        sms.zyer(uid,key)
    elif url==emayurl:
        sms.emay(uid,key)
    elif url==chinacomurl:
        sms.chinacom(uid,key)
    else:
        print host,'客户自己的短信平台,无法获取: %s' % (SMS_Config['url'])
        return sms_content

def Get_Sms_config():
    #key = paramiko.RSAKey.from_private_key_file(pkey_file)
   # s = paramiko.SSHClient()
   # s.load_system_host_keys()
   # s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
   # try:
    #    s.connect(hostname,port,username,pkey=key)
     #   stdin,stdout,stderr = s.exec_command(cmd)
    std=os.popen(cmd)
    Get_Content=['url','uid','key']
    for std in std.readlines():
        try:
            notify_data_tree = Etree.fromstring(std)
            for j in Get_Content:
                str_value = notify_data_tree.getiterator(j)
                for i in str_value:
                    #print i.text
                    SMS_Config[j]=i.text
        except Exception,e:
            os.system('exit')
#    print SMS_Config
    Get_Sms_Number(SMS_Config)


if __name__== "__main__":
    SMS_Config={}
    cmd="cat /var/CreditCloud/config/SMSConfig.xml"
    filename=['SMSConfig.xml.itrigo','SMSConfig.xml.zy','SMSConfig.xml.weimi','SMSConfig.xml.wj','SMSConfig.xml.zucp']
    pkey_file='/root/.ssh/id_rsa'
    port=22
    username='root'
    Get_Sms_config()
   # for i in filename:
    #    cmd='cat /var/CreditCloud/config/%s' % i
     #   Get_Sms_config()

