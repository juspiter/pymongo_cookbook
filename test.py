from cookbook import Cookbook
from recipe import Recipe

# Executar o container:
# docker run --name cookbook -d mongo:4.4.10

# Pegar o IP do container:
# docker inspect cookbook

# Conectar ao banco de dados:
book = Cookbook('172.17.0.2:27017')


# Popular o banco de dados, se necessário:
# book.add_recipe(Recipe("salad", 5, ["lettuce", "tomatoes", "vinegar", "olive oil"], "meal"))
# book.add_recipe(Recipe("soup", 45, ["water", "potatoes", "carrots", "salt", "pepper"], "meal"))
# book.add_recipe(Recipe('sandwich', 2, ['bread', 'mayo', 'ham', 'cheese'], 'snack'))
# book.add_recipe(Recipe('ice cream', 600, ['cream', 'milk', 'sugar', 'vanilla'], 'dessert'))


print(book.get_recipe_by_name("ice cream"), "\n")
print(book.get_recipe_by_type("meal"), "\n")
print(str(book))
