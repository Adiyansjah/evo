from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import Promotion


@require_http_methods(["GET"])
def promo_list(request):
    """
    This controller is responsible
    to render promotion list.
    """
    query = request.GET.copy()
    query_page = query.get('page', None)

    promotions = Promotion.objects.all()

    limit = 3
    paginator = Paginator(promotions, limit)

    try:
        promotions = paginator.page(query_page)
    except PageNotAnInteger:
        promotions = paginator.page(1)
    except EmptyPage:
        promotions = paginator.page(promotions.num_pages)

    page_url = {}

    if promotions.has_next():
        query['page'] = promotions.next_page_number()
        page_url['next'] = request.path + '?' + query.urlencode()

    if promotions.has_previous():
        query['page'] = promotions.previous_page_number()
        page_url['prev'] = request.path + '?' + query.urlencode()

    data = {'promotions': promotions, 'page_url': page_url}
    return render(request, 'promotion/promo_list.html', data)


@require_http_methods(["GET"])
def promo_details(request, promo_id):
    """
    This controller is responsible
    to render promotion detail based on id
    """
    promotion = get_object_or_404(Promotion, pk=promo_id)
    data = {'promotion': promotion}
    return render(request, 'promotion/promo_details.html', data)
