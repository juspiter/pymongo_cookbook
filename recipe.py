class Recipe:
	def __init__(self, name: str, cooking_time: int, ingredients: list, recipe_type: str):
		assert isinstance(name, str) and len(name) > 0,\
			"A recipe name must be provided as a string"

		assert isinstance(cooking_time, int) and cooking_time >= 0,\
			"Cooking time must be a non-negative int"

		assert isinstance(ingredients, list) and len(ingredients) > 0,\
			"The recipe's ingredients must be provided as a non-empty list"

		assert isinstance(recipe_type, str) and \
			recipe_type.lower() in ["snack", "meal", "dessert"],\
			"Recipe type must be 'snack', 'meal' or 'dessert'"

		self.name = name
		self.cooking_time = cooking_time
		self.ingredients = ingredients
		self.recipe_type = recipe_type.lower()

	def __str__(self):
		"Returns a string containing recipe info."
		return f"""Recipe: {self.name}
Cooking time: {self.cooking_time}
Ingredients: {str(self.ingredients)}
Recipe type: {self.recipe_type}"""
