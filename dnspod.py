#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import httplib, urllib
import socket
import time
 
params = dict(
    login_email="username@emaildomain", # replace with your email
    login_password="password", # replace with your password
    format="json",
    domain_id=100, # replace with your domain_od, can get it by API Domain.List
    record_id=100, # replace with your record_id, can get it by API Record.List
    sub_domain="@", # replace with your sub_domain
    record_line="默认",
)
current_ip = None
 
def ddns(ip):
    params.update(dict(value=ip))
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/json"}
    conn = httplib.HTTPSConnection("dnsapi.cn")
    conn.request("POST", "/Record.Ddns", urllib.urlencode(params), headers)
    
    response = conn.getresponse()
    print response.status, response.reason
    data = response.read()
    print data
    conn.close()
    return response.status == 200
 
def getip():
    url = 'http://myip.dnsdynamic.org'
    page = urllib.urlopen(url)
    ip = page.read()
    return ip
 
if __name__ == '__main__':
    while True:
        try:
            ip = getip()
            print ip
            if current_ip != ip:
                if ddns(ip):
                    current_ip = ip
        except Exception, e:
            print e
            pass
        time.sleep(30)
