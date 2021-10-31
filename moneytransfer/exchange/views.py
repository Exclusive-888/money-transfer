from exchange.filters import ExchangeFilter
from exchange.models import MoneyExchange
from exchange.forms import MoneyExchangeForm, EditMoneyExchangeForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url='administration:login')
def new_exchange(request):
    if request.method == "POST":
        form = MoneyExchangeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('exchange:money_exchange')                     
    else:
        form = MoneyExchangeForm()       
    return render(request,'exchange/add-money-exchange.html',{'form':form})




@login_required(login_url='administration:login')
def exchange_list(request):
    exchange_list = MoneyExchange.objects.all()
    Filter = ExchangeFilter(request.GET, queryset=exchange_list)
    page_obj = Filter.qs
    paginator = Paginator(page_obj, 1)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    context = {'exchange_list': MoneyExchange.objects.all(), 'filter': Filter, 'page_obj': page_obj}
    return render(request, "exchange/money-exchange.html", context)


@login_required(login_url='administration:login')
def view_exchange(request, id):
    context = {'view_exchange': MoneyExchange.objects.filter(pk = id)}
    return render(request, "exchange/view-money-exchange.html", context)



@login_required(login_url='administration:login')
def edit_exchange(request,id):
    exchange = MoneyExchange.objects.get(pk=id)
    form = EditMoneyExchangeForm(instance=exchange)
    if request.method == 'POST':
        form = EditMoneyExchangeForm(request.POST, instance=exchange)
        if form.is_valid():
            form.save()
            return redirect('exchange:money_exchange')
    return render(request,'exchange/edit-money-exchange.html',{'form':form})




@login_required(login_url='administration:login')             
def delete_exchange(request,id):
    exchange = MoneyExchange.objects.get(pk=id)
    exchange.delete()
    return redirect('exchange:money_exchange')
