# แปลง Case (เขียนโปรแกรมที่รับประโยคภาษาอังกฤษ แล้วสลับตัวพิมพ์เล็กเป็นพิมพ์ใหญ่ และพิมพ์ใหญ่เป็นพิมพ์เล็ก เช่น "HeLLo" -> "hEllO"
text_str=input("Type your sentense: ") #รับการป้อนค่า
text_convert = text_str.swapcase()
print(f" {text_convert}")