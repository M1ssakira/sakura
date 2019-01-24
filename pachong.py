

import requests
from pyquery import PyQuery as pq
# 抓取
# fangwen
# url 存
# 得到res
# 当下一页无下一页的时候


# init requests first
class zhihu_crawler():
    def __init__(self):
        self.header = dict()
        self.header['referer'] = 'www.zhihu.com'
        self.header['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:43.0) Gecko/20100101 Firefox/43.0'
        self.cookie = {
            'd_c0':'"ABDCxcmwUgyPTifK2O29PiJByYHgsg-MZNc=|1504487701"',
            '_zap':'c2afefb7-4556-40cd-9b84-87dd59dd496a',
            '__DAYU_PP':'YnUaMjeVaniivfI7jRqV29eee9abc51f',
            '_xsrf':'2K007YniiC4zsqDCt33aHQyYxQ3OS9Gr',
            'capsion_ticket':'"2|1:0|10:1546394992|14:capsion_ticket|44:YTM0YzZlZjE0ODk3NDJlZDlkNDcyM2Y3MjdmYTFjYWU=|3d063760e707c925d5db8eb263f0d3b7949a14af4c9f520c9e9cead964e7beae"',
            'z_c0':'"2|1:0|10:1546394993|4:z_c0|92:Mi4xZlJZekFBQUFBQUFBRU1MRnliQlNEQ1lBQUFCZ0FsVk5jV3NaWFFERmZfZ2hpMUhGVk54cTFhNV9TV2ZCVXhKM3Nn|ec2a0c994228760a3abb6ab9b20aec992ffc593aabeaaadb12a634a5c0af35b2"',
        'q_c1':'e100658d983b40e79a328adf3ebe1adc | 1547083866000 | 1533278495000',
        'tst':'f',
        'tgw_l7_route':'80f350dcd7c650b07bd7b485fcab5bf7'
        }

    def request_url(self):
        url = 'https://www.zhihu.com/people/zhuo-si-31/following'
        try:
            r = requests.get(url,headers=self.header,cookies=self.cookie)
            if r.status_code == 200:
                print ('---> success')
                print (r.text)
                return r.text
            else:
                print ('status code ',r.status_code)
        except BaseException as e:
            print ('--->',e)

    def parser_html(self,text):
        urls = list()
        doc = pq(text)
        items=doc('.List-item').items()
        for item in items:
            cls=item('.UserLink-link')
            print ('urls.append({})'.format(cls.attr.href))
            urls.append(cls.attr.href)


        print (len(urls))
        return urls


#存储

if __name__ == '__main__':
    pachong = zhihu_crawler()
    res = pachong.request_url()
    urls = pachong.parser_html(res)
    gg
