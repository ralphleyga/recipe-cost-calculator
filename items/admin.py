from django.contrib import admin

from .models import (
    Ingredient,
    RecipeItem,
    Recipe
)

admin.site.site_header = "Reciply"

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost', 'amount', 'unit')
    search_fields = ('name',)


class RecipeItemInline(admin.TabularInline):
    model = RecipeItem
    raw_id_fields = ('recipe',)


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'serving', 'total_cost')
    search_fields = ('name',)
    readonly_fields = ('total_cost',)

    inlines = (
        RecipeItemInline,
    )