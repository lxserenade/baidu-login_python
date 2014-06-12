

import urllib2
import urllib
import urllib
import cookielib
import re
import HTMLParser



def tieba():
    username = 'XXXXX'
    psw = 'XXXXXX'
    login_tokenStr = '''bdPass.api.params.login_token='(.*?)';'''
    login_tokenObj = re.compile(login_tokenStr,re.DOTALL)
    #cookiename = 'baidu%s.coockie' % (username)
    cj=cookielib.CookieJar()
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
    opener.addheaders = [('User-agent','Mozilla/5.0')]
    urllib2.install_opener(opener)
    indexurl = u'http://www.baidu.com/'
    r = opener.open(indexurl)
    url="https://passport.baidu.com/v2/api/?getapi&class=login&tpl=mn&tangram=true"
    r = opener.open(url)

    rsp = r.read()

    matched_objs = login_tokenObj.findall(rsp)
    if matched_objs:
        token = matched_objs[0]
    post_data = urllib.urlencode({'username':username,
                                    'password':psw,
                                    'token':token,
                                    'charset':'UTF-8',
                                    'callback':'parent.bd12Pass.api.login._postCallback',
                                    'index':'0',
                                    'isPhone':'false',
                                    'mem_pass':'on',
                                    'loginType':'1',
                                    'safeflg':'0',
                                    'staticpage':'https://passport.baidu.com/v2Jump.html',
                                    'tpl':'mn',
                                    'u':'http://www.baidu.com/',
                                    'verifycode':'',
                                    })
    #path = 'http://passport.baidu.com/?login'
    path = 'http://passport.baidu.com/v2/api/?login'

    headers = { 'Accept':'image/webp,*/*;q=0.8',
                'Accept-Encoding':'gzip,deflate,sdch',
                'Accept-Language':'en-US,en;q=0.8',
                'Connection':'keep-alive',
                'Host':'hm.baidu.com',
                'Referer':'http://passport.baidu.com/center',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
                }
    req = urllib2.Request(path,post_data,headers)
    rsp = urllib2.urlopen(req).read()
    #checkin_pattern = re.compile(r'<a style="float:right;margin-right: 12px;" href="(.*?)" target="_blank">')
    #checkin_result = checkin_pattern.search(rsp)
    itieba='http://tieba.baidu.com/f/like/mylike'
    rsp =  urllib2.urlopen(itieba).read().decode('gbk')
    
    checkin_pattern = re.compile(r'<tr><td><a href="(.*?)title="(.*?)">(.*?)</a></td><td>')
    checkin_result = checkin_pattern.findall(rsp)


   

    for item in checkin_result:
        print item[2]
       

        queryStr1 = 'http://tieba.baidu.com'+item[0]
        rsp =  urllib2.urlopen(queryStr1).read().decode('gbk')
       
        tbs_pattern = re.compile(r'PageData.tbs = "(.*?)";')
        tbs = tbs_pattern.findall(rsp)
        t=tbs[0]
        


        post=urllib.urlencode({'ie':'utf-8',
                                'kw':item[2].encode('utf8'),
                                'tbs':t.encode('utf8'),
                                })
        headers={
                'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:29.0) Gecko/20100101 Firefox/29.0',
                'Accept':'application/json, text/javascript, */*; q=0.01',
                'Accept-Encoding':'gzip,deflate,sdch',
                'Accept-Language':'en-US,en;q=0.8',
                'Connection':'keep-alive',
                'Content-Length':'88',
                'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
                'Host':'tieba.baidu.com',
                'Origin':'http://tieba.baidu.com',
                'Referer':'http://tieba.baidu.com/f?kw=%BB%CA%BC%D2%C2%ED%B5%C2%C0%EF',
                'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
                'X-Requested-With':'XMLHttpRequest',
                }
        path='http://tieba.baidu.com/sign/add'
        req = urllib2.Request(path,post,headers)
        rsp = urllib2.urlopen(req).read()
        print 'DONE'



tieba()





