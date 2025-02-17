from django.shortcuts import render

promotions = [
    {
        'id': 1,
        'title': 'Promoção 1',
        'description': 'Uma promoção qualquer um',
    },
    {
        'id': 2,
        'title': 'Promoção 2',
        'description': 'Uma promoção qualquer dois',
    },
    {
        'id': 3,
        'title': 'Promoção 3',
        'description': 'Uma promoção qualquer três',
    }
]

def home_view(request):
    context = {
        'promotions': promotions
    }

    return render(request, 'home/index.html', context)