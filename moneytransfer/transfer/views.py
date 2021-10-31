from administration.models import CurrencyRate
from transfer.filters import DebtFilter, MoneyFilter
from transfer.models import DebtTransfer, MoneyTransfer
from transfer.forms import DebtTransferForm, MoneyTransferForm, EditMoneyTransferForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.http import JsonResponse


# Create your views here.
@login_required(login_url='administration:login')
def new_transfer(request):
    if request.method == "POST":
        form = MoneyTransferForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transfer:money_transfer')                     
    else:
        form = MoneyTransferForm()       
    return render(request,'transfer/add-money-transfer.html',{'form':form})

def load_rate(request):
    to_currency = request.GET.get('to_currency')
    currencys = CurrencyRate.objects.all().filter(to_currency=to_currency)
    return render(request, 'transfer/rate.html', {'currencys': currencys})

def load_cities(request):
    from_currency = request.GET.get('from_currency')
    rates = CurrencyRate.objects.all().filter(from_currency=from_currency)
    return render(request, 'transfer/currency.html', {'rates': rates})

@login_required(login_url='administration:login')
def transfer_list(request):
    transfer_list = MoneyTransfer.objects.all()
    Filter = MoneyFilter(request.GET, queryset=transfer_list)
    page_obj = Filter.qs
    paginator = Paginator(page_obj, 10)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    context = {'transfer_list': MoneyTransfer.objects.all(), 'filter': Filter, 'page_obj': page_obj}
    return render(request, "transfer/money-transfer.html", context)


@login_required(login_url='administration:login')
def view_transfer(request, id):
    context = {'view_transfer': MoneyTransfer.objects.filter(pk = id)}
    return render(request, "transfer/view-money-transfer.html", context)



@login_required(login_url='administration:login')
def edit_transfer(request,id):
    transfer = MoneyTransfer.objects.get(pk=id)
    form = EditMoneyTransferForm(instance=transfer)
    if request.method == 'POST':
        form = EditMoneyTransferForm(request.POST, instance=transfer)
        if form.is_valid():
            form.save()
            return redirect('transfer:money_transfer')
    return render(request,'transfer/edit-money-transfer.html',{'form':form})




@login_required(login_url='administration:login')             
def delete_transfer(request,id):
    transfer = MoneyTransfer.objects.get(pk=id)
    transfer.delete()
    return redirect('transfer:money_transfer')


@login_required(login_url='administration:login')
def debt_list(request):
    transfer_list = DebtTransfer.objects.all()
    Filter = DebtFilter(request.GET, queryset=transfer_list)
    page_obj = Filter.qs
    paginator = Paginator(page_obj, 8)
    page_number = request.GET.get('page',1)
    page_obj = paginator.get_page(page_number)
    context = {'transfer_list': DebtTransfer.objects.all(), 'filter': Filter, 'page_obj': page_obj}
    return render(request, "transfer/debt-money-transfer.html", context)

@login_required(login_url='administration:login')
def edit_debt(request,id):
    transfer = DebtTransfer.objects.get(pk=id)
    form = DebtTransferForm(instance=transfer)
    if request.method == 'POST':
        form = DebtTransferForm(request.POST, instance=transfer)
        if form.is_valid():
            form.save(commit=False)
            DebtTransfer.objects.update_or_create(paid_amount=form.cleaned_data['paid_amount'],outstanding_amount=form.cleaned_data['outstanding_amount'],
            receiver_customer=form.cleaned_data['receiver_customer'],sender_agent=form.cleaned_data['sender_agent'], from_currency=form.cleaned_data['from_currency'],
            due_date=form.cleaned_data['due_date'],debt_id=form.cleaned_data['debt_id'], sending_amount=form.cleaned_data['sending_amount'],)
            return redirect('transfer:debt_transfer')
    return render(request,'transfer/edit-debt-money-transfer.html',{'form':form})


@login_required(login_url='administration:login')
def view_debt(request, id):
    context = {'view_debt': DebtTransfer.objects.filter(pk = id)}
    return render(request, "transfer/view-debt-money-transfer.html", context)
