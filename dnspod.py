#!/usr/bin/env python
#-*- coding:utf-8 -*-
 
import httplib, urllib
import socket
import time

params = dict(
        login_email="", # replace with your email
        login_password="", # replace with your password
        format="json",
        domain_id=, # replace with your domain_id, can get it by API Domain.List
        record_id=, # replace with your record_id, can get it by API Record.List
        sub_domain="@", # replace with your sub_domain
        record_line="默认"
)
lastIp = ""
record_url = ""
def getLastIp():
        ip = ""
        try:
                f = open('lastIp', 'r')
                ip = f.read()
                f.close()
        except Exception, e:
                pass
        return ip
        
def storeIp(ip):
        f = open('lastIp', 'w')
        f.write(ip)
        f.close()
        
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

def uploadIp(ip):
        url = record_url + "?cmd=1&ip=" + ip
        urllib.urlopen(url)
        pass
                
        
def getip():
        url = 'http://myip.dnsdynamic.org'
        page = urllib.urlopen(url)
        ip = page.read()
        return ip

if __name__ == '__main__':
    while True:
                try:
                        ip = getip()
                        uploadIp(ip)
                        print ip
                        current_ip = lastIp
                        if current_ip != ip:
                                if ddns(ip):
                                        pass
                except Exception, e:
                        print e
                        pass
                time.sleep(300)
