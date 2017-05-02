from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.urls import reverse


from .models import Event, Category, Ticket


@require_http_methods(["GET"])
def front_page(request):
    """
    This controller is responsible
    to render front page
    """
    return render(request, 'event/front.html')


@require_http_methods(["GET"])
def event_list(request):
    """
    This controller is responsible
    to render event list based on query.
    """
    query = request.GET.copy()
    query_category = query.get('category', None)
    query_name = query.get('name', None)
    query_page = query.get('page', None)

    categories = Category.objects.all()
    events = Event.objects.prefetch_related('ticket_set').all()

    if query_category and query_category != 'All':
        events = events.filter(category__name=query_category)
    if query_name:
        events = events.filter(name__icontains=query_name)

    limit = 3
    paginator = Paginator(events, limit)

    try:
        events = paginator.page(query_page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(events.num_pages)

    page_url = {}

    if events.has_next():
        query['page'] = events.next_page_number()
        page_url['next'] = request.path + '?' + query.urlencode()

    if events.has_previous():
        query['page'] = events.previous_page_number()
        page_url['prev'] = request.path + '?' + query.urlencode()

    data = {'events': events, 'categories': categories, 'page_url': page_url}

    return render(request, 'event/event_list.html', data)


@require_http_methods(["GET"])
def event_details(request, event_id):
    """
    This controller is responsible
    to render event detail based on id.
    """
    event = get_object_or_404(Event, pk=event_id)
    data = {'event': event}
    return render(request, 'event/event_details.html', data)


@require_http_methods(["GET"])
def calendar(request):
    """
    This controller is responsible
    to give event list by date
    """
    query = request.GET.copy()
    query_date = query.get('date', None)
    query_page = query.get('page', None)

    events = Event.objects.prefetch_related('ticket_set').all()

    if query_date:
        events = events.filter(start_date=query_date)

    limit = 3
    paginator = Paginator(events, limit)

    try:
        events = paginator.page(query_page)
    except PageNotAnInteger:
        events = paginator.page(1)
    except EmptyPage:
        events = paginator.page(events.num_pages)

    page_url = {}

    if events.has_next():
        query['page'] = events.next_page_number()
        page_url['next'] = request.path + '?' + query.urlencode()

    if events.has_previous():
        query['page'] = events.previous_page_number()
        page_url['prev'] = request.path + '?' + query.urlencode()

    data = {'events': events, 'page_url': page_url}

    return render(request, 'event/event_calendar.html', data)



