def main():
    alist = []
    f = open("input.txt","r")
    maxium = 0
    minimum = 100
    average = 0
    number_people = 0
    total=0
    interval1=0
    interval2=0
    interval3=0
    interval4=0
    interval5=0
    interval6=0
    interval7=0
    interval8=0
    interval9=0
    interval10=0    
    for line in f:
        i_d,marks=line.split()
        if maxium < int(marks):
            maxium = int(marks)
        if minimum > int(marks):
            minimum = int(marks)
        number_people +=1
        total = total+int(marks)
        if int(marks)>=90:
            interval1+=1
        elif int(marks)>=80 and int(marks)<90:
            interval2+=1 
        elif int(marks)>=70 and int(marks)<80:
            interval3+=1 
        elif int(marks)>=60 and int(marks)<70:
            interval4+=1
        elif int(marks)>=50 and int(marks)<60:
            interval5+=1
        elif int(marks)>=40 and int(marks)<50:
            interval6+=1
        elif int(marks)>=30 and int(marks)<40:
            interval7+=1 
        elif int(marks)>=20 and int(marks)<30:
            interval8+=1 
        elif int(marks)>=10 and int(marks)<20:
            interval9+=1
        elif int(marks)>=0 and int(marks)<10:
            interval10+=1        
        
    average = total/number_people
    print(interval1)
    print(interval2)
    print(interval3)
    print(interval4)
    print(interval5)
    print(interval6)
    print(interval7)
    print(interval8)
    print(interval9)
    print(interval10)
    f2=open("output.htm","w")
    f2.write('<html>')
    f2.write('    <body>')
    f2.write('      <h1>Welcome to stastistics page</h1>')
    average='      <h4>Average:'+str(average)+'</h4>'
    f2.write(average)
    maxium='      <h4>Maximum:'+str(maxium)+'</h4>'
    f2.write(maxium)
    minimum='      <h4>Maximum:'+str(minimum)+'</h4>'
    f2.write(minimum)
    f2.write('<table>')
    f2.write('     <tr>') 
    
    interval1='<div style="width:10px;height:'+str(interval1*20)+'px;background:blue;border:1px solid red;"></div>'
    interval2='<div style="width:10px;height:'+str(interval2*20)+'px;background:blue;border:1px solid red;"></div>'
    interval3='<div style="width:10px;height:'+str(interval3*20)+'px;background:blue;border:1px solid red;"></div>'
    interval4='<div style="width:10px;height:'+str(interval4*20)+'px;background:blue;border:1px solid red;"></div>'
    interval5='<div style="width:10px;height:'+str(interval5*20)+'px;background:blue;border:1px solid red;"></div>'
    interval6='<div style="width:10px;height:'+str(interval6*20)+'px;background:blue;border:1px solid red;"></div>'
    interval7='<div style="width:10px;height:'+str(interval7*20)+'px;background:blue;border:1px solid red;"></div>'
    interval8='<div style="width:10px;height:'+str(interval8*20)+'px;background:blue;border:1px solid red;"></div>'
    interval9='<div style="width:10px;height:'+str(interval9*20)+'px;background:blue;border:1px solid red;"></div>'
    interval10='<div style="width:10px;height:'+str(interval10*20)+'px;background:blue;border:1px solid red;"></div>'
        
    f2.write('         <td valign="bottom">')
    f2.write(interval1)
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write(interval2)
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write(interval3)
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write(interval4)
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write(interval5)
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write(interval6)
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write(interval7)
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write(interval8)
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write(interval9)
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write(interval10)
    f2.write('         </td>')
    f2.write('     </tr>')
    f2.write('     <tr>')
    f2.write('         <td valign="bottom">')
    f2.write('            <h4>[0-9]</h4>')
    f2.write('         </td>')
    
    f2.write('         <td valign="bottom">')
    f2.write('            <h4>[10-19]</h4>')
    f2.write('         </td>')
    
    f2.write('         <td valign="bottom">')
    f2.write('            <h4>[20-29]</h4>')
    f2.write('         </td>')
    
    f2.write('         <td valign="bottom">')
    f2.write('            <h4>[30-39]</h4>')
    f2.write('         </td>')
    
    f2.write('         <td valign="bottom">')
    f2.write('            <h4>[40-49]</h4>')
    f2.write('         </td>')
    
    f2.write('         <td valign="bottom">')
    f2.write('            <h4>[50-59]</h4>')
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write('            <h4>[60-69]</h4>')
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write('            <h4>[70-79]</h4>')
    f2.write('         </td>')
        
    f2.write('         <td valign="bottom">')
    f2.write('            <h4>[80-89]</h4>')
        
    f2.write('         </td>')    
        
    f2.write('         <td valign="bottom">')
    f2.write('            <h4>[90-99]</h4>')
    f2.write('         </td>')    
    f2.write('     </tr>')
        
        
        
        
    f2.write('    </body>')
    f2.write('</html>')    
    f.close() 
        
main()