##delete all Simple_ files before running

##Q: does the "a" even matter if im processing all at once?

T1=open("t1.txt","w") #makes new file (even if old exists)
T2=open("t2.txt","w")
D1=open("d1.txt","w")
D2=open("d2.txt","w")
D3=open("d3.txt","w")

Simple_T1=open("simple_T1.txt","a")
Simple_T2=open("simple_T2.txt","a")
Simple_D1=open("simple_D1.txt","a")
Simple_D2=open("simple_D2.txt","a")
Simple_D3=open("simple_D3.txt","a")

read_from=open("rawData.txt","r")

file_handles=[T1,T2,D1,D2,D3,Simple_T1,Simple_T2,Simple_D1,Simple_D2,Simple_D3,read_from]

#data=read_from.readline()   ## for single line, testing purposes

for data in read_from.readlines(): ##For going through all lines, final version

        data_exp=data.split()

        length=len(data_exp)
        i=0

        while(i+2<length):
                if (data_exp[i]=="0:"):
                        middle=T2
                        if(i<=14):
                                Simple_T2.write(data_exp[i+2]) ##gets initial temperatures
                        if(data_exp[i+2]=="0.00"):              ##End time (reached 0 C)
                                Simple_T2.write(" ")
                                Simple_T2.write(data_exp[i+1])
                                Simple_T2.write("\n")
                                
                elif (data_exp[i]=="1:"):
                        middle=T1
                        if(i<=14):
                                Simple_T1.write(data_exp[i+2])
                        if(data_exp[i+2]=="0.00"):
                                print("fgdfg")
                                Simple_T1.write(" ")
                                Simple_T1.write(data_exp[i+1])
                                Simple_T1.write("\n")

                elif (data_exp[i]=="2:"):
                        middle=D2
                        if(i<=14):
                                Simple_D2.write(data_exp[i+2])
                        if(data_exp[i+2]=="0.00"):             
                                Simple_D2.write(" ")
                                Simple_D2.write(data_exp[i+1])
                                Simple_D2.write("\n")

                elif (data_exp[i]=="3:"):
                        middle=D3
                        if(i<=14):
                                Simple_D3.write(data_exp[i+2])
                        if(data_exp[i+2]=="0.00"):             
                                Simple_D3.write(" ")
                                Simple_D3.write(data_exp[i+1])
                                Simple_D3.write("\n")

                elif (data_exp[i]=="4:"):
                        middle=D1
                        if(i<=14):
                                Simple_D1.write(data_exp[i+2])
                        if(data_exp[i+2]=="0.00"):             
                                Simple_D1.write(" ")
                                Simple_D1.write(data_exp[i+1])
                                Simple_D1.write("\n")

                
                middle.write(data_exp[i+1])
                middle.write(" ")
                middle.write(data_exp[i+2])
                middle.write("\n")
                i+=3


        T1.write("-----------END---------\n")
        T2.write("-----------END---------\n")
        D1.write("-----------END---------\n")
        D2.write("-----------END---------\n")
        D3.write("-----------END---------\n") 

        print("done")
##T1.close()
##T2.close()
##D1.close()
##D2.close()
##D3.close()
##read_from.close()

for fil in file_handles:
        fil.close()



print("done2")



##To do:
##        add loop to go through all lines -------------- DONE AND TESTED
