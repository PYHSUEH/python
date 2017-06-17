# -*- coding: utf-8 -*-
import urllib.request

import ssl

#yang bin
url='https://www.youtube.com/channel/UCXT1lD9WEUAEO4KNSZFVniw/playlists?flow=grid&view=1'
#msabcroo
url2='https://www.youtube.com/user/ruthcoffeeshop/playlists?flow=grid&view=1'

def getHtml(url):
   context = ssl._create_unverified_context()
   page=urllib.request.urlopen(url,context=context)
   html=page.read().decode(encoding='utf-8',errors='strict')
   return html
#print(getHtml(url))

#url
text = getHtml(url)




#catch first title
title = text.find(r'dir="ltr" title="')
last = text[title+17:].find(r'"')

#print (title)
#print (last)

str = text[title+17:title+17+last]

#catch first link
text_1 = text[title+17+last:]
title2_1 = text_1.find(r'href="')
last2_1 = text_1[title2_1+6:].find(r'">')

#print (title2_1)
#print (last2_1)

str_1 = text_1[title2_1+6:title2_1+6+last2_1]

print (str,str_1)

#next turn
num2 = title+17+last
text2 = text[num2:]

while text2.find(r'dir="ltr" title="') != -1:
   #catch title
   title2 = text2.find(r'dir="ltr" title="')
   last2 = text2[title2+17:].find(r'"')
   str1 = text2[title2+17:title2+17+last2]



   #catch link
   text_1_2 = text2[title2+17+last2:]
   title2_1_2 = text_1_2.find(r'href="')
   last2_1_2 = text_1_2[title2_1_2+6:].find(r'">')

   str_1_2 = text_1_2[title2_1_2+6:title2_1_2+6+last2_1_2]



   print (str1,str_1_2)
   #next turn
   num2 = title2+17+last2
   text2 = text2[num2:]
