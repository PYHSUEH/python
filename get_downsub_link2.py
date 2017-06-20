import urllib.request



def getHtml(url1):
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}  
    req = urllib.request.Request(url=url1, headers=headers)  
    text=urllib.request.urlopen(req).read().decode(encoding='utf-8',errors='strict')
    return text


def getValue(text1,str1,str2,str1_1,str2_1):

    a = []
    
    #print (page)
    #catch first title
    title = text1.find(str1)
    last = text1[title+len(str1):].find(str2)

    #print (title)
    #print (last)

    strq = text1[title:title+len(str1)+last]

    #catch first link
    text_1 = text1[title+len(str1)+last:]
    title2_1 = text_1.find(str1_1)
    last2_1 = text_1[title2_1+len(str1_1):].find(str2_1)

    #print (title2_1)
    #print (last2_1)

    str_1 = text_1[title2_1+len(str1_1):title2_1+len(str1_1)+last2_1]

    subtitle1=getHtml('https://downsub.com/'+strq)

    print (subtitle1)
    

    d = {'key1' : 'https://downsub.com/'+strq, 'key2' : str_1 , 'key3' : subtitle1}
    a.append(dict(d))


    #next turn
    num2 = title+len(str1)+last
    text2 = text[num2:]

    while text2.find(str1) != -1:
       #catch title
       title2 = text2.find(str1)
       last2 = text2[title2+len(str1):].find(str2)
       str1_q = text2[title2:title2+len(str1)+last2]



       #catch link
       text_1_2 = text2[title2+len(str1)+last2:]
       title2_1_2 = text_1_2.find(str1_1)
       last2_1_2 = text_1_2[title2_1_2+len(str1_1):].find(str2_1)

       str_1_2 = text_1_2[title2_1_2+len(str1_1):title2_1_2+len(str1_1)+last2_1_2]



       #d=d+{'key1' : str1, 'key2' : str_1_2 }
       #print (str1_q,str_1_2)


       subtitle2=getHtml('https://downsub.com/'+str1_q)


       d2={'key1':'https://downsub.com/'+str1_q, 'key2' : str_1_2, 'key3' : subtitle2}
       a.append(dict(d2))
       #next turn
       num21 = title2+len(str1)+last2
       text2 = text2[num21:]

    
    return a


 
url1='https://downsub.com/?url=https://www.youtube.com/watch?v=Ej1hlQgwXcA'

url2='https://downsub.com/?url=https://www.youtube.com/watch?v=A-QgGXbDyR0'

text = getHtml(url1)



d1=getValue(text,'index.php?','">>>','&nbsp;&nbsp;','<br>')

print(len(d1))

print (d1[0]["key2"])

print (d1[1]["key1"])
