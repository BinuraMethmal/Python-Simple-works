n=str(input("Enter your NIC number : "))

if len(n)==10:
    print("NIC Type : Old ")
    birth=n[:2]
    print("You were born on ",birth)
    
    g=n[2:5]
    
    g_int=int(g)
    #print(g_int)

    if g_int>000 and g_int<367:       
        print("You are a Male.")
        
    elif g_int>500 and g_int<867:
        print("You are a Female.")
         
    if (n[9]==("V")):
        print("You are a Voter.")
             
    elif (n[9]==("X")):
        print("You are a Non Voter.")
        
elif len(n)==12:
    print("NIC Type : New ")

    birth2=n[:4]
    print("You were Born on ",birth2)

    g2=n[4:7]  
    g2_int=int(g2)
    #print(g2_int)

    if g2_int>000 and g2_int<367:       
        print("You are a Male.")
        
    elif g2_int>500 and g2_int<867:
        print("You are a Female.")  
else:
    print("Invalid NIC number!")

    
