def cookbook():
    global cookbook
    cookbook = {}
    with open("recipes.txt") as file:
        for line in file:
            dish_name = line.strip()
            dish_ingredients = []
            ingredients_count = int(file.readline().strip())
            for el in range(ingredients_count):
                ingredient = file.readline().strip().split(' | ')
                cookbook_dish = {'ingredient_name': ingredient[0], 'quantity': ingredient[1], 'measure': ingredient[2]}
                dish_ingredients.append(cookbook_dish)
            file.readline()
            cookbook[dish_name] = dish_ingredients
    return cookbook

def get_shop_list_by_dishes(dishes, person_count):
    cookbook_keys = cookbook().keys()
    all_ingredients = {}
    for dish in dishes:
        if dish in cookbook_keys:
            ingredients = cookbook.get(dish)
            for ingredient in ingredients:
                if ingredient.get('ingredient_name') in all_ingredients.keys():
                    all_ingredients[ingredient.get('ingredient_name')] = {'quantity': (int(ingredient.get('quantity'))
                    + int(all_ingredients.get(ingredient.get('ingredient_name')).get('quantity') / 2)) * person_count,
                    'measure': ingredient.get('measure')}
                else:
                    all_ingredients[ingredient.get('ingredient_name')] = {'quantity': int(ingredient.get('quantity')) * int(person_count),
                    'measure': ingredient.get('measure')}
        else:
            return 'Неизвестное блюдо'
    return all_ingredients

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
