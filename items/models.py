from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

from measurement.utils import guess

UNIT = (
    ('g', 'Gram'),
    ('mg', 'Milligram'),
    ('kg', 'Kilogram'),

    ('ml', 'Millimeter'),
    ('l', 'Liter'),

    ('oz', 'Oz'),

    ('us_tbsp', 'Table Spoon'),
    ('us_tsp', 'Tea Spoon'),
    
    ('us_cup', 'Cup')
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
    
    class Meta:
        ordering = ('name',)


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
            costs += recipe.cost()
        return '₱{0:.2f}'.format(costs)


class RecipeItem(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    amount = models.DecimalField(null=False, blank=False, decimal_places=2 , max_digits=10)
    unit = models.CharField(max_length=200, choices=UNIT)
    created =  models.DateTimeField(auto_now_add=True)

    def __str__(self):
        unit = self.get_unit_display()
        return f'{self.recipe.name} - {self.amount} {unit} - ₱{self.cost()}'

    def clean(self):
        try:
            self.cost()
        except:
            raise ValidationError(f"Unable to convert {self.ingredient.unit} to {self.unit}")

    def cost(self):
        try:
            ingredient = self.ingredient
            measurement = guess(self.ingredient.amount, self.ingredient.unit)
            recipe_amount = measurement.__getattr__(self.unit)
            used_amount = float(self.amount) / float(recipe_amount)
            used_cost = float(used_amount) * float(self.ingredient.cost)
            return used_cost
        except:
            raise ValidationError(f"Unable to convert {self.ingredient.unit} to {self.unit}")