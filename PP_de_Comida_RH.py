def main():

    """
                                                            Import section
    """
    import random





    """
                                                            Data storing
    """
                                                            #Breakfasts


    # All recipes are collected on a dictionary, in this particular case Breakfast
    breakfast = {
        "Eggs with ham" : 
        {

        "Eggs":2,
        "Ham slides" : 2,
        "": 0,

        },

        "Eggs with spinach" : 
        {

        "Eggs": 2,
        "Spinach (gr)" : 100,
        "": 0,

        },

        "Hotcakes": 
        {

        "Eggs": 1,
        "Milk (ml)": 175,
        "Hot cake mix cup": 1,
        "Butter (gr)": 15,
        "Maple syrup (ml)": 100,
        "": 0,

        },

        "Eggs with bacon": 
        {

        "Eggs":2,
        "Bacon strips": 2,
        "": 0,

        },

        "Chicken on a raft": 
        {

        "Eggs": 2,
        "Slice of bread":2,
        "Avocado": 1,
        "": 0,

        },

        "French toast": 
        {

        "Eggs":2,
        "Slice of bread":2,
        "Cinnamon ground":1,
        "Maple syrup (ml)": 100,
        "Butter (gr)": 30,
        "": 0,    

        },

        "Eggs with tortilla": 
        {

        "Eggs": 2,
        "Tortillas (gr)": 50,
        "Oil (ml)": 10,
        "Salt (gr)": 0.2,
        "":0,

        },

        "Breakfast tacos":
        {

        "Eggs": 1,
        "Milk (ml)": 175,
        "Hot cake mix cup": 1,
        "Butter (gr)": 15,
        "Maple syrup (ml)": 100,
        "Ham slides":2,
        "": 0,

        },

        "Eggs with potatoes":
        {

        "Eggs":2,
        "Potatoes (gr)":80,
        "Oil (ml)": 20,
        "": 0,

        },

        "Eggs with sausage":
        {
        
        "Eggs":2,
        "Sausage": 1,
        "": 0,

        },

        "Eggs with beans":
        {
        
        "Eggs":2,
        "Can of beans": 0.25,

        }


    }




                                                #Entrees

    entree = {
        "Red rice":{

        "Rice (gr)": 150,
        "Tomato":1,
        "Onion": 0.25,
        "Garlic clove":0.25,
        "Oil (ml)": 12.5,
        "Water (ml)": 200,
        "":0,

        },

        "White rice":
        {

        "Rice (gr)": 150,
        "Peas (gr)": 375,
        "Garlic clove":1,
        "Oil (ml)": 25,
        "Water (ml)": 200,
        "":0,

        },

        "White spaguetti":
        {

        "Pasta package":0.5,
        "Sour cream (ml)": 75,
        "Fin herbs (gr)":10,
        "Salt (gr)": 5,
        "Butter (gr)": 15,
        "Cheese (gr)": 75,
        "":0,

        },

        "Mac & Cheese":
        {

        "Mac & Cheese package":0.25,
        "Water (ml)": 360,
        "Milk (ml)": 15,
        "Butter (gr)": 15,
        "":0,

        },

        "Apple sweet salad":
        {

        "Apple":1,
        "Lettuce (gr)": 250,
        "Pecans (gr)":25,
        "Cranberries (gr)": 25,
        "Sunflower seeds (gr)":20,
        "Jicama (gr)":100,
        "":0,

        },

        "Chicken and Rice salad":
        {

        "Chicken breast (gr)": 500,
        "Onion":0.125,
        "Garlic clove":1,
        "Salt (gr)": 10,
        "Rice (gr)":50,
        "Pinapple can 500 gr": 0.25,
        "Banana":0.75,
        "Olive oil (ml)":5,
        "Salt (gr)": 5,
        "Mint leaf":2,
        "":0,

        },

        "Potatoes salad":
        {

        "Potatoes (gr)": 200,
        "Peas (gr)": 250,
        "Mayonaisse (gr)" : 50,
        "":0,

        },

        "Vegetable's broth":
        {

        "Carrot": 2,
        "Celery stick":1,
        "Onion": 1,
        "Leek":1,
        "Parlsey sprig":1,
        "Water (ml)":1000,
        "":0,

        },

        "Mashed carrots":
        {

        "Carrot": 4,
        "Butter (gr)": 25,
        "Eggs":1,
        "Sour cream (ml)": 30,
        "Salt (gr)": 10,
        "Water (ml)":500,
        "":0,

        },

        "Lettuce cream": 
        {

        "Lettuce (gr)": 325,
        "Butter (gr)": 20,
        "Milk (ml)":250,
        "Potatoes (gr)": 50,
        "Salt (gr)": 10,
        "":0,

        },

        "Vegetable's soup":
        {
        
        "Small frozen vegetables package":0.5,
        "Tomato" : 1,
        "Onion": 0.125,
        "Garlic clove":0.5,
        "Water (ml)":250,
        "Salt (gr)": 15,

        },

        "Grilled asparagus":
        {
        
        "Asparagus (gr)":200,
        "Butter (gr)": 25,
        "Salt (gr)": 20,

        },

        "Grilled Nopales":
        {
        
        "Nopales": 2,
        "Salt (gr)": 20,

        }

    }






                                                            #Lunches
        #Lunches Recipes

    lunch = {
        "Hamburger": 
        {

        "Burger patty":1,
        "Burger bun": 1,
        "Tomato" : 1,
        "American cheese slices":1,
        "Ketchup (gr)": 100,
        "Mayonaisse (gr)" : 50,
        "Mustard (gr)" : 50,
        "": 0,

        },

        "Steak with vegetables": 
        {

        "Beef steak": 2,
        "Carrot": 1,
        "Zuccini": 1,
        "Oil (ml)": 25,
        "Salt (gr)": 5,
        "": 0,

        },

        "Steak with onion": 
        {

        "Beef steak": 2,
        "Onion": 1,
        "": 0,

        },

        "Potatoes with chorizo": 
        {

        "Potatoes (gr)": 300,
        "Chorizo (gr)": 250,
        "Sour cream (ml)": 100,
        "Cheese (gr)": 150,
        "Bolillo": 1,
        "": 0,

        },

        "Hotdogs" : 
        {

        "Hotdog buns":2,
        "Sausage": 2,
        "Bacon strips": 2,
        "Ketchup (gr)": 100,
        "Mayonaisse (gr)" : 50,
        "Mustard (gr)" : 50,
        "": 0,

        },

        "Little tuna tortas": 
        {

        "Eggs":2,
        "Can of tuna": 2,
        "Potatoes (gr)":250,
        "":0,

        },

        "Green enchiladas":
        {

        "Tortillas (gr)":100,
        "Chicken breast (gr)": 350,
        "Sour cream (ml)": 75,
        "Cheese (gr)": 125,
        "Onion": 0.25,
        "Tomatillos": 5,
        "Garlic clove":0.5,
        "Green chile":0.5,
        "Cilantro (gr)": 25,
        "Oil (ml)": 25,
        "Salt (gr)": 25,
        "Baking soda (gr)": 10, 
        "":0,

        },

        "Tuna with vegetables":
        {

        "Can of tuna": 2,
        "Can of vegetables":1,
        "Saladitas crackets package": 0.5,
        "Mayonaisse (gr)" : 50,
        "":0,

        },

        "Consome":
        {

        "Water (ml)":1500,
        "Beef meat (gr)":200,
        "Leek":1,
        "Carrot":1,
        "Parsley (gr)": 20,
        "Salt (gr)": 50,
        "Bread crust": 1,
        "":0,

        },

        "Grilled chicken":
        {
        
        "Chicken breast (gr)": 200,
        "Oil (ml)": 25,
        "Seasoning sheet":2,

        },

        "Chicharron and Guacamole tacos":
        {

        "Chicharron (gr)":150,
        "Avocado": 1,
        "Tomato" : 0.25,
        "Onion": 0.25,
        "Garlic":0.125,
        "Lime":1,
        "Salt (gr)": 50,
        "Tortillas (gr)":80,

        },

    }






                                                                #Dinners
        #Dinner Recipes


    dinner = {
        "Molletes": 
        {

        "Cheese (gr)": 300,
        "Bolillo":2,
        "Can of beans": 0.5,
        "": 0,

        },

        "Quesadillas": 
        {

        "Cheese (gr)": 300,
        "Flour tortillas": 3,
        "": 0,

        },

        "Cereal": 
        {

        "Milk (ml)": 250,
        "Cereal (gr)": 60,
        "": 0,

        },

        "Beans with chorizo": 
        {

        "Chorizo (gr)" : 125,
        "Can of beans" : 0.5,
        "": 0,

        },

        "Nopales with hat": 
        {

        "Cheese (gr)": 150,
        "Nopales": 2,
        "Chorizo (gr)" : 250,
        "Can of beans" : 1,
        "Lechuga (gr)": 100,
        "": 0,

        },

        "Homemade Pizza":
        {
        
        "Flour tortillas": 2,
        "Pizza sauce (ml)": 100,
        "Cheese (gr)": 300,
        "Pepperoni slices": 10,

        },

        "Sincronizadas": 
        {

        "Cheese (gr)": 200,
        "Flour tortillas": 4,
        "Ham slides" : 2,
        "American cheese slices":2,
        "": 0,

        },
    }






                                                                #Desserts



    dessert={
        "Rice with milk":
        {

        "Rice (gr)": 120,
        "Cinnamon bars":0.5,
        "Water (ml)": 360,
        "Carnation can":0.25,
        "Lechera can":0.25,
        "":0,

        },

        "Jello gelatine":
        {

        "Jello box":0.25,
        "Water (ml)":250,
        "":0,

        },

        "Peanut butter cookies":
        {
        
        "Peanut butter (gr)": 60,
        "Sugar (gr)":60,
        "Chocolate chips (gr)":30,
        "Eggs": 0.25,
        "Baking soda (gr)":5,
        "":0,

        },

        "Cake slice":
        {

        "Cake":0.125,
        "":0,

        },

        "Sweet bread":
        {
        
        "Sweet bread (personal choice)":1,
        "":0,

        },

        "Skip Dessert":
        {
        
        "":0,

        },
    }



                                                                #Calories

    calories= [
        ["Eggs with ham","Eggs with spinach","Hotcakes","Eggs with bacon","Hamburger","Steak with vegetables","Steak with onion","Molletes","Quesadillas","Potatoes with chorizo","Cereal","Beans with chorizo","Nopales with hat","Chicken on a raft","Hotdogs","French toast","Little tuna tortas","Eggs with tortilla","Breakfast tacos","Green enchiladas","Eggs with potatoes","Tuna with vegetables","Red rice","White rice","White spaguetti","Mac & Cheese","Apple sweet salad","Rice with milk","Jello gelatine","Chicken and Rice salad","Potatoes salad","Vegetable's broth","Mashed carrots","Lettuce cream","Consome","Eggs with sausage","Eggs with beans","Vegetable's soup","Grilled asparagus","Grilled Nopales","Grilled chicken","Chicharron and Guacamole tacos","Homemade Pizza","Sincronizadas","Peanut butter cookies","Cake slice","Sweet bread","Skip Dessert",],
        [291,212,531,186,330,258,198,510,693,302,420,334,378,210,468,356,592,395,930,1018,378,115,724,260,394,390,245,555,80,220,360,20,125,45,576,395,486,250,180,30,110,820,300,784,480,400,300,0]
    ]







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
            for i in range(len(calories[0])-1):
                if calories[0][i] == x:                                        #if
                    calories_total += calories[1][i]                           #Math Operation (Addition)
        
        for x in meal_list2:
            for i in range(len(calories[0])-1):
                if calories[0][i] == x:                                        #if
                    calories_total += calories[1][i] 

        for x in meal_list3:
            for i in range(len(calories[0])-1):
                if calories[0][i] == x:                                        #if
                    calories_total += calories[1][i]                           #Math Operation (Addition)

        for x in meal_list4:
            for i in range(len(calories[0])-1):
                if calories[0][i] == x:                                        #if
                    calories_total += calories[1][i]                           #Math Operation (Addition)

        for x in meal_list5:
            for i in range(len(calories[0])-1):
                if calories[0][i] == x:                                        #if
                    calories_total += calories[1][i]                            #Math Operation (Addition)

        return calories_total





    #Function save_menu (meal_list1, meal_list2, meal_list3) Save all the meals ordering them by days in numbers and returning them as a String.
    def save_menu(meal_list1, meal_list2, meal_list3,meal_list4,meal_list5,num_days):
        number = num_days
        menu = ""
        for x in range(1,number+1):
            calories_day = 0.0
            menu = menu + f"Day {x}\n    Breakfast:  {meal_list1[x-1]}\n    Entree:     {meal_list2[x-1]}\n    Lunch:      {meal_list3[x-1]}\n    Dinner:     {meal_list4[x-1]}\n    Dessert:    {meal_list5[x-1]}\n"

            for i in range(len(calories[0])-1):
                if meal_list1[x-1] == calories[0][i]:                                                                
                        calories_day += calories[1][i]

                if meal_list2[x-1] == calories[0][i]:                                                                
                        calories_day += calories[1][i]

                if meal_list3[x-1] == calories[0][i]:                                                                
                        calories_day += calories[1][i]

                if meal_list4[x-1] == calories[0][i]:                                                                
                        calories_day += calories[1][i]

                if meal_list5[x-1] == calories[0][i]:                                                                
                        calories_day += calories[1][i]       


            menu= menu+ f"    Calories of the day per person: {calories_day}\n    \n"
        return menu






    #Function save_list (shop_list) Saves the shopping list in a stylish format and returns it as a String.
    def save_list(list,num,days):
        new_list = []                                                       #Creation of a list
        lista = ""
        for k,v in list.items():
            if k!=""and v!=0:
                if k == "Water (ml)":
                    new_list.append(f"[ ] {k}: {v*num+(2000*days*num)}\n")                                               #if
                else:
                    new_list.append(f"[ ] {k}: {v*num}\n")                         #Saving the ingredients from the dictionary list to the list new_list

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
    order = order.lower()

    if order == "yes":                                          #if
        #Input of number of days to call the functions get meal from each category.
        num_days = int(input("Please enter the number of days you would like to receive a Meal Plan: "))
        portions = int(input("Please enter the number of people you will cook to during the week (Please count youself): "))

        meals_b =get_meal(breakfast,num_days)
        meals_e =get_meal(entree, num_days)
        meals_l =get_meal(lunch,num_days)
        meals_d =get_meal(dinner,num_days)
        meals_dd=get_meal(dessert,num_days)

        menu_total_cal = calories_count(meals_b,meals_e,meals_l,meals_d,meals_dd)

        shoppy = get_ingredients(breakfast, meals_b,entree, meals_e,lunch,meals_l,dinner,meals_d,dessert,meals_dd)
        
        listed = save_list(shoppy,portions,num_days)
        menu = save_menu(meals_b,meals_e,meals_l,meals_d,meals_dd,num_days)
        
        result =f" El menu es {menu}\n The shopping list of this meal collection is:\n{listed}\nThe total calories of this meal collection per person are: {menu_total_cal}\nNote: The program has added two liters of water for each person everyday\nThank you for using the program. Have a good day."





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