import urllib2
import urllib
import urllib
import cookielib
import re
import HTMLParser



def tieba():
    username = 'xxxx'
    psw = 'xxxx'
    login_tokenStr = '''bdPass.api.params.login_token='(.*?)';'''
    login_tokenObj = re.compile(login_tokenStr,re.DOTALL)
    #cookiename = 'baidu%s.coockie' % (username)
    cj = cookielib.LWPCookieJar()
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

    headers = {'User-Agent' : 'Mozilla 5.10',
                "Accept-Language": "zh-cn",
                'charset':'UTF-8'}
    req = urllib2.Request(path,post_data,headers)
    rsp = urllib2.urlopen(req).read()
    #checkin_pattern = re.compile(r'<a style="float:right;margin-right: 12px;" href="(.*?)" target="_blank">')
    #checkin_result = checkin_pattern.search(rsp)
    itieba='http://tieba.baidu.com/f/like/mylike'
    rsp = opener.open(itieba).read().decode('gbk')
    
    tieba_pattern = re.compile(r'<tr><td><a href="(.*?)title="(.*?)">(.*?)</a></td><td>')
    tieba_result = checkin_pattern.findall(rsp)
  

    for item in tieba_result:
        print item[2]
tieba()