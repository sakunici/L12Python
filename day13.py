# เขียนไฟล์
with open("diary.txt", "w") as file:
    file.write("Today I start learning writing in Python!")

# อ่านไฟล์
with open("diary.txt", "r") as file:
    content = file.read()
    print(content)
