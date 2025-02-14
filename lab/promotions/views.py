from django.shortcuts import render
from django.http import HttpResponse

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

def detail_promotion(request, promotion_id):
    promotion = None
    if(promotion_id <= len(promotions) and promotion_id > 0):
        promotion = promotions[int(promotion_id)-1]
    else:
        promotion = {
            'title': 'Essa promoção não existe.',
            'description': 'Promoção não encontrada.'
        }

    context = {
            'promotion': promotion
        }
    
    return render(request, 'promotions/detail_promotion.html', context)