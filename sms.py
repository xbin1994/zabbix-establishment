#!/usr/bin/python
# -*- coding: utf-8 -*-
import top.api
import sys

req = top.api.AlibabaAliqinFcSmsNumSendRequest('gw.api.taobao.com',80)
req.set_app_info(top.appinfo('****','****'))
req.extend = ""
req.sms_type = "normal"
req.sms_free_sign_name = "****"
mes = sys.argv[1]
mes = mes.replace('.','_')
req.sms_param = "{'message':%s}" %mes
req.rec_num = "1311111111"
req.sms_template_code = "****"
try :
    resp = req.getResponse()
    print (resp)
except Exception,e:
    print (e)
