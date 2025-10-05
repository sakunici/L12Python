# Guest Verification
import random
guest_list = ["Manee", "Piti", "Choojai", "Mana"]

guest_choice=random.choice (guest_list)
guest_register_str=input("What is your name? : ")
guest_input=str(guest_register_str)

if guest_input in guest_list:
    guest_list.remove(guest_input)
    print(f"Welcome {guest_input}! you have been checked in.")
    print(f"Guest still waiting {guest_list}")
else:
    print(f"Sorry {guest_input}! you are not in the guest list.")



