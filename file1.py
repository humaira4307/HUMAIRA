'''fileptr=open("file.txt","r")
if fileptr:
    print("open successfully")'''
fileptr=open("file.txt","a")
fileptr.write("welcome to bitm clg")
print(fileptr)
if fileptr:
    print("opened successfully")
fileptr.close()