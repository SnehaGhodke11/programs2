usernm=input("Enter User Name:")

pass1=(input("Enter Password:"))

if usernm.strip()=="admin" and pass1.strip()=="1234":
    print("Welcome Admin")
else:
    print("Try Again")