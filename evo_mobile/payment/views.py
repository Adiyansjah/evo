from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required

import uuid
from datetime import datetime
from event.models import Event, Ticket
from authentication.models import UserDetail
from .models import Payment


@login_required
@require_http_methods(["GET"])
def buy_ticket(request, event_id):
    event = get_object_or_404(
        Event, pk=event_id)
    tickets = event.tickets.all()
    data = {'tickets': tickets, 'event': event_id}
    return render(request, 'payment/buy_ticket.html', data)


@login_required
@require_http_methods(["POST"])
def show_receipt(request):
    event = request.POST.get('event')
    tickets = request.POST.getlist('ticket[]', [])

    paid = []
    total = 0
    event = Event.objects.get(pk=event)

    for ticket in tickets:
        raw_data = ticket.split('-')
        q = int(raw_data[1])
        if q > 0:
            t = Ticket.objects.get(pk=raw_data[0])
            paid.append({
                'ticket': t,
                'quantity': q,
                'total': t.price * q
            })
            total += t.price * q

    data = {
        'event': event,
        'tickets': paid,
        'user': request.user.detail,
        'code': uuid.uuid4(),
        'total': total
    }

    return render(request, 'payment/receipt.html', data)


@login_required
@require_http_methods(["POST"])
def save_receipt(request):
    method = request.POST.get('payment')
    total = request.POST.get('total')
    event_id = request.POST.get('event')
    code = request.POST.get('code')

    payment = Payment()
    payment.price = float(total)
    payment.code = code
    payment.method = method
    payment.event = Event.objects.get(pk=event_id)
    payment.user = request.user
    payment.save()

    return redirect('/my_ticket')


@login_required
@require_http_methods(["GET"])
def show_my_tickets(request):
    upcoming = Payment.objects.filter(event__start_date__gte=datetime.now().date()).filter(user=request.user.id)
    history = Payment.objects.filter(event__start_date__lt=datetime.now().date()).filter(user=request.user.id)
    data = {
        'upcoming': upcoming,
        'history': history
    }
    return render(request, 'payment/my_ticket.html', data)
