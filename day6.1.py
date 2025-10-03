#Toiec Score to CEFR
toiec=int(input("Your Toic Score : "))
if toiec >=945:
    print("CEFR = C1")
elif toiec >=785:
    print("CEFR = B2")
elif toiec >=550:
    print("CEFR = B1")
elif toiec >=225:
    print("CEFR = A2")
elif toiec >=120:
    print("CEFR = A1")
else: 
    print("Keep Learning and Try Again")
