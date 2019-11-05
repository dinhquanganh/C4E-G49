# #  EX1
# from youtube_dl import YoutubeDL
# #1: Tải 1 video
# dl = YoutubeDL()
# dl.download(['https://www.youtube.com/watch?v=i1IKnWDecwA']) 

# #2: Tải 1 audio
# options = {'format': 'bestaudio/audio'}
# dl = YoutubeDL(options)
# dl.download(['https://www.youtube.com/watch?v=z5Jc7KiTLbs'])

# #3: Tìm và tải video
# options = {
#     'default_search': 'ytsearch', 'max_downloads': 1 }
# dl = YoutubeDL(options)
# dl.download(['Có tất cả nhưng thiếu anh'])

# #4: Tìm và tải audio
# options = {'default_search': 'ytsearch','max_downloads': 1,'format': 'bestaudio/audio'}
# dl = YoutubeDL(options)
# dl.download(['Đi đu đưa đi'])

#
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
browser= webdriver.Chrome()
browser.get('https://music.apple.com/us/playlist/top-100-global/pl.d25f5d1181894928af76c85c967f8f31')
# e= browser.find_element_by_name('q')
# e.send_keys('python')
# e.send_keys(Keys.RETURN)

time.sleep(2)# doi trinh duyet load xong
kqua=browser.find_elements_by_xpath("//div[@class='product-hero__tracks']")
l=[]
for v in kqua:
   # print(v.text)
    try :
        d=  {'title':v.find_element_by_xpath('.//span').text,
            'tencs':v.find_element_by_xpath('.//a').get_attribute('href')}
        l.append(d)
        print()
        print()
    except Exception as ex:
        print(ex)
import xlwt
workbook = xlwt.Workbook('czo.xlsx')
worksheet = workbook.add_sheet('aaaa')
i=0
for n in l:
    i+=1
    worksheet.write(i,0,n)
# with open('result.json','wt',encoding='utf-8') as f:
#     import json
#     f.write(json.dumps(l,ensure_ascii=False))
# print(l)

# import xlwt

# x=1
# y=2
# z=3

# list1=[2.34,4.346,4.234]

# book = xlwt.Workbook(encoding="utf-8")

# sheet1 = book.add_sheet("Sheet 1")

# sheet1.write(0, 0, "Display")
# sheet1.write(1, 0, "Dominance")
# sheet1.write(2, 0, "Test")

# sheet1.write(0, 1, x)
# sheet1.write(1, 1, y)
# sheet1.write(2, 1, z)

# sheet1.write(4, 0, "Stimulus Time")
# sheet1.write(4, 1, "Reaction Time")

# i=4

# for n in list1:
#     i = i+1
#     sheet1.write(i, 0, n)



# book.save("trial.xls")
