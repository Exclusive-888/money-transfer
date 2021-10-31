# from administration.forms import AgentForm, CustomerForm
from customeraccess.models import Receiver, SendMoney
from administration.models import Faq
from customeraccess.forms import ReceiverForm, SendMoneyForm, EditReceiverForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from customeraccess.filters import ReceiverFilter

# Create your views here.
@login_required(login_url='customeraccess:login')
def my_dashboard(request):
    # receiver = Receiver.objects.all()
    # transaction = SendMoney.objects.all()
    # total_receiver = receiver.count()
    # total_money_transaction = transaction.count()
    # context = {'total_receiver':total_receiver, 'total_money_transaction':total_money_transaction}
    return render(request, "customeraccess/customer-dashboard.html")

@login_required(login_url='customeraccess:login')
def construction(request):
    return render(request, "base/index.html")



# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             if user.is_customer:
#                 login(request, user)
#                 return redirect('administration:my_dashboard')
#             elif user.is_agent:
#                 login(request, user)
#                 return redirect('administration:dashboard')
#         else:
#             messages.info(request, 'Username OR Password is Incorrect !')

#     context = {}
#     return render(request, 'auth/customer-login-form.html', context)



@login_required(login_url='customeraccess:login')
def add_receiver(request):
    if request.method == "POST":
        form = ReceiverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customeraccess:my_receiver')
    else:
        form = ReceiverForm()
    return render(request, 'customeraccess/add-receiver.html', {'form': form})


@login_required(login_url='customeraccess:login')
def my_receiver(request):
    my_receiver = Receiver.objects.all()
    Filter = ReceiverFilter(request.GET, queryset=my_receiver)
    page_obj = Filter.qs
    paginator = Paginator(page_obj, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'my_receiver': Receiver.objects.all(), 'filter': Filter, 'page_obj': page_obj}
    return render(request, "customeraccess/my-receiver.html", context)


@login_required(login_url='customeraccess:login')
def view_receiver(request, id):
    context = {'view_receiver': Receiver.objects.filter(pk=id)}
    return render(request, "customeraccess/view-my-receiver.html", context)


@login_required(login_url='customeraccess:login')
def edit_receiver(request, id):
    receiver = Receiver.objects.get(pk=id)
    form = EditReceiverForm(instance=receiver)
    if request.method == 'POST':
        form = EditReceiverForm(request.POST, instance=receiver)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated')
            return redirect('customeraccess:my_receiver')
    return render(request, 'customeraccess/edit-my-receiver.html', {'form': form})


@login_required(login_url='customeraccess:login')
def delete_receiver(request, id):
    receiver = Receiver.objects.get(pk=id)
    receiver.delete()
    return redirect('customeraccess:my_receiver')


@login_required(login_url='customeraccess:login')
def make_transaction(request):
    if request.method == "POST":
        form = SendMoneyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('customeraccess:my_transaction')
    else:
        form = SendMoneyForm()
    return render(request, 'customeraccess/send-money.html', {'form': form})


@login_required(login_url='customeraccess:login')
def my_transaction(request):
    context = {'my_transaction': SendMoney.objects.all()}
    return render(request, "customeraccess/my-transaction.html", context)

@login_required(login_url='customeraccess:login')
def view_transaction(request, id):
    context = {'view_transaction': SendMoney.objects.filter(pk=id)}
    return render(request, "customeraccess/view-my-transaction.html", context)


def logoutCustomer(request):
    logout(request)
    return redirect('administration:login')


@login_required(login_url='customeraccess:login')
def track_transfer(request):
    return render(request, "customeraccess/track-transfer.html")


@login_required(login_url='customeraccess:login')
def track_details(request):
    return render(request, "customeraccess/track-transfer-details.html")


@login_required(login_url='customeraccess:login')
def find_agent(request):
    return render(request, "customeraccess/find-agent.html")


@login_required(login_url='customeraccess:login')
def agent_location(request):
    return render(request, "customeraccess/find-nearest-location.html")

@login_required(login_url='administration:login')
def faq_list(request):
    context = {'faq_list': Faq.objects.all()}
    return render(request, "customeraccess/customer-faq-view.html", context)
