def menu_is_boring(meals):
    previous_meal=None
    for meal in meals:
        if meal == previous_meal:
            return True
        previous_meal=meal
    return False
meals_1=['Redneck Rids','Prawn Star','San Quentin Squid','Fist Full of Pizza','Honky Tonk Chicken']
meals_2=['Redneck Rids','Prawn Star','Running Bear Salmon','Running Bear Salmon','Honky Tonk Chicken']
is_boring=menu_is_boring(meals_1)
print(is_boring)
is_boring=menu_is_boring(meals_2)
print(is_boring)