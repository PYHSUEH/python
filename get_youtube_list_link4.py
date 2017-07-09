import urllib.request
import sqlite3
import time

def dbWord(word):
    word=word.replace("'","''")
    return word


def getHtml(url1):
    
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'}  
    req = urllib.request.Request(url=url1, headers=headers)  
    text=urllib.request.urlopen(req).read().decode(encoding='utf-8',errors='strict')
    return text


def getValue(text1,str1,str2,str1_1,str2_1):

    conn = sqlite3.connect('data.sqlite')

    print ('Opened database successfully')

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

    #print (subtitle1)
    

    d = {'key1' : 'https://downsub.com/'+strq, 'key2' : str_1 , 'key3' : subtitle1}
    a.append(dict(d))
    str_sqlite = "INSERT INTO data (input1,output1,output2) VALUES ('%s', '%s', '%s' )" %(dbWord(d["key1"]),dbWord(d["key2"]),dbWord(d["key3"]))
    print (str_sqlite)
    conn.execute(str_sqlite)
    conn.commit()

    #time.sleep( 1 )

    #next turn
    num2 = title+len(str1)+last
    text2 = text1[num2:]

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
       str_sqlite = "INSERT INTO data (input1,output1,output2) VALUES ('%s', '%s', '%s' )" %(dbWord(d2["key1"]),dbWord(d2["key2"]),dbWord(d2["key3"]))
       conn.execute(str_sqlite)
       conn.commit()

       #time.sleep( 1 )

       
       #next turn
       num21 = title2+len(str1)+last2
       text2 = text2[num21:]

    print ('Records created successfully')
    conn.close()
    return a

def getValue2(text1,str1,str2,str1_1,str2_1,title0):

    conn = sqlite3.connect('data.sqlite')

    print ('Opened database successfully')

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

    #print (subtitle1)
    

    d = {'key1' : 'https://downsub.com/'+strq, 'key2' : str_1 , 'key3' : subtitle1}
    a.append(dict(d))
    str_sqlite = "INSERT INTO data (input1,output1,output2) VALUES ('%s', '%s', '%s' )" %(dbWord(title0),dbWord(d["key2"]),dbWord(d["key3"]))
    print (str_sqlite)
    conn.execute(str_sqlite)
    conn.commit()

    #time.sleep( 1 )

    #next turn
    num2 = title+len(str1)+last
    text2 = text1[num2:]

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
       str_sqlite = "INSERT INTO data (input1,output1,output2) VALUES ('%s', '%s', '%s' )" %(dbWord(title0),dbWord(d2["key2"]),dbWord(d2["key3"]))
       conn.execute(str_sqlite)
       conn.commit()

       #time.sleep( 1 )

       
       #next turn
       num21 = title2+len(str1)+last2
       text2 = text2[num21:]

    print ('Records created successfully')
    conn.close()
    return a



def getValue3(text1,str1,str2,str1_1,str2_1):  #playlist retun list title 

#    conn = sqlite3.connect('data.sqlite')

#    print ('Opened database successfully')

    a = []
    
    #print (page)
    #catch first title
    title = text1.find(str1)
    last = text1[title+len(str1):].find(str2)

    #print (title)
    #print (last)

    strq = text1[title+len(str1):title+len(str1)+last]

    #catch first link
    text_1 = text1[title+len(str1)+last:]
    title2_1 = text_1.find(str1_1)
    last2_1 = text_1[title2_1+len(str1_1):].find(str2_1)

    #print (title2_1)
    #print (last2_1)

    str_1 = text_1[title2_1+len(str1_1):title2_1+len(str1_1)+last2_1]

#    subtitle1=getHtml('https://downsub.com/'+strq)

    #print (subtitle1)
    

    d = {'key1' : strq, 'key2' : str_1 }
    a.append(dict(d))
#    str_sqlite = "INSERT INTO data (input1,output1,output2) VALUES ('%s', '%s', '%s' )" %(dbWord(title0),dbWord(d["key2"]),dbWord(d["key3"]))
#    print (str_sqlite)
#    conn.execute(str_sqlite)
#    conn.commit()

    #time.sleep( 1 )

    #next turn
    num2 = title+len(str1)+last
    text2 = text1[num2:]

    while text2.find(str1) != -1:
       #catch title
       title2 = text2.find(str1)
       last2 = text2[title2+len(str1):].find(str2)
       str1_q = text2[title2+len(str1):title2+len(str1)+last2]



       #catch link
       text_1_2 = text2[title2+len(str1)+last2:]
       title2_1_2 = text_1_2.find(str1_1)
       last2_1_2 = text_1_2[title2_1_2+len(str1_1):].find(str2_1)

       str_1_2 = text_1_2[title2_1_2+len(str1_1):title2_1_2+len(str1_1)+last2_1_2]



       #d=d+{'key1' : str1, 'key2' : str_1_2 }
       #print (str1_q,str_1_2)


#       subtitle2=getHtml('https://downsub.com/'+str1_q)


       d2={'key1':str1_q, 'key2' : str_1_2,}
       a.append(dict(d2))
#       str_sqlite = "INSERT INTO data (input1,output1,output2) VALUES ('%s', '%s', '%s' )" %(dbWord(title0),dbWord(d2["key2"]),dbWord(d2["key3"]))
#       conn.execute(str_sqlite)
#       conn.commit()

       #time.sleep( 1 )

       
       #next turn
       num21 = title2+len(str1)+last2
       text2 = text2[num21:]

#    print ('Records created successfully')
#    conn.close()
    return a






def getHtmlAndGetValue(url0):
    text0 = getHtml(url0)
    
    first1 = url0.find('v=')
    title0 = url0[first1+2:]
    print (title0)
    d1=getValue2(text0,'index.php?','">>>','&nbsp;&nbsp;','<br>',title0)
    return d1
    
 
url1='https://downsub.com/?url=https://www.youtube.com/watch?v=Ej1hlQgwXcA'

url2='https://downsub.com/?url=https://www.youtube.com/watch?v=A-QgGXbDyR0'

url3='https://www.youtube.com/user/TEDEducation/playlists?view=1&flow=grid'

d1 = getHtml(url3)


d2=getValue3(d1,'dir="ltr" title="','"  aria-describedby="','href="','">')



for var in d2:
    print (var['key1'],var['key2'])

str1="https://www.youtube.com"+d2[0]['key2']
print (str1)
t1 = getHtml(str1)
d3=getValue3(t1,'spf-link " dir="ltr" href="','" data-sessionlink=','">\n      ','\n    </a>')

print (d3[0]['key2'])

t2 = getHtml(str1)
d4=getValue3(t2,'img data-ytimg="1" alt="" aria-hidden="true" src="','width="','src="','">')

#print(len(d1))

#print (d1[0]["key2"])

#print (d1[1]["key1"])
