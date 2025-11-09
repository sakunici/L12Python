#ตัวนับคำ
text_str=input("Type your text: ")  #รับค่า
text=text_str.split()  #แยก String เป็น List ของคำ
word_count=len(text) #ใช้ฟังก์ชัน len() นับจำนวนคำ
print(f"Your sentense has {word_count} words")  #แสดงผลลัพธ์