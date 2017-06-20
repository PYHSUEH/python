# -*- coding: utf-8 -*-
import urllib.request

import ssl

url1='https://downsub.com/?url=https://www.youtube.com/watch?v=Ej1hlQgwXcA'

print (url1)


response = urllib.request.urlopen(url1)
print(response.read().decode('utf-8'))
