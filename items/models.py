from django.db import models
from django.conf import settings

UNIT = (
    ('g', 'gram'),
    ('mg', 'miligram'),
    ('kg', 'kilogram'),

    ('ml', 'Milimeter'),
    ('l', 'Liter'),

    ('oz', 'Oz'),

    ('tbsp', 'Table Spoon'),
    ('tsp', 'Tea Spoon'),
    
    ('cup', 'Cup'),
)


class Ingredient(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    cost = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    unit = models.CharField(max_length=200, choices=UNIT)
    amount = models.DecimalField(blank=False, null=False, decimal_places=2, max_digits=10)

    def __str__(self):
        return f'{self.name} {self.amount} {self.unit}'
    
    def amount_unit(self):
        return f'{self.amount} {self.unit}'


class Recipe(models.Model):
    name = models.CharField(max_length=500)
    description = models.TextField(blank=True, null=True)
    serving = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
    def total_cost(self):
        recipies = self.recipeitem_set.all()
        costs = 0

        for recipe in recipies:
            ingredient = recipe.ingredient
            used_amount = recipe.amount / ingredient.amount
            used_cost = used_amount * ingredient.cost
            costs += used_cost
        return '₱{0:.2f}'.format(costs)


class RecipeItem(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(null=False, blank=False, decimal_places=2 , max_digits=10)
    unit = models.CharField(max_length=200, choices=UNIT)
    created =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.recipe.name} - {self.amount} {self.unit}'

    def cost(self):
        use_amount = amount / self.recipe.amount
        price = use * self.recipe.cost
        return price
