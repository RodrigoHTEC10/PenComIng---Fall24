"""
                                                        Import section
"""
import random





"""
                                                        Data storing
"""
                                                        #Breakfasts
    #Breakfast Recipes
#Each recipe will be a dictionary
eggs_ham = {
    
    "Eggs":2,
    "Ham slides" : 2,
    "": 0,
}

eggs_spinach = {
    
    "Eggs": 2,
    "Spinach" : 100,
    "": 0,
}

hotcakes = {
    
    "Eggs": 2,
    "Milk (ml)": 350,
    "Hot cake mix": 2,
    "Butter (gr)": 30,
    "Maple syrup (ml)": 100,
    "": 0,
}

eggs_bacon ={
    "Eggs":2,
    "Bacon strips": 2,
    "": 0,
}

chicken_raft = {
    
    "Eggs": 2,
    "Slice of bread":2,
    "Avocado": 1,
    "": 0,
}

eggs_tortilla = {
    "Eggs": 2,
    "Tortillas (gr)": 50,
    "Oil (ml)": 10,
    "Salt (gr)": 0.2,
    "":0,
}

french_toast = {
    
    "Eggs":2,
    "Slice of bread":2,
    "Cinnamon ground":1,
    "Maple syrup (ml)": 100,
    "Butter (gr)": 30,
    "": 0,
    
}

breakfast_tacos = {
    "Eggs": 3,
    "Milk (ml)": 175,
    "Hot cake mix": 1,
    "Butter (gr)": 15,
    "Maple syrup (ml)": 100,
    "Ham slides":2,
    "": 0,
}

eggs_potatoes = {
    "Eggs":2,
    "Potatoes":2,
    "Oil (ml)": 20,
    "": 0,
}

# All recipes are collected on a dictionary, in this particular case Breakfast
BREAKFAST = {
    "Eggs with ham" : eggs_ham,
    "Eggs with spinach" : eggs_spinach,
    "Hotcakes": hotcakes,
    "Eggs with bacon": eggs_bacon,
    "Chicken on a raft": chicken_raft,
    "French toast": french_toast,
    "Eggs with tortilla": eggs_tortilla,
    "Breakfast tacos":breakfast_tacos,
    "Eggs with potatoes":eggs_potatoes,
}





                                                         #Lunches
    #Lunches Recipes
hamburger = {
    
    "Burger patty":1,
    "Burger bun": 1,
    "Tomato" : 1,
    "American cheese":1,
    "Ketchup (gr)": 100,
    "Mayonaisse (gr)" : 50,
    "Mustard (gr)" : 50,
    "": 0,
    
}

steak_veggy = {
    
    "Beef steak": 2,
    "Carrot": 2,
    "Zuccini": 2,
    "Oil (ml)": 50,
    "Salt (gr)": 5,
    "": 0,
}

steak_onion = {
    
    "Beef steak": 2,
    "Onion": 1,
    "": 0,
}

papas_chorizo = {
    
    "Potatoes": 10,
    "Chorizo (gr)": 250,
    "Sour cream (ml)": 100,
    "Cheese (gr)": 150,
    "Bolillo": 1,
    "": 0,
}

hotdogs = {
    
    "Hotdog buns":2,
    "Sausage": 2,
    "Bacon strips": 2,
    "Ketchup (gr)": 100,
    "Mayonaisse (gr)" : 50,
    "Mustard (gr)" : 50,
    "": 0,
    
}

tortitas_tuna = {
    "Eggs":2,
    "Can of tuna": 2,
    "Potatoes":6,
    "":0,


}

enchilada_verde = {

    "Tortillas (gr)":100,
    "Chicken breast (gr)": 700,
    "Sour cream (ml)": 150,
    "Cheese (gr)": 250,
    "Onion": 0.5,
    "Tomatillos": 10,
    "Garlic clove":1,
    "Green chile":1,
    "Cilantro (gr)": 50,
    "Oil (ml)": 50,
    "Salt (gr)": 50,
    "Baking soda (gr)": 20, 

}

tuna_vegetables = {
    "Can of tuna": 2,
    "Can of vegetables":1,
    "Saladitas crackets package": 0.5,
    "Mayonaisse (gr)" : 50,
    "":0,

}

LUNCH = {
    "Hamburger": hamburger,
    "Steak with vegetables": steak_veggy,
    "Steak with onion": steak_onion,
    "Potatoes with chorizo": papas_chorizo,
    "Hotdogs" : hotdogs,
    "Little tuna tortas": tortitas_tuna,
    "Green enchiladas":enchilada_verde,
    "Tuna with vegetables":tuna_vegetables,
}



                                                            #Dinners
    #Dinner Recipes
molletes = {
    "Cheese (gr)": 200,
    "Bolillo":1,
    "Can of beans": 1,
    "": 0,
}

quesadillas = {
    "Cheese (gr)": 300,
    "Flour tortillas": 3,
    "": 0,
}

cereal = {
   
    "Milk (ml)": 250,
    "Cereal (gr)": 60,
    "": 0,
}

frijoles_chorizo = {
   
    "Chorizo (gr)" : 250,
    "Can of beans" : 1,
    "": 0,
}

nopales_sombrero = {
    "Cheese (gr)": 150,
    "Nopales": 2,
    "Chorizo (gr)" : 250,
    "Can of beans" : 1,
    "Lechuga (gr)": 100,
    "": 0,
}




DINNER = {
    "Molletes": molletes,
    "Quesadillas": quesadillas,
    "Cereal": cereal,
    "Beans with chorizo": frijoles_chorizo,
    "Nopales with hat": nopales_sombrero,
}



                                                            #Calories
calories = {
    "Eggs with ham": 291,
    "Eggs with spinach": 212,
    "Hotcakes": 531,
    "Eggs with bacon": 186,
    "Hamburger": 330,
    "Steak with vegetables": 258,
    "Steak with onion": 198,
    "Molletes": 510,
    "Quesadillas": 693,
    "Potatoes with chorizo": 302,
    "Cereal": 420,
    "Beans with chorizo":334,
    "Nopales with hat": 378,
    "Chicken on a raft": 210,
    "Hotdogs" : 468,
    "French toast": 356,
    "Little tuna tortas":592,
    "Eggs with tortilla":395,
    "Breakfast tacos": 930,
    "Green enchiladas": 1018,
    "Eggs with potatoes":378,
    "Tuna with vegetables":115,



}



"""
                                                                Functions
""" 
# Function: get_meal (name of recipes dictionary meal_type, input of user num_days)   Obtains and collects the recipes based on the numbers of the list provided and make them into a string.
def get_meal(meal_type,num_days):    
    meal_list = random.choices(list(meal_type), k = num_days)
    return meal_list




#Function: get_ingredients. Access all three meal types' recipes, decompose the ingredients and add them to the shop_list dictionary adding the new quantities for those inrgedients that repeat.
def get_ingredients(meal_type1, meal_list1, meal_type2, meal_list2, meal_type3, meal_list3):   #Collects the ingredients of each recipe mentioned.
    shop_list = {}
    
    for x in meal_list1:
        temporal = meal_type1.get(x)
        is_new = False
        for y in temporal.keys():
            if y in shop_list and is_new == True:                       #if
                is_new = False

            elif y in shop_list and is_new == False:                    #elif
                quantity = shop_list.get(y)
                new_quantity = temporal.get(y)
                shop_list.update({y: quantity+new_quantity})            #Math Operation (Addition)

            else:                                                       #else
                new_quantity = temporal.get(y)                          
                shop_list.update({y:new_quantity})
                is_new = True

      
    for x in meal_list2:
        temporal = meal_type2.get(x)
        is_new = False  
        for y in temporal.keys():
            if y in shop_list and is_new == True:                       #if
                is_new = False

            elif y in shop_list and is_new == False:                    #elif
                quantity = shop_list.get(y)
                new_quantity = temporal.get(y)
                shop_list.update({y: quantity+new_quantity})            #Math Operation (Addition)

            else:                                                       #else
                new_quantity = temporal.get(y)
                shop_list.update({y:new_quantity})
                is_new = True

    
    for x in meal_list3:
        temporal = meal_type3.get(x)
        is_new = False
        for y in temporal.keys():
            if y in shop_list and is_new == True:                       #if
                is_new = False

            elif y in shop_list and is_new == False:                    #elif
                quantity = shop_list.get(y)
                new_quantity = temporal.get(y)
                shop_list.update({y: quantity+new_quantity})            #Math Operation (Addition)
                is_new = False

            else:                                                       #else
                new_quantity = temporal.get(y)
                shop_list.update({y:new_quantity})
                is_new = True

    is_new=False
    return shop_list



#Función calories_count (meal_list1, meal_list2, meal_list3). Looks for the recipes calories in the calories dictionary and gives a weekly addition of them.
def calories_count(meal_list1, meal_list2, meal_list3):
    calories_total = 0.0
    for x in meal_list1:
        if x in calories.keys():                                        #if
            calories_total += calories.get(x)                           #Math Operation (Addition)
    
    for x in meal_list2:
        if x in calories.keys():                                        #if
            calories_total += calories.get(x)                           #Math Operation (Addition)

    for x in meal_list3:
        if x in calories.keys():                                        #if
            calories_total += calories.get(x)                           #Math Operation (Addition)

    return calories_total




#Function print_menu (meal_list1, meal_list2, meal_list3) Print all the meals ordering them by days in numbers
def print_menu(meal_list1, meal_list2, meal_list3,num_days):
    number = num_days
    for x in range(1,number+1):
        calories_day = 0.0
        print(f"Day {x}")
        print(f"    Breakfast:  {meal_list1[x-1]}")
        print(f"    Lunch:      {meal_list2[x-1]}")
        print(f"    Dinner:     {meal_list3[x-1]}")

        if meal_list1[x-1] in calories.keys():                          #if
            calories_day += calories.get(meal_list1[x-1])               #Math Operation (Addition)

        if meal_list2[x-1] in calories.keys():                          #if
            calories_day += calories.get(meal_list2[x-1])               #Math Operation (Addition)

        if meal_list3[x-1] in calories.keys():                          #if
            calories_day += calories.get(meal_list3[x-1])               #Math Operation (Addition)

        print(f"    Calories of the day: {calories_day}")
        print(" ")




#Function print_list (shop_list) Prints the shopping list in a stylish format.
def print_list(list):
    new_list = []
    for k,v in list.items():
        if k!=""and v!=0:                                               #if
            new_list.append(f"[ ] {k}: {v}")
    sorted_list = sorted(new_list)
    for x in sorted_list:
        print(x)



"""
                                                            User Interface
"""
#Introduccion and input from the user to start the program.
print("Welcome to the Meal Planner and Shopping List Generator.\nWould you like to get the meals of this week?")
order = input("Please answer \"Yes\" or \"No\": ")
if order == "Yes" or "yes":                                             #if
    #Input of number of days to call the functions get meal from each category.
    num_days = int(input("Please enter the number of days you would like to receive a Meal Plan: "))
    meals_b =get_meal(BREAKFAST,num_days)
    meals_l =get_meal(LUNCH,num_days)
    meals_d =get_meal(DINNER,num_days)
    menu_total_cal = calories_count(meals_b,meals_l,meals_d)
    shoppy = get_ingredients(BREAKFAST, meals_b,LUNCH,meals_l,DINNER,meals_d)

    print_menu(meals_b,meals_l,meals_d,num_days)
    print("The shopping list of this week is:")
    print_list(shoppy)
    print(f"The total calories of this week are: {menu_total_cal}")
    
else:                                                                   #else
    print("Thank you for using the program. Have a good day.")





"""
                                                            Attempts and Trials
"""

"""
break_list = get_meal(Breakfast,2)
print(break_list)          #Practice of get_meal function.
for x in break_list:
    print(Breakfast.get(x))

print(f"Breakfasts of this week are {meals_b}.")
print(f"Lunches of this week are {meals_l}.")
print(f"Dinners of this week are {meals_d}.")

print(f"The breakfasts of the week are: {meals_b}")
print(f"The lunches of the week are: {meals_l}")
print(f"The dinners of the week are: {meals_d}")
"""