def cook_book(file_):
   
    with open(file_, encoding="utf-8") as f:
        data = f.readlines()
        data.append("\n")
        dishes = {}
        recipe = []
        
        for i in data:
            if i != "\n":
                recipe.extend([i.strip()])
            elif i == "\n":
                dishes[recipe[0]] = []
                line = 2
                for i in range(int(recipe[1])):
                    ingr_list = recipe[line].split(" | ")
                    line += 1
                    dishes[recipe[0]].append({"ingredient_name": ingr_list[0], "quantity": int(ingr_list[1]), "measure": ingr_list[2]})
                recipe = []
        return dishes

def get_shop_list_by_dishes(dishes, person_count):

    dishes_all = cook_book("cook_book.txt")
    ingr_dict = {}

    for dish in dishes:
        if dish in dishes_all:
            for ingredient_dict in dishes_all[dish]:
                if ingredient_dict["ingredient_name"] not in ingr_dict:
                    ingr_dict[ingredient_dict["ingredient_name"]] = {"measure": ingredient_dict["measure"], "quantity": ingredient_dict["quantity"] * person_count}
                else:
                    ingr_dict[ingredient_dict["ingredient_name"]]["quantity"] += ingredient_dict["quantity"] * person_count
    return ingr_dict


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 15))
                

