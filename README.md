dnspod_py
=========

dnspod官方脚本无法正确获取ip地址，修正，自用。
官方原说明

替换上你的Email，密码，域名ID，记录ID等参数，就可以运行了。 会在后台一直运行，每隔30秒检查一遍IP，如果修改了就更新IP。

获得domain_id可以用curl curl -k https://dnsapi.cn/Domain.List -d "login_email=xxx&login_password=xxx"

获得record_id类似 curl -k https://dnsapi.cn/Record.List -d "login_email=xxx&login_password=xxx&domain_id=xxx"
