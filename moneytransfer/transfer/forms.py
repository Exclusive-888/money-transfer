from transfer.models import MoneyTransfer, DebtTransfer
from administration.models import CurrencyRate, MoneyUser
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML





class MoneyTransferForm(forms.ModelForm):
    
    total_commission = forms.ModelChoiceField(queryset=CurrencyRate.objects.all(), to_field_name="total_commission")
    class Meta:
        model = MoneyTransfer
        fields = ('sender_agent', 'receiver_agent', 'sender_cu', 'receiver_cu', 'send_method',
                  'receive_method', 'agent_bank', 'from_currency', 'to_currency', 'total_commission',
                  'transfer_rate', 'sending_amount', 'receiving_amount', 'paid_amount', 'due_date',
                  'outstanding_amount', 'total_payment', 'payment_status', 'reason_type', 'notification_type', 'notes')

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),

        }

        labels = {

            'sender_agent': 'Sender Agent',
            'receiver_cu': 'Receiver Customer',
            'receiver_agent': 'Receiver Agent',
            'sender_cu': 'Sender Customer',
            'send_method': 'Sending Method',
            'receive_method': 'Receiving Method',
            'from_currency': 'Sending Currency',
            'to_currency': 'Receiving Currency',
            'total_commission': 'Exchange Rate',
            'transfer_rate': 'Transfer Rate',
            'sending_amount': 'Sending Amount',
            'receiving_amount': 'Receiving Amount',
            'paid_amount': 'Paid Amount',
            'outstanding_amount': 'Outstanding Amount',
            'total_payment': 'Total Payment',
            'payment_status': 'Payment Status',
            'reason_type': 'Reason For Sending',
            'notification_type': 'Notification',
            'notes': 'Notes (optional) ',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['receiving_amount'].widget.attrs['readonly'] = True
        self.fields['outstanding_amount'].widget.attrs['readonly'] = True
        self.fields['total_payment'].widget.attrs['readonly'] = True
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.fields['sender_agent'].queryset = MoneyUser.objects.filter(is_agent=True, is_active=True)
        self.fields['sender_cu'].queryset = MoneyUser.objects.filter(is_customer=True, is_active=True)
        self.fields['receiver_agent'].queryset = MoneyUser.objects.filter(is_agent=True, is_active=True)
        self.fields['receiver_cu'].queryset = MoneyUser.objects.filter(is_customer=True, is_active=True)

        if 'from_currency' in self.data:
            try:
                from_currency = int(self.data.get('from_currency'))
                self.fields['to_currency'].queryset = MoneyTransfer.objects.filter(from_currency=from_currency)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['to_currency'].queryset = self.instance.from_currency.to_currency_set
        

        if 'to_currency' in self.data:
            try:
                to_currency = int(self.data.get('to_currency'))
                self.fields['total_commission'].queryset = CurrencyRate.objects.filter(to_currency=to_currency)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['total_commission'].queryset = self.instance.to_currency.total_commission_set

        self.helper.layout = Layout(
            HTML("<br>"),
            HTML("<h6 class=card-title> Transaction Details </h6><hr>"),
            Row(
                Column('sender_agent', css_class='form-group col-md-4 mb-3'),
                Column('receiver_agent', css_class='form-group col-md-4 mb-3'),
                Column('send_method', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('sender_cu', css_class='form-group col-md-4 mb-3'),
                Column('receiver_cu', css_class='form-group col-md-4 mb-3'),
                Column('receive_method', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('agent_bank', css_class='form-group col-md-4 mb-3'),
                Column('from_currency', css_class='form-group col-md-4 mb-3'),
                Column('to_currency', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('total_commission', css_class='form-group col-md-4 mb-3'),
                Column('transfer_rate', css_class='form-group col-md-4 mb-3'),
                Column('sending_amount', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('receiving_amount', css_class='form-group col-md-4 mb-3'),
                Column('paid_amount', css_class='form-group col-md-4 mb-3'),
                Column('total_payment', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('outstanding_amount', css_class='form-group col-md-4 mb-3'),
                Column('due_date', css_class='form-group col-md-4 mb-3'),
                Column('payment_status', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('reason_type', css_class='form-group col-md-4 mb-3'),
                Column('notification_type', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Notes Information </h6><hr>"),
            Row(
                Column('notes', css_class='form-group col-md-8 mb-3'),
                css_class='row'
            ),

        )


class EditMoneyTransferForm(forms.ModelForm):
    total_commission = forms.ModelChoiceField(queryset=CurrencyRate.objects.all(), to_field_name="total_commission")

    class Meta:
        model = MoneyTransfer
        fields = ('sender_agent', 'receiver_agent', 'sender_cu', 'receiver_cu', 'send_method',
                  'receive_method', 'agent_bank', 'from_currency', 'to_currency', 'total_commission',
                  'transfer_rate', 'sending_amount', 'receiving_amount', 'paid_amount', 'due_date',
                  'outstanding_amount', 'total_payment', 'payment_status', 'reason_type', 'notification_type', 'notes')

        widgets = {

            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),

        }

        labels = {

            'sender_agent': 'Sender Agent',
            'receiver_agent': 'Receiver Agent',
            'sender_cu': 'Sender Customer',
            'send_method': 'Sending Method',
            'receive_method': 'Receiving Method',
            'from_currency': 'Sending Currency',
            'to_currency': 'Receiving Currency',
            'total_commission': 'Exchange Rate',
            'transfer_rate': 'Transfer Rate',
            'sending_amount': 'Sending Amount',
            'receiving_amount': 'Receiving Amount',
            'paid_amount': 'Paid Amount',
            'outstanding_amount': 'Outstanding Amount',
            'total_payment': 'Total Payment',
            'payment_status': 'Payment Status',
            'reason_type': 'Reason For Sending',
            'notification_type': 'Notification',
            'notes': 'Notes (optional)',

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.fields['sender_agent'].queryset = MoneyUser.objects.filter(is_agent=True, is_active=True)
        self.fields['sender_cu'].queryset = MoneyUser.objects.filter(is_customer=True, is_active=True)
        self.fields['receiver_agent'].queryset = MoneyUser.objects.filter(is_agent=True, is_active=True)
        self.fields['receiver_cu'].queryset = MoneyUser.objects.filter(is_customer=True, is_active=True)
        # self.fields['to_currency'].queryset = MoneyTransfer.objects.none()
        # self.fields['total_commission'].queryset = MoneyTransfer.objects.none()
        self.helper.layout = Layout(
            HTML("<br>"),
            HTML("<h6 class=card-title> Transaction Details </h6><hr>"),
            Row(
                Column('sender_agent', css_class='form-group col-md-4 mb-3'),
                Column('receiver_agent', css_class='form-group col-md-4 mb-3'),
                Column('send_method', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('sender_cu', css_class='form-group col-md-4 mb-3'),
                Column('receiver_cu', css_class='form-group col-md-4 mb-3'),
                Column('receive_method', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('agent_bank', css_class='form-group col-md-4 mb-3'),
                Column('from_currency', css_class='form-group col-md-4 mb-3'),
                Column('to_currency', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('total_commission', css_class='form-group col-md-4 mb-3'),
                Column('transfer_rate', css_class='form-group col-md-4 mb-3'),
                Column('sending_amount', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('receiving_amount', css_class='form-group col-md-4 mb-3'),
                Column('paid_amount', css_class='form-group col-md-4 mb-3'),
                Column('total_payment', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('outstanding_amount', css_class='form-group col-md-4 mb-3'),
                Column('due_date', css_class='form-group col-md-4 mb-3'),
                Column('payment_status', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('reason_type', css_class='form-group col-md-4 mb-3'),
                Column('notification_type', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Notes Information </h6><hr>"),
            Row(
                Column('notes', css_class='form-group col-md-8 mb-3'),
                css_class='row'
            ),

        )


class DebtTransferForm(forms.ModelForm):
    sender_agent = forms.ModelChoiceField(queryset=MoneyUser.objects.filter(user_type='agent'))


    class Meta:
        model = DebtTransfer
        fields = ('paid_amount', 'due_date', 'outstanding_amount', 'receiver_customer',
        'sender_agent','sending_amount','from_currency','to_currency','total_commission', 'debt','debt_id')

        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'})

        }
        labels = {
            'due_date': 'Choose Next Payment Due Date',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['outstanding_amount'].widget.attrs['readonly'] = True
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('paid_amount', css_class='form-group col-md-4 mb-3'),
                Column('due_date', css_class='form-group col-md-4 mb-3'),
                Column('outstanding_amount', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('sender_agent', css_class='form-group col-md-4 mb-3'),
                Column('receiver_customer', css_class='form-group col-md-4 mb-3'),
                Column('from_currency', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('sending_amount', css_class='form-group col-md-4 mb-3'),
                Column('debt_id', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),

        )
