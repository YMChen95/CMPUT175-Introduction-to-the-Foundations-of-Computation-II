import urllib.request

url="https://www.cs.ualberta.ca/" 
page=urllib.request.urlopen(url)
pagetext=page.read().decode()
myDict={}
while '<a href="' in pagetext:
    link_start_index=pagetext.index('<a href="')+9
    link_end_index=pagetext.index('">',link_start_index)
    text_start_index=link_end_index+2
    text_end_index= pagetext.index('</a>',text_start_index)
    link=pagetext[link_start_index:link_end_index]
    text=pagetext[text_start_index:text_end_index]
    
    if text[0]!='<':
        myDict[link]=text
    pagetext=pagetext[text_end_index+5:]
list1=[]

for key in myDict:
    print(key,":",myDict[key])
#print(myDict)