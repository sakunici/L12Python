fruits_list = [ # create the list if you have more than 1 things
    {"fruit":"banana","price":60,"colour":"yellow"},
    {"fruit":"grape","price":80,"colour":"purple"},
    {"fruit":"orange","price":100,"colour":"orange"},
    {"fruit":"coconut","price":50,"colour":"green"},
    {"fruit":"cherry","price":500,"colour":"red"},
]
for fruit_data in fruits_list: # using For Loop to pick up one by one
    print(f" My favourite fruit is {fruit_data['fruit']}, it cost {fruit_data['price']} THB it is {fruit_data['colour']}") # order to pick up one by one with all data of each fruit

