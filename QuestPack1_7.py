#เซ็นเซอร์คำหยาบ
text_str=input("Type your sentense: ") #รับการป้อนค่า
text_lower=text_str.lower() #แปลง String ต้นฉบับเป็นพิมพ์เล็ก
sensor=["fuck","asshole","bitch"]  #คำที่ต้องการเซนเซอร์
text_to_censor = text_lower  #กำหนดให้ตัวแปรเซ็นเซอร์เริ่มต้นที่พิมพ์เล็ก
for sensor_word in sensor:
   text_to_censor = text_to_censor.replace(sensor_word, "***") #แทนที่คำหยาบพิมพ์เล็ก
print(f" Censored tex is {text_to_censor}") #แสดงผลลัพธ์สุดท้าย
