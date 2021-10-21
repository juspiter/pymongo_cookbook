from pymongo import MongoClient
from recipe import Recipe


class Cookbook:
	def __init__(self, addr: str):
		"Gera uma instância da classe Database do módulo pymongo"
		self.recipes = MongoClient(host=[addr]).cookbook.recipes

	def __str__(self):
		"Retorna uma string com os nomes de todas receitas do livro separadas por tipo"
		return f"""Recipes contained:
	Snacks: {self.get_recipe_by_type("snack")}
	Meals: {self.get_recipe_by_type("meal")}
	Desserts: {self.get_recipe_by_type("dessert")}"""

	def get_recipe_by_name(self, name: str) -> dict:
		"Retorna a receita de nome <name> como um dicionário"
		return self.recipes.find_one({"name": name})

	def get_recipe_by_type(self, recipe_type: str) -> list:
		"Retorna uma lista com todos os nomes de receitas do tipo <recipe_type>"
		lst = list()
		results = self.recipes.find({"recipe_type": recipe_type})
		for result in results:
			lst.append(result["name"])
		return lst

	def add_recipe(self, new_recipe: Recipe) -> None:
		"Adiciona uma nova receita ao livro, ou atualiza uma receita de mesmo nome já existente"
		self.recipes.find_one_and_update({"name": new_recipe.name}, {
			'$set': new_recipe.__dict__}, upsert=True)
