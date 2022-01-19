import requests
from lxml import etree
import time
from send_email import send_email
from add_to_mysql import add_info
class Cst(object):

    def __init__(self):
        self.index = ['32178','36216','36217','36224','36227','36228','36273','36276','36202','36192']
        # self.url = "http://www.cst.zju.edu.cn/36216/list.htm"
        self.headers = {
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36'
        }
        self.idx = 2956

    def get_data(self, url):
        response = requests.get(url, headers=self.headers)
        with open('temp.html' ,'wb') as f:
            f.write(response.content)
        return response.content

    def parse_data(self, data):
        html = etree.HTML(data)
        title = html.xpath('//*[@id="wp_news_w15"]/div/ul/li[1]/span[1]/a/text()')[0]
        time = html.xpath('//*[@id="wp_news_w15"]/div/ul/li[1]/span[2]/text()')[0]
        url = "http://www.cst.zju.edu.cn/" + html.xpath('//*[@id="wp_news_w15"]/div/ul/li[1]/span[1]/a/@href')[0]
        return title + "***" + time + "***" + url

    def save_data(self, data, t):
        
        file_name = 'result.txt'
        with open(file_name, 'a') as f:
            f.write(str(data) + '\n')

        word = data.split("***")
        nums = word[1].split("-")
        num = nums[0] + nums[1] + nums[2]
        t = int(num)
        add_info(title=word[0], t=t,url=word[2],idx=self.idx)
        self.idx = self.idx + 1
        
    def run(self):
        last_h = -1
        last_title = ['','','','','','','','','',''] 
        while True:
            t = time.localtime(time.time())

            h = t.tm_hour
            m = t.tm_min
            if m == 10 and last_h != h:
                last_h = h
                for i,idx in enumerate(self.index):
                    data = self.get_data('http://www.cst.zju.edu.cn/' + idx + '/list.htm')
                    result = self.parse_data(data)
                    if last_title[i] != result:
                        last_title[i] = result
                        # send_email(last_title[i])
                        self.save_data(result,t)


if __name__ == '__main__':
    cst = Cst()
    cst.run()