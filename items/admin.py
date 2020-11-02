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

    class Media:
        css = {
            'all': ('selects/select2.css',)
            }
        js = (
                'selects/jquery.js',
                'selects/select2.js',
                'selects/custom.js',
            )


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'serving', 'total_cost')
    search_fields = ('name',)
    readonly_fields = ('total_cost',)

    inlines = (
        RecipeItemInline,
    )
