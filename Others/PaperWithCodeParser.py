from bs4 import BeautifulSoup
import os
from translate_api import translator
# 提前打开网页并保存相关的页面为html文件
root = r"C:\Users\brisyramshere\Documents\xu.zhang\github\brisyramshere.github.io\Others"
html = r"view-source_https___paperswithcode.com_area_medical.html"
path = os.path.join(root, html)
bs = BeautifulSoup(open(path,encoding='utf-8'))

list = bs.body.find_all(attrs={'class':'col-xl-8 card-col card-col-title'})
for l in list:
    title = l.h1.contents[0]
    title_ch = translator(title)
    print(title+','+title_ch)

    
