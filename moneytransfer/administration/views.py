from customeraccess.models import SendMoney, Receiver
from exchange.models import MoneyExchange
from transfer.models import MoneyTransfer
from administration.models import BankUser, CurrencyRate, Faq, MoneyUser, ReasonType
from administration.forms import AgentBankForm, AgentChangeForm, AgentForm, CurrencyForm, CustomerBankForm, CustomerChangeForm, CustomerForm, EditAgentBankForm, EditAgentForm, EditCustomerBankForm, EditCustomerForm, EditCurrencyForm, EditReasonForm, FaqForm, ReasonForm, PasswordChangeForm, EditFaqForm
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib import messages 
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from administration.filters import AgentFilter, CurrencyFilter, CustomerFilter, AgentBankFilter, CustomerBankFilter, ReasonFilter, FaqFilter
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from administration.mixins import SearchMixin


# Create your views here.

"************************************** DASHBOARD-VIEW ****************************************"
def agentprofile(request):
    if request.method == "POST":
        form = AgentChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ("Your Profile Updated"))
            return redirect('administration:dashboard')
    else:
        form = AgentChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'auth/edit-agent-profile.html', context)


def customerprofile(request):
    if request.method == "POST":
        form = CustomerChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, ("Your Profile Updated"))
            return redirect('administration:my_dashboard')
    else:
        form = CustomerChangeForm(instance=request.user)
    context = {'form': form}
    return render(request, 'auth/edit-customer-profile.html', context)

def agentchangepassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Password Changed", extra_tags='green')
            return redirect('administration:dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'auth/password-change-form.html', context)


def customerchangepassword(request):
    if request.method == "POST":
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Password Changed", extra_tags='green')
            return redirect('administration:my_dashboard')
    else:
        form = PasswordChangeForm(user=request.user)
    context = {'form': form}
    return render(request, 'auth/customer-password-change-form.html', context)



class GlobalSearchView(SearchMixin, TemplateView):
    template_name = 'administartion/dashboard.html'
    search_settings = {
        'administration.Customer': ['username'],
        'administration.Agent': ['username', 'description'],
    }

def error_500(request, *args, **argv):
        data = {}
        return render(request,'auth/error-404-NOT-FOUND.html', data)


def error_404(request, *args, **argv):
        data = {}
        return render(request,'auth/error-404-NOT-FOUND.html', data)



@login_required(login_url='customeraccess:login')
def my_dashboard(request):
    receiver = Receiver.objects.all()
    transaction = SendMoney.objects.all()
    received = SendMoney.objects.filter(money_status="Received")
    pending = SendMoney.objects.filter(money_status="Ready To Collect")
    cancel = SendMoney.objects.filter(money_status="Cancelled")
    total_complete = received.count()
    total_pending = pending.count()
    total_cancel = received.count()
    total_receiver = receiver.count()
    total_money_transaction = transaction.count()
    context = {'total_receiver':total_receiver, 'total_money_transaction':total_money_transaction, 
    'total_complete':total_complete, 'total_pending': total_pending, 'total_cancel':total_cancel}
    return render(request, "customeraccess/customer-dashboard.html", context)

@login_required(login_url='administration:login')
def dashboard(request):
    agent = MoneyUser.objects.filter(user_type='agent')
    customer = MoneyUser.objects.filter(user_type='customer')
    currency = CurrencyRate.objects.all()
    exchange = MoneyExchange.objects.all()
    transfer = MoneyTransfer.objects.all()
    debt = MoneyTransfer.objects.all()
    total_agent = agent.count()
    total_customer = customer.count()
    total_currency = currency.count()
    total_exchange = exchange.count()
    total_transfer = transfer.count()
    total_debt = debt.count()
    context = {'total_agent': total_agent, 'total_customer': total_customer, 'total_currency':total_currency, 
    'total_exchange':total_exchange, 'total_transfer': total_transfer, 'total_debt': total_debt}
    return render(request, "administration/dashboard.html", context)

def login_view(request):
    if request.user.is_authenticated and request.user.is_agent:
        return redirect('administration:dashboard')
    elif request.user.is_authenticated and request.user.is_customer:
        return redirect('administration:my_dashboard')    
    elif request.user.is_authenticated:
        return redirect('administration:dashboard')        
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                if user.is_customer:
                    login(request, user)
                    return redirect('administration:my_dashboard')
                elif user.is_authenticated:
                    login(request, user)
                    return redirect('administration:dashboard')    
                elif user.is_agent:
                    login(request, user)
                    return redirect('administration:dashboard')
            else:
                messages.info(request, 'Username OR Password is Incorrect !')

        context = {}
        return render(request, 'auth/login-form.html', context)


def logoutUser(request):
	logout(request)
	return redirect('administration:login')

"************************************** AGENT-VIEW ****************************************"


@login_required(login_url='administration:login')
def new_agent(request):
    if request.method == "POST":
        form = AgentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_type = 'agent'
            obj.is_agent = True
            obj.save(['user_type','is_agent'])
            messages.success(request, "Succesfully Registered", extra_tags='green')                     
            return redirect('administration:agent')
    else:
        form = AgentForm()       
    return render(request,'administration/add-new-agent.html',{'form':form})




@login_required(login_url='administration:login')
def agent_list(request):
    agent_list = MoneyUser.objects.filter(user_type='agent')
    Filter = AgentFilter(request.GET, queryset=agent_list)
    page_obj = Filter.qs
    paginator = Paginator(page_obj, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'agent_list': MoneyUser.objects.filter(user_type='agent'), 'filter': Filter, 'page_obj': page_obj}
    return render(request, "administration/agent.html", context)


@login_required(login_url='administration:login')
def view_agent(request, id):
    context = {'view_agent': MoneyUser.objects.filter(pk = id)}
    return render(request, "administration/view-agent.html", context)

def search(request):
    user_list = MoneyUser.objects.all()
    user_filter = AgentFilter(request.GET, queryset=user_list)
    return render(request, 'administration/user_list.html', {'filter': user_filter})


@login_required(login_url='administration:login')
def edit_agent(request,id):
    agent = MoneyUser.objects.get(pk=id)
    form = EditAgentForm(instance=agent)
    if request.method == 'POST':
        form = EditAgentForm(request.POST, instance=agent)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated')
            return redirect('administration:agent')
    return render(request,'administration/edit-agent.html',{'form':form})





@login_required(login_url='administration:login')             
def delete_agent(request,id):
    agent = MoneyUser.objects.get(pk=id)
    agent.delete()
    return redirect('administration:agent')


"************************************** CUSTOMER-VIEW ****************************************"

@login_required(login_url='administration:login')
def new_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.user_type = 'customer'
            obj.is_customer = True
            obj.save(['user_type', 'is_customer'])
            return redirect('administration:customer')             
    else:
        form = CustomerForm()       
    return render(request,'administration/add-new-customer.html',{'form':form})


@login_required(login_url='administration:login')
def customer_list(request):
    customer_list = MoneyUser.objects.filter(user_type='customer')
    Filter = CustomerFilter(request.GET, queryset=customer_list)
    page_obj = Filter.qs
    paginator = Paginator(page_obj, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'customer_list': MoneyUser.objects.filter(user_type='customer'), 'filter': Filter, 'page_obj': page_obj}
    return render(request, "administration/customer.html", context)



@login_required(login_url='administration:login')
def view_customer(request, id):
    context = {'view_customer': MoneyUser.objects.filter(pk = id)}
    return render(request, "administration/view-customer.html", context)



@login_required(login_url='administration:login')
def edit_customer(request,id):
    customer = MoneyUser.objects.get(pk=id)
    form = EditCustomerForm(instance=customer)
    if request.method == 'POST':
        form = EditCustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated')
            return redirect('administration:customer')
    return render(request,'administration/edit-customer.html',{'form':form})


@login_required(login_url='administration:login')             
def delete_customer(request,id):
    customer = MoneyUser.objects.get(pk=id)
    customer.delete()
    return redirect('administration:customer')

"************************************** CURRENCY-VIEW ****************************************"

@login_required(login_url='administration:login')
def new_currency(request):
    if request.method == "POST":
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Currency Added!')
            return redirect('administration:currency')             
    else:
        form = CurrencyForm()       
    return render(request,'administration/add-currency.html',{'form':form})


@login_required(login_url='administration:login')
def currency_list(request):
    currency_list = CurrencyRate.objects.all()
    Filter = CurrencyFilter(request.GET, queryset=currency_list)
    page_obj = Filter.qs
    paginator = Paginator(page_obj, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'currency_list': CurrencyRate.objects.all(), 'filter': Filter, 'page_obj': page_obj}
    return render(request, "administration/currency.html", context)



@login_required(login_url='administration:login')
def view_currency(request, id):
    context = {'view_currency': CurrencyRate.objects.filter(pk = id)}
    return render(request, "administration/view-currency.html", context)



@login_required(login_url='administration:login')
def edit_currency(request,id):
    currency = CurrencyRate.objects.get(pk=id)
    form = EditCurrencyForm(instance=currency)
    if request.method == 'POST':
        form = EditCurrencyForm(request.POST,  instance=currency)
        if form.is_valid():
            form.save()
            return redirect('administration:currency')
    return render(request,'administration/edit-currency.html',{'form':form})


@login_required(login_url='administration:login')             
def delete_currency(request,id):
    currency = CurrencyRate.objects.get(pk=id)
    currency.delete()
    return redirect('administration:currency')

"************************************** REASONS-VIEW ****************************************"

@login_required(login_url='administration:login')
def new_reason(request):
    if request.method == "POST":
        form = ReasonForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Succesfully Created", extra_tags='green')                     
            return redirect('administration:reason')                     
    else:
        form = ReasonForm()       
    return render(request,'administration/add-reasons.html',{'form':form})




@login_required(login_url='administration:login')
def reason_list(request):
    reason_list = ReasonType.objects.all()
    Filter = ReasonFilter(request.GET, queryset=reason_list)
    page_obj = Filter.qs
    paginator = Paginator(page_obj, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'reason_list': ReasonType.objects.all(), 'filter': Filter, 'page_obj': page_obj}
    return render(request, "administration/reasons.html", context)


@login_required(login_url='administration:login')
def view_reason(request, id):
    context = {'view_reason': ReasonType.objects.filter(pk = id)}
    return render(request, "administration/view-reasons.html", context)



@login_required(login_url='administration:login')
def edit_reason(request,id):
    reason = ReasonType.objects.get(pk=id)
    form = EditReasonForm(instance=reason)
    if request.method == 'POST':
        form = EditReasonForm(request.POST, instance=reason)
        if form.is_valid():
            form.save()
            return redirect('administration:reason')
    return render(request,'administration/edit-reasons.html',{'form':form})




@login_required(login_url='administration:login')             
def delete_reason(request,id):
    reason = ReasonType.objects.get(pk=id)
    reason.delete()
    return redirect('administration:reason')


"************************************** AGENT-BANK-VIEW ****************************************"

@login_required(login_url='administration:login')
def add_agentbank(request):
    if request.method == "POST":
        form = AgentBankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administration:agent_bank')             
    else:
        form = AgentBankForm()       
    return render(request,'administration/add-agent-bank.html',{'form':form})


@login_required(login_url='administration:login')
def agent_bank(request):
    agent_bank = BankUser.objects.filter(bank_user='agentbank')
    Filter = AgentBankFilter(request.GET, queryset=agent_bank)
    page_obj = Filter.qs
    paginator = Paginator(page_obj, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'agent_bank': BankUser.objects.filter(bank_user='agentbank'), 'filter': Filter, 'page_obj': page_obj}
    return render(request, "administration/agent-bank.html", context)



@login_required(login_url='administration:login')
def view_agentbank(request, id):
    context = {'view_agentbank': BankUser.objects.filter(pk = id)}
    return render(request, "administration/view-agent-bank.html", context)



@login_required(login_url='administration:login')
def edit_agentbank(request,id):
    agentbank = BankUser.objects.get(pk=id)
    form = EditAgentBankForm(instance=agentbank)
    if request.method == 'POST':
        form = EditAgentBankForm(request.POST,  instance=agentbank)
        if form.is_valid():
            form.save()
            return redirect('administration:agent_bank')
    return render(request,'administration/edit-agent-bank.html',{'form':form})


@login_required(login_url='administration:login')             
def delete_agentbank(request,id):
    agentbank = BankUser.objects.get(pk=id)
    agentbank.delete()
    return redirect('administration:agent_bank')


"************************************** CUSTOMER-BANK-VIEW ****************************************"

@login_required(login_url='administration:login')
def add_customerbank(request):
    if request.method == "POST":
        form = CustomerBankForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('administration:customer_bank')             
    else:
        form = CustomerBankForm()       
    return render(request,'administration/add-customer-bank.html',{'form':form})


@login_required(login_url='administration:login')
def customer_bank(request):
    customer_bank = BankUser.objects.filter(bank_user='customerbank')
    Filter = CustomerBankFilter(request.GET, queryset=customer_bank)
    page_obj = Filter.qs
    paginator = Paginator(page_obj, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'customer_bank': BankUser.objects.filter(bank_user='customerbank'), 'filter': Filter, 'page_obj': page_obj}
    return render(request, "administration/customer-bank.html", context)



@login_required(login_url='administration:login')
def view_customerbank(request, id):
    context = {'view_customerbank': BankUser.objects.filter(pk = id)}
    return render(request, "administration/view-customer-bank.html", context)



@login_required(login_url='administration:login')
def edit_customerbank(request,id):
    customerbank = BankUser.objects.get(pk=id)
    form = EditCustomerBankForm(instance=customerbank)
    if request.method == 'POST':
        form = EditCustomerBankForm(request.POST,  instance=customerbank)
        if form.is_valid():
            form.save()
            return redirect('administration:customer_bank')
    return render(request,'administration/edit-customer-bank.html',{'form':form})


@login_required(login_url='administration:login')             
def delete_customerbank(request,id):
    customerbank = BankUser.objects.get(pk=id)
    customerbank.delete()
    return redirect('administration:customer_bank')


@login_required(login_url='administration:login')
def add_faq(request):
    if request.method == "POST":
        form = FaqForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Succesfully Created", extra_tags='green')                     
            return redirect('administration:faq_list')                     
    else:
        form = FaqForm()       
    return render(request,'administration/add-faq.html',{'form':form})


@login_required(login_url='administration:login')
def faq_list(request):
    context = {'faq_list': Faq.objects.all()}
    return render(request, "administration/faq.html", context)

@login_required(login_url='administration:login')
def edit_faq(request,id):
    faq = Faq.objects.get(pk=id)
    form = EditFaqForm(instance=faq)
    if request.method == 'POST':
        form = EditFaqForm(request.POST, instance=faq)
        if form.is_valid():
            form.save()
            return redirect('administration:faq_list')
    return render(request,'administration/edit-faq.html',{'form':form})




@login_required(login_url='administration:login')             
def delete_faq(request,id):
    faq = Faq.objects.get(pk=id)
    faq.delete()
    return redirect('administration:faq_list')
