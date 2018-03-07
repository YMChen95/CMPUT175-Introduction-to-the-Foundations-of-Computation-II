def main():
    attributes1 = []
    list1 = []
    list2 = []
    list3 = []
    attributes2 = []
    data2 = []
    #city_dict = {"YEG" : Edmonton , "YYC":Calgary , "YVR":Vancouver}
    f1 = open("hotels.data","r")
    #f2 = open("Restaurants.data","r")
    #attributes1 = f1.readline().rstrip("\n").split(";")
    for line1 in f1:
        data1=line1.rstrip("\n").split(";")
        if data1[0] == "YEG":
            list1.append(data1)
        elif data1[0] == "YYC":
            list2.append(data1)
        elif data1[0] == "YVR":
            list3.append(data1)
    
    #attributes2 = f2.readline().rstrip("\n").split(";")
    #for line2 in f2:
        #data2.append(line2.rstrip("\n").split(";"))
    for i  in range(len(list1)) :
        hotel_url = 'YEGhotel'+str(i)+'.htm'      
        try:
            f2=open(hotel_url,'w')
        except:
            print('error')
        f2.write('<html>')   
        f2.write('    <body>')   
        f2.write('      <h1>Query Results</h1>')   
        f2.write('      <h2>      From City:Edmonton</h2>')
        img_line="      <img src='"+list1[i][4]+"' />"
        f2.write(img_line)
        dis='      <h3>'+list1[i][6]+'</h3> '
        f2.write(dis)
        name='      <h3>'+"   "+'Hotel: '+list1[i][1]+'</h3> '
        price='      <h3>'+'Price per night: '+list1[i][3]+'</h3> '
        url='      <h3>'+'URl: '+'<a href="'+list1[i][5]+'">'+list1[i][5]+'</a>'+'</h3> '
        phone='      <h3>'+'Phone: '+list1[i][7]+'</h3> '
        address='      <h3>'+'Address: '+list1[i][6]+'</h3> '
        a = list1[i][2]
        m=int(a[0])
        n=int(a[2])        
        star1 = "<img src='star-full.png' />"*m
        if n !=0:
            star3 = "<img src='star-half.png' />"*1
            star2 = "<img src='star-empty.png' />"*(4-m)
        else:
            star3 = "<img src='star-half.png' />"*0
            star2 = "<img src='star-empty.png' />"*(5-m)
            
        star_full = ('       <td>'+star1+star3+star2+'</td>')
        review='      <h3>'+'Review: '+star_full+list1[i][2]+'</h3> '
            
        f2.write(name)
        f2.write(review)
        f2.write(price)
        f2.write(url)
        f2.write(phone)
        f2.write(address)
        f2.write('    </body>')
        f2.write('</html>')
        
    for i  in range(len(list2)) :
        hotel_url = 'YYChotel'+str(i)+'.htm'      
        try:
            f2=open(hotel_url,'w')
        except:
            print('error')
        f2.write('<html>')   
        f2.write('    <body>')   
        f2.write('      <h1>Query Results</h1>')   
        f2.write('      <h2>      From City:Calgary</h2>')
        img_line="      <img src='"+list2[i][4]+"' />"
        f2.write(img_line)
        dis='      <h3>'+list2[i][6]+'</h3> '
        f2.write(dis)
        name='      <h3>'+'Hotel: '+list2[i][1]+'</h3> '
        price='      <h3>'+'Price per night: '+list2[i][3]+'</h3> '
        url='      <h3>'+'URl: '+'<a href="'+list2[i][5]+'">'+list2[i][5]+'</a>'+'</h3> '
        phone='      <h3>'+'Phone: '+list2[i][7]+'</h3> '
        address='      <h3>'+'Address: '+list2[i][6]+'</h3> '
        a = list1[i][2]
        m=int(a[0])
        n=int(a[2])        
        star1 = "<img src='star-full.png' />"*m
        if n !=0:
            star3 = "<img src='star-half.png' />"*1
            star2 = "<img src='star-empty.png' />"*(4-m)
        else:
            star3 = "<img src='star-half.png' />"*0
            star2 = "<img src='star-empty.png' />"*(5-m)
                                       
        star_full = ('       <td>'+star1+star3+star2+'</td>')
        review='      <h3>'+'Review: '+star_full+list2[i][2]+'</h3> '        
        f2.write(name)
        f2.write(review)
        f2.write(price)
        f2.write(url)
        f2.write(phone)
        f2.write(address)
        f2.write('    </body>')
        f2.write('</html>')    
        
    f2=open("hotels.htm","w")
    f2.write('<html>')
    f2.write('    <body>')
    f2.write('      <h1>Query Results</h1>')
    f2.write('      <h3>From City: Calgary</h3>')
    f2.write('<table border="1" style="width:55%">')
    f2.write('   <tr>')
    f2.write('       <th>Hotel</th>')
    f2.write('       <th>Review</th>')
    f2.write('       <th>Price per night</th>')
    f2.write('       <th>Details</th>')
    f2.write('   </tr>')
    
    for i in range(len(list2)):
        f2.write('   <tr>')
        hotel1='       <td>'+list2[i][1]+'</td>'
        f2.write(hotel1)
        a = list2[i][2]
        m=int(a[0])
        n=int(a[2])
        star1 = "<img src='star-full.png' />"*m
        if n !=0:
            star3 = "<img src='star-half.png' />"*1
            star2 = "<img src='star-empty.png' />"*(4-m)
        else:
            star3 = "<img src='star-half.png' />"*0
            star2 = "<img src='star-empty.png' />"*(5-m)
        
        
        star_full = ('       <td>'+star1+star3+star2+'('+list2[i][2]+')'+'</td>')
        f2.write(star_full)
        price = '       <td>'+list2[i][3]+'</td>'
        f2.write(price)
        link = "<a href="+'YYChotel'+str(i)+'.htm'+">More...</a>"
        f2.write('       <td>'+link+'</td>')
        f2.write('   </tr>')
        
    f2.write('</table>')   
    f2.write('      <h3>From City: VAncouver</h3>')
    f2.write('<table border="1" style="width:65%">')
    f2.write('   <tr>')
    f2.write('       <th>Hotel</th>')
    f2.write('       <th>Review</th>')
    f2.write('       <th>Price per night</th>')
    f2.write('       <th>Details</th>')
    f2.write('   </tr>')
    for i in range(len(list1)):
        f2.write('   <tr>')
        hotel1='       <td>'+list1[i][1]+'</td>'
        f2.write(hotel1)
        a = list1[i][2]
        m=int(a[0])
        n=int(a[2])
        star1 = "<img src='star-full.png' />"*m
        if n !=0:
            star3 = "<img src='star-half.png' />"*1
            star2 = "<img src='star-empty.png' />"*(4-m)
        else:
            star3 = "<img src='star-half.png' />"*0
            star2 = "<img src='star-empty.png' />"*(5-m)
                
                
        star_full = ('       <td>'+star1+star3+star2+'('+list1[i][2]+')'+'</td>')
        f2.write(star_full)
        price = '       <td>'+list1[i][3]+'</td>'
        f2.write(price)
        link = "<a href="+'YEGhotel'+str(i)+'.htm'+">More...</a>"
        f2.write('       <td>'+link+'</td>')               
        f2.write('   </tr>')    
    f2.write('</table>')
    
    f2.write('    </body>')
    f2.write('</html>')   
    f1.close()
main()