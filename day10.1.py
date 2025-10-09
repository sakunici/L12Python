import random
number_list=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
correct_number = random.choice(number_list)
guest=0
while guest != correct_number:
    guest_str = input("Enter the right number(1-20): ")
    guest = int(guest_str)
    if guest < correct_number:
        print("Too low, Try Again")
    elif guest > correct_number:
        print ("Too high Try Again")
print (f"Congratulations ! The correct number number was {correct_number}")
