#นับจำนวนสระ (a, e, i, o, u) ทั้งตัวพิมพ์เล็กและใหญ่
yourtext_str=input("Type your text in English: ") #รับค่าประโยคภาษาอังกฤษ
text=yourtext_str.lower()
vovel_str=["a","e","i","o","u"]
count = 0
for letter_vovel_str in text:
    if letter_vovel_str in vovel_str:
        count = count + 1
print (f"You text have {count} vovel in total")

