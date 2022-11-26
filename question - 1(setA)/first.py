p = df["pep"].values.tolist()
c = 0
t = 0 
for val in pep: 
    if (val!="NO"):
        c=c+1
    t+=1 
per = (c/t)*100;
print("Percentage = ",per)
