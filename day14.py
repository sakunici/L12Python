# ตัวนับสระ: เขียนโปรแกรมที่รับประโยคภาษาอังกฤษ แล้วนับจำนวนสระ (a, e, i, o, u) ทั้งตัวพิมพ์เล็กและใหญ่

def count_vowels(sentence):
    vowels = "aeiou"
    vowel_count = 0
    
    for char in sentence:
        lower_char = char.lower()
        if lower_char in vowels:
            vowel_count += 1
            return vowel_count
        
user_input = input("Type your sentence: ")
total_vowels = count_vowels(user_input)

print(f"Your sentence is: \"{user_input}\" ")
print(f"Your vowels a, e, i, o, u in the sentence is: {total_vowels}")