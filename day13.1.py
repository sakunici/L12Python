# เขียนโปรแกรม "สมุดบันทึกอย่างง่าย" ให้ผู้ใช้พิมพ์ข้อความที่ต้องการบันทึก แล้วโปรแกรมจะนำข้อความนั้นไปต่อท้ายไฟล์ชื่อ my_journal.txt
entry_text = input("What do you want to write today?") # 1. รับข้อความที่ต้องการบันทึกจากผู้ใช้

with open("myjournal.txt", "a") as file: # 2. เปิดไฟล์ในโหมด "a" (append) เพื่อต่อท้าย
    file.write(entry_text + "\n") # เพิ่ม "\n" เพื่อให้ข้อความใหม่ขึ้นบรรทัดใหม่เสมอ

print("Your entry has been saved successfully!")