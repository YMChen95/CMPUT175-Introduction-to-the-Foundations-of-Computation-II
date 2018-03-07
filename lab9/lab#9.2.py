def main():

    list1 = []
    list2 = []
    list3 = []
    user_input=input("Enter file:")
    f1 = open(user_input,"r")

    for line1 in f1:
        data1=line1.rstrip("\n").split(";")
        if data1[0] == "YEG":
            list1.append(data1)
        elif data1[0] == "YYC":
            list2.append(data1)
        elif data1[0] == "YVR":
            list3.append(data1)
    list1.sort(key=lambda x: int(x[3][1:]))
    list2.sort(key=lambda x: int(x[3][1:]))
    list3.sort(key=lambda x: int(x[3][1:]))            
    print(list1)
        
    f2=open("output.htm","w")
    
    f2.write('<html>')
    f2.write('    <body>')
    f2.write('      <h1>Query Results</h1>')
    f2.write('      <h3>From City: Calgary</h3>')
    f2.write('<table border="1" style="width:55%">')
    f2.write('   <tr>')
    f2.write('       <th>Restaurants</th>')
    f2.write('       <th>Review</th>')
    f2.write('       <th>Price</th>')
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
    f2.write('      <h3>From City: Edmonton</h3>')
    f2.write('<table border="1" style="width:65%">')
    f2.write('   <tr>')
    f2.write('       <th>Restaurants</th>')
    f2.write('       <th>Review</th>')
    f2.write('       <th>Price</th>')
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
    
    f2.write('</table>')   
    f2.write('      <h3>From City: Vancouver</h3>')
    f2.write('<table border="1" style="width:65%">')
    f2.write('   <tr>')
    f2.write('       <th>Restaurants</th>')
    f2.write('       <th>Review</th>')
    f2.write('       <th>Price</th>')
    f2.write('       <th>Details</th>')
    f2.write('   </tr>')
    for i in range(len(list3)):
        f2.write('   <tr>')
        hotel1='       <td>'+list3[i][1]+'</td>'
        f2.write(hotel1)
        a = list3[i][2]
        m=int(a[0])
        n=int(a[2])
        star1 = "<img src='star-full.png' />"*m
        if n !=0:
            star3 = "<img src='star-half.png' />"*1
            star2 = "<img src='star-empty.png' />"*(4-m)
        else:
            star3 = "<img src='star-half.png' />"*0
            star2 = "<img src='star-empty.png' />"*(5-m)
                    
                    
        star_full = ('       <td>'+star1+star3+star2+'('+list3[i][2]+')'+'</td>')
        f2.write(star_full)
        price = '       <td>'+list3[i][3]+'</td>'
        f2.write(price)
        link = "<a href="+'YVRrestaurant'+str(i)+'.htm'+">More...</a>"
        f2.write('       <td>'+link+'</td>')               
        f2.write('   </tr>')    
    f2.write('</table>')    
    f2.write('    </body>')
    f2.write('</html>')   
    f1.close()
main()