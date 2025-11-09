#Palindrome
text_str=input("Type in English: ")
text=text_str.lower()
str_var1=text
str_var2=text[::-1]
if str_var1 == str_var2:
    print(f" Your text is Palindrome ")
else:
    print (f"Your text is not Palindrome")