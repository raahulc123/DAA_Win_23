n=100000
fp = open("ascending_100000.txt","w")
fp.write(str(n)+" ")  
for i in range(1,n):
    fp.write(str(i)+" ")  
fp.write(str(n))
fp.close()
