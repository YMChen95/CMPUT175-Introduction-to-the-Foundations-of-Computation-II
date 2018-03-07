isProgram = True
try:
        infile = open("rainfall.txt",'r')
except IOError:
        print('File does not exist')
        isProgram=False

name = []
one = []
two = []
three = []
four =[]
if isProgram==True:
        for line in infile: 
                name,number = line.split()
                if float(number) <= 70:
                        one.append("%25s"%(name))
                        one.append("%5.1f\n"%float(number))
                elif float(number) <= 80:
                        two.append("%25s"%name)
                        two.append("%5.1f\n"%float(number))
                elif float(number) <= 90:
                        three.append("%25s"%name)
                        three.append("%5.1f\n"%float(number))
                else:
                        four.append("%25s"%name)
                        four.append("%5.1f\n"%float(number))
outfile = open("rainfallfmt.txt",'w')
outfile.writelines("[60 --- 70]\n")
outfile.writelines(''.join(one))
outfile.writelines("[71 --- 80]\n")
outfile.writelines(''.join(two))
outfile.writelines("[81 --- 90]\n")
outfile.writelines(''.join(three))
outfile.writelines("[91 ---   ]\n")
outfile.writelines(''.join(four))
infile.close()
outfile.close()