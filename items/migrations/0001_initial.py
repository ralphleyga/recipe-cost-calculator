# Generated by Django 3.1.2 on 2020-11-02 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('unit', models.CharField(choices=[('g', 'gram'), ('mg', 'miligram'), ('kg', 'kilogram'), ('ml', 'Milimeter'), ('l', 'Liter'), ('oz', 'Oz'), ('tbsp', 'Table Spoon'), ('tsp', 'Tea Spoon'), ('cup', 'Cup')], max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('description', models.TextField(blank=True, null=True)),
                ('serving', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('unit', models.CharField(choices=[('g', 'gram'), ('mg', 'miligram'), ('kg', 'kilogram'), ('ml', 'Milimeter'), ('l', 'Liter'), ('oz', 'Oz'), ('tbsp', 'Table Spoon'), ('tsp', 'Tea Spoon'), ('cup', 'Cup')], max_length=200)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('ingredient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.ingredient')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='items.recipe')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
