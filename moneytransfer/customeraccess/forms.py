from customeraccess.models import Receiver, SendMoney
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML



class ReceiverForm(forms.ModelForm):

    class Meta:
          model = Receiver
          fields = ('title_type','first_name','last_name','email',
          'mobile_no', 'city', 'country', 'account_name', 'account_no',
          'branch_code', 'bank_name', 'bank_contact', 'bank_email', 'description')

          widgets={
              'email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'mobile_no': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),
              'description' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),
              'bank_email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'bank_contact': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),

              
              
          }

          labels={
              'title_type' :'Title',
              'first_name' :'First Name',
              'last_name' :'Last Name',
              'email' : 'Email',
              'mobile_no' :'Mobile Number',
              'city' :'City',
              'country' :'Country',
              'account_name' : 'Account Name',
              'account_no' : 'Account Number',
              'branch_code' : 'Bank BranchCode',
              'bank_name' : 'Bank Name',
              'bank_contact' : 'Bank Contact Number (optional)',
              'bank_email' : 'Bank Email (optional)',  
              'description' : 'Description (optional)'

          }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            HTML("<br>"),
            HTML("<h6 class=card-title> Basic Information </h6><hr>"),
            Row(
                Column('title_type', css_class='form-group col-md-4 mb-3'),
                Column('first_name', css_class='form-group col-md-4 mb-3'),
                Column('last_name', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='form-group col-md-4 mb-3'),
                Column('mobile_no', css_class='form-group col-md-4 mb-3'),
                Column('city', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            Row(
                Column('country', css_class='form-group col-md-4 mb-3'),
                Column('city', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Bank Information </h6><hr>"),
            Row(
                Column('account_name', css_class='form-group col-md-4 mb-3'),
                Column('account_no', css_class='form-group col-md-4 mb-3'),
                Column('branch_code', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            Row(
                Column('bank_name', css_class='form-group col-md-4 mb-3'),
                Column('bank_contact', css_class='form-group col-md-4 mb-3'),
                Column('bank_email', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Description </h6><hr>"),
            Row(
                Column('description', css_class='form-group col-md-8 mb-3'),
                css_class='row'            

            ),
            
        )      

class EditReceiverForm(forms.ModelForm):

    class Meta:
          model = Receiver
          fields = ('title_type','first_name','last_name','email',
          'mobile_no', 'city', 'country', 'account_name', 'account_no',
          'branch_code', 'bank_name', 'bank_contact', 'bank_email', 'description')

          widgets={
              'email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'mobile_no': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),
              'description' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),
              'bank_email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'bank_contact': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),

              
              
          }

          labels={
              'title_type' :'Title',
              'first_name' :'First Name',
              'last_name' :'Last Name',
              'email' : 'Email',
              'mobile_no' :'Mobile Number',
              'city' :'City',
              'country' :'Country',
              'account_name' : 'Account Name',
              'account_no' : 'Account Number',
              'branch_code' : 'Bank BranchCode',
              'bank_name' : 'Bank Name',
              'bank_contact' : 'Bank Contact Number (optional)',
              'bank_email' : 'Bank Email (optional)',  
              'description' : 'Description (optional)'

          }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            HTML("<br>"),
            HTML("<h6 class=card-title> Basic Information </h6><hr>"),
            Row(
                Column('title_type', css_class='form-group col-md-4 mb-3'),
                Column('first_name', css_class='form-group col-md-4 mb-3'),
                Column('last_name', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='form-group col-md-4 mb-3'),
                Column('mobile_no', css_class='form-group col-md-4 mb-3'),
                Column('city', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            Row(
                Column('country', css_class='form-group col-md-4 mb-3'),
                Column('city', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Bank Information </h6><hr>"),
            Row(
                Column('account_name', css_class='form-group col-md-4 mb-3'),
                Column('account_no', css_class='form-group col-md-4 mb-3'),
                Column('branch_code', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            Row(
                Column('bank_name', css_class='form-group col-md-4 mb-3'),
                Column('bank_contact', css_class='form-group col-md-4 mb-3'),
                Column('bank_email', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Description </h6><hr>"),
            Row(
                Column('description', css_class='form-group col-md-8 mb-3'),
                css_class='row'            

            ),
            
        )      


class SendMoneyForm(forms.ModelForm):

    
    class Meta:
          model = SendMoney
          fields = ('receiver','from_currency','to_currency','our_rate','transfer_rate',
          'send_amount', 'total_amount', 'receive_amount','send_method', 'receive_method',
          'account_name', 'account_no', 'branch_code', 'bank_name', 'reason_type', 'bank_email',
          'money_status', 'description')

          widgets={
            
               'description' : forms.Textarea(attrs={'placeholder': 'Write Your Description'}),
           
              
              
          }

          labels={
              'receiver' :'Receiver Name',
              'from_currency' :'From Currency',
              'to_currency' :'To Currency',
              'our_rate' : ' Exchange Rate',
              'transfer_rate' : 'Transfer Rate',
              'send_amount' : 'Send Amount',
              'receive_amount' : 'Receive Amount',
              'total_amount' : 'Transfer Total',
              'send_method' : 'Send Money To',
              'receive_method' : 'Receive Money From',
              'account_name' : 'Account Name',
              'account_no' : 'Account Number',
              'branch_code' : 'Bank BranchCode',
              'bank_name' : 'Bank Name',
              'money_status' : 'Transfer Status',
              'description' : 'Description',
              'reason_type' : 'Reason Type',
          }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.fields['receive_amount'].widget.attrs['readonly'] = True
        self.fields['total_amount'].widget.attrs['readonly'] = True
        self.helper.layout = Layout(
            HTML("<br>"),
            HTML("<h6 class=card-title> Send Money </h6><hr>"),
            Row(
                Column('receiver', css_class='form-group col-md-4 mb-3'),
                Column('from_currency', css_class='form-group col-md-4 mb-3'),
                Column('to_currency', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('our_rate', css_class='form-group col-md-4 mb-3'),
                Column('transfer_rate', css_class='form-group col-md-4 mb-3'),
                Column('send_amount', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            Row(
                Column('receive_amount', css_class='form-group col-md-4 mb-3'),
                Column('total_amount', css_class='form-group col-md-4 mb-3'),
                Column('send_method', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            Row(
                Column('receive_method', css_class='form-group col-md-4 mb-3'),
                Column('account_name', css_class='form-group col-md-4 mb-3'),
                Column('account_no', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            # HTML("<br>"),
            # HTML("<h6 class=card-title> Bank Information </h6><hr>"),
            Row(
                Column('branch_code', css_class='form-group col-md-4 mb-3'),
                Column('bank_name', css_class='form-group col-md-4 mb-3'),
                Column('reason_type', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Description </h6><hr>"),
            Row(
                Column('description', css_class='form-group col-md-8 mb-3'),
                css_class='row'            

            ),
            
        )      
