import xlwt
import requests
from lxml import etree
import time

all_info_list = []


def get_info(url):
    html = requests.get(url)
    selector = etree.HTML(html.text)

   
    infos = selector.xpath('/html/body/div[2]/em/div[1]/div[1]')

    for info in infos:
       
        title = info.xpath('div/div[2]/div[2]/a[1]/text()')[0]
    
        author = info.xpath('div/div[2]/div[1]/a/text()')[0]
        info_list = [title, author]
       
        all_info_list.append(info_list)


    time.sleep(1)

if __name__ == '__main__':
    url = ['http://book.zongheng.com/store.html']
    get_info(url)
    time.sleep(5)
   
    header = ['title', 'author']
   
    book = xlwt.Workbook(encoding='utf_8')
   
    sheet = book.add_sheet('Sheet')


    for h in range(len(header)):
       
        sheet.write(0, h, header[h])

    i = 1
   
    for list in all_info_list:
        j = 0
        for data in list:
            sheet.write(i, j, data)
            print(data)
            j += 1
        i += 1
    book.save('zhonghengxiaoshuo.xls')
