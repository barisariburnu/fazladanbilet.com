from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from mailgun import mailgun

__author__ = 'cemkiy'

from django.shortcuts import render, render_to_response
# Create your views here.
from django.http.response import HttpResponse, HttpResponseRedirect
from bitcoin.coinbase_api import coinbase_api
from member.models import Orders, On_Sales
from decimal import Decimal
from django.template import Context

# def exeample(request):
#     api = coinbase_api()
#     button = api.create_button('1', 'deneme', '31')
#     print button[0]
#
#     return render_to_response('main.html', locals())


@login_required
def payment_page(request, order_id):
    try:
        order = Orders.objects.filter(id=order_id, active=True)[0]
    except Exception as e:
        print e
        return False

    amount = Decimal(order.on_sales.amount_bitcoin) * int(order.total_ticket)
    print amount
    api = coinbase_api()
    button = api.create_button(amount, order_id)
    print api.get_orders()
    button_data = button[0]
    return render_to_response('payment_page.html', locals())


@login_required
def succes_url(request, order_id):
    clean_order_id = ''
    for letter in str(order_id):
        if letter == '?':
            clean_order_id = int(clean_order_id)
            break
        else:
            clean_order_id += letter

    try:
        order = Orders.objects.filter(id=clean_order_id, status='1')[0]
        on_sale = On_Sales.objects.filter(id=order.on_sales.id)[0]
    except Exception as e:
        print e
        return HttpResponseRedirect('/sorry')

    api = coinbase_api()
    coinbase_order = api.get_order_by_id(clean_order_id)

    if coinbase_order:
        print coinbase_order[2]
        if str(coinbase_order[2]) == 'Status.complete': #control for payment
            try:
                order.status = '2'  # next step for dealing
                order.save()
            except Exception as e:
                print e
                return False

            try:
                on_sale.total_ticket = int(on_sale.total_ticket) - int(order.total_ticket)  # decrease total ticket
                on_sale.save()
                if on_sale.total_ticket == 0:
                    on_sale.active = False
                    on_sale.save()
            except Exception as e:
                print e
                return False

            amount = Decimal(order.on_sales.amount_bitcoin) * int(order.total_ticket)

            template = get_template("mail_comes_shipping.html")
            context = Context({'username': order.ship_to_user.username,
                               'ticket_name': order.on_sales.title,
                               'total': str(amount),
                               'total_ticket': order.total_ticket})
            content = template.render(context)
            mailgun_operator = mailgun()
            mailgun_operator.send_mail_with_html(order.ship_to_user.email, content)

            template = get_template("mail_sends_shipping.html")
            context = Context({'username': order.on_sales.member.username,
                       'ship_to_username': order.ship_to_user.username,
                       'id': order.ship_to_user.id,
                       'shipping_address': order.address,
                       'shipping_username': order.name,
                       'shipping_phone': order.phone,
                       'total': str(amount),
                       'total_ticket': order.total_ticket})
            content = template.render(context)
            mailgun_operator.send_mail_with_html(order.on_sales.member.email, content)
        else:
            return HttpResponseRedirect('/bitcoin/cancel_url')

    return render_to_response('success_url.html', locals())


def cancel_url(request):
    return render_to_response('cancel_url.html', locals())