def main():

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
        "Potatoes (gr)":80,
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







                                                            #Entrees
        #Entrees Recipes
    red_rice = {
        "Rice (gr)": 300,
        "Tomato":2,
        "Onion": 0.25,
        "Garlic clove":1,
        "Oil (ml)": 50,
        "Water (ml)": 400,
        "":0,

    }

    white_rice={
        "Rice (gr)": 300,
        "Peas (gr)": 750,
        "Garlic clove":2,
        "Oil (ml)": 50,
        "Water (ml)": 400,
        "":0,

    }

    white_spaguetti ={
        "Pasta package":1,
        "Sour cream (ml)": 150,
        "Fin herbs (gr)":20,
        "Salt (gr)": 10,
        "Butter (gr)": 30,
        "Cheese (gr)": 150,
        "":0,

    }

    mac_cheese ={
        "Mac & Cheese package":1,
        "Water (ml)": 1440,
        "Milk (ml)": 60,
        "Butter (gr)": 60,
        "":0,

    }

    salad_sweet_apple = {
        "Apple":1,
        "Lettuce (gr)": 250,
        "Pecans (gr)":50,
        "Cranberries (gr)": 50,
        "Sunflower seeds (gr)":40,
        "Jicama (gr)":100,
        "":0,

    }

    chicken_rice_salad = {
        "Chicken breast (gr)": 1500,
        "Onion":0.125,
        "Garlic clove":1,
        "Salt (gr)": 10,
        "Rice (gr)":250,
        "Pinapple can 500 gr": 1,
        "Banana":2,
        "Olive oil (ml)":15,
        "Salt (gr)": 15,
        "Mint leaf":5,
        "":0,

    }

    potatoes_salad = {
        "Potatoes (gr)": 400,
        "Peas (gr)": 500,
        "Mayonaisse (gr)" : 100,
        "":0,

    }

    vegetables_broth = {
        "Carrot": 2,
        "Celery stick":1,
        "Onion": 1,
        "Leek":1,
        "Parlsey sprig":1,
        "Water (ml)":2000,
        "":0,

    }

    mashed_carrots = {
        "Carrot": 8,
        "Butter (gr)": 50,
        "Eggs":2,
        "Sour cream (ml)": 60,
        "Salt (gr)": 20,
        "Water (ml)":1000,
        "":0,

    }

    lettuce_cream={
        "Lettuce (gr)": 750,
        "Butter (gr)": 40,
        "Milk (ml)":500,
        "Potatoes (gr)": 100,
        "Salt (gr)": 20,
        "":0,

    }

    ENTREE = {
        "Red rice":red_rice,
        "White rice":white_rice,
        "White spaguetti":white_spaguetti,
        "Mac & Cheese": mac_cheese,
        "Apple sweet salad": salad_sweet_apple,
        "Chicken and Rice salad":chicken_rice_salad,
        "Potatoes salad":potatoes_salad,
        "Vegetable's broth":vegetables_broth,
        "Mashed carrots":mashed_carrots,
        "Lettuce cream": lettuce_cream,

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
        
        "Potatoes (gr)": 300,
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
        "Potatoes (gr)":250,
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
        "":0,

    }

    tuna_vegetables = {
        "Can of tuna": 2,
        "Can of vegetables":1,
        "Saladitas crackets package": 0.5,
        "Mayonaisse (gr)" : 50,
        "":0,

    }

    consome = {
        "Water (ml)":1500,
        "Beef meat (gr)":200,
        "Leek":1,
        "Carrot":1,
        "Parsley (gr)": 20,
        "Salt (gr)": 50,
        "Bread crust": 1,
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
        "Consome":consome,

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






                                                                #Desserts


    rice_milk = {
        "Rice (gr)": 120,
        "Cinnamon bars":0.5,
        "Water (ml)": 360,
        "Carnation can":0.25,
        "Lechera can":0.25,
        "":0,
    }

    jello ={
        "Jello box":0.25,
        "Water (ml)":250,
        "":0,

    }

    DESSERT={
        "Rice with milk":rice_milk,
        "Jello gelatine":jello,
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
        "Red rice":724,
        "White rice":260,
        "White spaguetti":394,
        "Mac & Cheese": 390,
        "Apple sweet salad": 245,
        "Rice with milk":555,
        "Jello gelatine":80,
        "Chicken and Rice salad":220,
        "Potatoes salad":360,
        "Vegetable's broth":20,
        "Mashed carrots":125,
        "Lettuce cream":45,
        "Consome":576,

    }






    """
                                                                    Functions
    """ 

    # Function: get_meal (name of recipes dictionary meal_type, input of user num_days)   Obtains and collects the recipes based on the numbers of the list provided and make them into a string.
    def get_meal(meal_type,num_days):
        counter= 0
        for x in meal_type:
            counter+=1
        
        if num_days<= counter:    
            meal_list = random.sample(list(meal_type),num_days)             #Cast typing of the dictionary meal_type into a list to work in the random.sample()
        else:
            meal_list = random.choices(list(meal_type), k=num_days)         #Cast typing of the dictionary meal_type into a list to work in the random.sample()

        return meal_list






    #Function: get_ingredients. Access all three meal types' recipes, decompose the ingredients and add them to the shop_list dictionary adding the new quantities for those inrgedients that repeat.
    def get_ingredients(meal_type1, meal_list1, meal_type2, meal_list2, meal_type3, meal_list3,meal_type4, meal_list4, meal_type5, meal_list5):   #Collects the ingredients of each recipe mentioned.
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


        for x in meal_list4:
            temporal = meal_type4.get(x)
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

        
        for x in meal_list5:
            temporal = meal_type5.get(x)
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
    def calories_count(meal_list1, meal_list2, meal_list3,meal_list4,meal_list5):
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

        for x in meal_list4:
            if x in calories.keys():                                        #if
                calories_total += calories.get(x)                           #Math Operation (Addition)

        for x in meal_list5:
            if x in calories.keys():                                        #if
                calories_total += calories.get(x)                           #Math Operation (Addition)

        return calories_total





    #Function save_menu (meal_list1, meal_list2, meal_list3) Save all the meals ordering them by days in numbers and returning them as a String.
    def save_menu(meal_list1, meal_list2, meal_list3,meal_list4,meal_list5,num_days):
        number = num_days
        menu = ""
        for x in range(1,number+1):
            calories_day = 0.0
            menu = menu + f"Day {x}\n    Breakfast:  {meal_list1[x-1]}\n    Entree:     {meal_list2[x-1]}\n    Lunch:      {meal_list3[x-1]}\n    Dinner:     {meal_list4[x-1]}\n    Dessert:    {meal_list5[x-1]}\n"

            if meal_list1[x-1] in calories.keys():                          #if
                calories_day += calories.get(meal_list1[x-1])               #Math Operation (Addition)

            if meal_list2[x-1] in calories.keys():                          #if
                calories_day += calories.get(meal_list2[x-1])               #Math Operation (Addition)

            if meal_list3[x-1] in calories.keys():                          #if
                calories_day += calories.get(meal_list3[x-1])               #Math Operation (Addition)

            if meal_list4[x-1] in calories.keys():                          #if
                calories_day += calories.get(meal_list4[x-1])               #Math Operation (Addition)

            if meal_list5[x-1] in calories.keys():                          #if
                calories_day += calories.get(meal_list4[x-1])               #Math Operation (Addition)

            menu= menu+ f"    Calories of the day: {calories_day}\n    \n"
        return menu






    #Function save_list (shop_list) Saves the shopping list in a stylish format and returns it as a String.
    def save_list(list):
        new_list = []                                                       #Creation of a list
        lista = ""
        for k,v in list.items():
            if k!=""and v!=0:                                               #if
                new_list.append(f"[ ] {k}: {v}\n")                          #Saving the ingredients from the dictionary list to the list new_list
        sorted_list = sorted(new_list)
        for x in sorted_list:
            lista=lista +x
        return lista






    """
                                                                User Interface
    """
    #Introduccion and input from the user to start the program.
    print("Welcome to the Meal Planner and Shopping List Generator.\nWould you like to get the meals of this week?")
    order = str(input("Please answer \"Yes\" or \"No\": "))

    if order == "Yes":                                             #if
        #Input of number of days to call the functions get meal from each category.
        num_days = int(input("Please enter the number of days you would like to receive a Meal Plan: "))

        meals_b =get_meal(BREAKFAST,num_days)
        meals_e =get_meal(ENTREE, num_days)
        meals_l =get_meal(LUNCH,num_days)
        meals_d =get_meal(DINNER,num_days)
        meals_dd=get_meal(DESSERT,num_days)

        menu_total_cal = calories_count(meals_b,meals_e,meals_l,meals_d,meals_dd)

        shoppy = get_ingredients(BREAKFAST, meals_b,ENTREE, meals_e,LUNCH,meals_l,DINNER,meals_d,DESSERT,meals_dd)
        
        listed = save_list(shoppy)
        menu = save_menu(meals_b,meals_e,meals_l,meals_d,meals_dd,num_days)
        
        result =f" El menu es {menu}\n The shopping list of this meal collection is:\n{listed}\n The total calories of this meal collection are: {menu_total_cal}\nThank you for using the program. Have a good day."





    else:                                                                   #else
        result ="Thank you for using the program. Have a good day."
        
    return result







"""
                                                            Use of the main() function
"""

printing_text = main()
print(printing_text)





"""
                                                            File creation and Experimentation
"""

file01=open("recipes.txt","wt")
file01.write(str(printing_text))
file01.close()






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