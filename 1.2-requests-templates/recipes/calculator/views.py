
from django.shortcuts import render, reverse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }


def recipe_view(request, dish):
    recipe = DATA.get(dish, None)
    if recipe:
        servings = int(request.GET.get('servings', 1))
        updated_recipe = {key: value * servings for key, value in recipe.items()}
        context = {
          'recipe': updated_recipe
        }
        return render(request, 'calculator/index.html', context)


def home_view(request):
    template_name = 'calculator/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Омлет': reverse('recipe', kwargs={'dish': 'omlet'}),
        'Паста': reverse('recipe', kwargs={'dish': 'pasta'}),
        'Бутерброд': reverse('recipe', kwargs={'dish': 'buter'}),
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)
