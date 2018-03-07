def main():
        infile = open("earthquake.txt",'r')     
        my_dic={}
        for line in infile:
                line=line.strip("\r\n")
                world=line.split(" ")
                
                if world[1] not in my_dic:
                        my_dic[world[1]]=[]
                        my_dic[world[1]].append(world[1])
                my_dic[world[1]].append(world[0])
                my_list = []
                for i in my_dic:
                        my_list.append(my_dic[i])
        print (my_list)
main()

