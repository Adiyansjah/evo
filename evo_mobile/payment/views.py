from django.shortcuts import render


def buy_ticket(request, event_id):
    return render(request, 'payment/buy_ticket.html')


def show_receipt(request, receipt_id):
    return render(request, 'payment/receipt.html')
