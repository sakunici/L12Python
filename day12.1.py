text_input="    str123th  "
text_clean=text_input.strip()
print(f" '{text_clean}'")


phone_number = "099-888-9999"
# เราต้องการเก็บเบอร์โทรแบบไม่มีขีด
cleaned_phone = phone_number.replace("-", "") # แทนที่ "-" ด้วย "ความว่างเปล่า"

print(f"เบอร์โทรดั้งเดิม: {phone_number}")
print(f"เบอร์โทรที่จัดรูปแบบใหม่: {cleaned_phone}")

department="Department"
clean_dept=department.replace ("ment","ttt" )

print(f"Old text: {department}")
print(f"New text: {clean_dept}")