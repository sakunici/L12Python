print("Welcome to the Menu x Budget Program")
import random
cheap_menu_list = ["Noodle","Krapao","Fried Rice","Panaeng",]
medium_menu_list = ["Pasta","Grilled Chicken","Burger","Shabu","Pizza","Shrimp Tom Yum"]

cheap_menu_choice=random.choice (cheap_menu_list)
medium_menu_choice =random.choice (medium_menu_list)
budget_str=input("How much is your budget today? (THB): ")
budget_int=int(budget_str)

if budget_int >= 300:
    print (f"You should eat: {medium_menu_choice}")
elif budget_int >= 80:
    print (f"You should eat: {cheap_menu_choice}")
else:
    print ("You don't have enough money, Go work and make money!")
