a="""Lorem ipsum dolor sit amet,
consectetur adipiscingE elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.EEEE""" 

ecount=0
Ecount=0
for i in a:
    if i=="e":
        ecount+=1
    elif i=="E":
        Ecount+=1
        
print("e",ecount)
print("E",Ecount)