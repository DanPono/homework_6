import random
import string


class Ingredient:
    def __init__(self, name, amount, unit):
        self.name = name
        self.amount = amount
        self.unit = unit

    def __str__(self):
        return f"{self.name} | {self.amount} | {self.unit}"


class Recipe:
    def __init__(self, name, ingredients=None):
        self.name = name
        self.ingredients = ingredients or []

    def Add(self, ingredient):
        self.ingredients.append(ingredient)

    def __str__(self):
        return f"{self.name}\n{len(self.ingredients)}\n" + "\n".join(str(i) for i in self.ingredients)


class RecipeBook:
    def __init__(self, file_name):
        self.file_name = file_name
        self.recipes = {}

    def Add(self, recipe):
        ingredients_list = []
        for ingredient in recipe.ingredients:
            ingredients_list.append({
                'ingredient_name': ingredient.name,
                'quantity': ingredient.amount,
                'measure': ingredient.unit
            })
        self.recipes[recipe.name] = ingredients_list

    def read_recipes(self):
        with open(self.file_name, "r") as f:
            file_contents = f.read()
            recipes_str = file_contents.split("\n\n")
            for recipe_str in recipes_str:
                recipe_lines = recipe_str.split("\n")
                name = recipe_lines[0]
                n_ingredients = int(recipe_lines[1])
                ingredients = []
                for i in range(n_ingredients):
                    ingredient_str = recipe_lines[i + 2]
                    ingredientName, amount, unit = ingredient_str.split(" | ")
                    ingredients.append(Ingredient(ingredientName, float(amount), unit))
                recipe = Recipe(name, ingredients)
                self.Add(recipe)

    def __str__(self):
        return str(self.recipes)


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    recipesBook = RecipeBook("recipes.txt")
    recipesBook.read_recipes()
    for dish in dishes:
        for ingredient in recipesBook.recipes[dish]:
            name = ingredient['ingredient_name']
            measure = ingredient['measure']
            quantity = ingredient['quantity'] * person_count
            if name not in shop_list:
                shop_list[name] = {'measure': measure, 'quantity': quantity}
            else:
                shop_list[name]['quantity'] += quantity
    return shop_list



def Task1():
    recipesBook = RecipeBook("recipes.txt")
    r1 = Recipe("Омлет")
    r1.Add(Ingredient('яйцо', 2, 'шт'))
    r1.Add(Ingredient('Молоко', 100, 'мл'))
    r1.Add(Ingredient('Помидор', 2, 'шт'))
    r2 = Recipe("Утка по-пекински")
    r2.Add(Ingredient('Утка', 1, 'шт'))
    r2.Add(Ingredient('Вода', 2, 'л'))
    r2.Add(Ingredient('Мед', 3, 'ст.л.'))
    r3 = Recipe("Запеченный картофель")
    r3.Add(Ingredient('Картофель', 1, 'шт'))
    r3.Add(Ingredient('Чеснок', 3, 'шт'))
    r3.Add(Ingredient('Сыр гауда', 100, 'мл'))
    r4 = Recipe("Фахитос")
    r4.Add(Ingredient('Говядина', 500, 'г'))
    r4.Add(Ingredient('Перец сладкий', 1, 'шт'))
    r4.Add(Ingredient('Лаваш', 2, 'шт'))
    r4.Add(Ingredient('Винный уксус', 3, 'шт'))
    r4.Add(Ingredient('Помидор', 1, 'ст.л.'))

    recipesBook.Add(r1)
    recipesBook.Add(r2)
    recipesBook.Add(r3)
    recipesBook.Add(r4)
    print(recipesBook)


def Task2():
    print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


def merge_files():
    for i in range(1, 4):
        with open(f"file{i}.txt", "w") as f:
            for j in range(random.randint(1, 10)):
                f.write(f"Строка номер {j + 1} файла номер {i}\n")



    files = []
    for i in range(1, 4):
        with open(f'file{i}.txt', 'r') as f:
            content = f.read()
            files.append((f'file{i}.txt', content.count('\n'), content))

    files.sort(key=lambda x: x[1])


    with open('result.txt', 'w') as f:
        for file in files:
            filename, num_lines, content = file
            f.write(f'{filename}\n{num_lines}\n{content}\n')


def Task3():
    merge_files()



if __name__ == '__main__':
    Task1()
    Task2()
    Task3()
