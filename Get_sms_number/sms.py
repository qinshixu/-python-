#!/usr/bin/env python
#coding:utf-8
import re
import hashlib
import requests
import json
from suds.client import Client


def MD5(pwd):
    m=hashlib.md5()
    m.update(pwd)
    pwd=m.hexdigest()
    return pwd


def zucp(sn='',key=''):
    pwd=''
    snkey=sn+key
    pwd=MD5(snkey).upper()
    Old_url = 'http://sdk2.zucp.net:8060/webservice.asmx/balance?'
    url = Old_url + 'sn=%s&pwd=%s' % (sn,pwd)
    resp = requests.get(url)
    resp = resp.content.split('\r\n')
    mat = re.match(r'(.*)">(.*)</string>',resp[1])
    if mat:
        print int(mat.group(2))
    else:
        print 0


def weimi(uid,key):
    url='http://api.weimi.cc/2/account/balance.html'+'?type=json&uid=%s&pas=%s' % (uid,key)
    resp = requests.get(url)
    resp=eval(resp.content)
    print int(resp['sms-left'])


def webchinese(uid,key):
    url='http://sms.webchinese.cn/web_api/SMS/?Action=SMS_Num&Uid=%s&Key=%s' % (uid,key)
    resp = requests.get(url)
    print int(resp.content)


def dhst(uid,key):
    pwd=MD5(key)
    message='''<?xml version="1.0" encoding="UTF-8"?><message><account>'''+uid+"</account><password>"+pwd+"</password></message>"
    message='''<message><account>'''+uid+"</account><password>"+pwd+"</password></message>"
    url='http://3tong.net/http/sms/Balance?message=%s' % message
    resp=requests.get(url)
    mat=re.match('(.*)<number>(.*)</number>',resp.content)
    if "鉴权失败" in resp.content:
        #print "主机: %s ip鉴权失败，请使用浏览器查看: %s" % (host,url)
	print 0
    elif mat:
        print int(mat.group(2))
    else:
        print 0


def itrigo(uid,key):
    url='http://221.122.112.136:8080/sms/mm.jsp?uid=%s&pwd=%s' % (uid,key)
    resp=requests.get(url)
    number=resp.content.split('||')
    if number[0]=='100':
        print int(number[1])
    else:
        print 0


def zyer(uid,key):
    pwd=MD5(key)[8:24]
    url='http://sdk.zyer.cn/SmsService/SmsService.asmx/GetBalance?LoginName=%s&Password=%s&SmsKind=808' % (uid,pwd)
    resp=requests.get(url)
    #print resp.content.split('\n')[3].strip(' ')
    mat=re.match(r'<Balance>(.*)</Balance>',resp.content.split('\n')[3].strip(' '))
    if mat:
        print int(mat.group(1))
    else:
        print 0
def emay(uid,key):
    url='http://sdk999ws.eucp.b2m.cn:8080/sdkproxy/querybalance.action?cdkey=%s&password=%s' % (uid,key)
    resp=requests.get(url)
    mat=re.match(r'(.*)<message>(.*)</message>',resp.content.strip('\n\r'))
    if mat:
        print int(mat.group(2))
    else:
        print 0

def chinacom(uid,key):
    url='http://sms.chinacomservice.net:8069/GeneralWs/services/DkfServices?wsdl'
    client=Client(url)
    resp=client.service.getUserSmsCount(uid,key)
    if resp=='104':
        print 0
    else:
        print int(resp)

if __name__ == "__main__":
    pass
#    weimi()
#    webchinese()
#     dhst()
#    itrigo()
#    zyer()
#    emay()
