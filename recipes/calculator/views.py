from django.shortcuts import render

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
}


def recipet(request, dish: str):
    data = request.POST or None
    if data:
        dish = data.get('dish')
    ingridients = DATA.get(dish).copy() if DATA.get(dish) else None
    if ingridients:
        servings = request.GET.get('servings')
        if servings and servings.isdigit():
            for key in ingridients:
                ingridients[key] *= int(servings)
    context = {
        'recipe': ingridients or None,
        'DATA': DATA.keys()
    }
    return render(request, 'calculator/index.html', context)
