from exchange.models import MoneyExchange
from administration.models import CurrencyRate
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML



class MoneyExchangeForm(forms.ModelForm):

    exchange_rate = forms.ModelChoiceField(queryset=CurrencyRate.objects.all(), to_field_name="total_commission")

    class Meta:
          model = MoneyExchange
          fields = ('buying_currency','selling_currency','buying_amount','selling_amount', 'exchange_rate',
          'customer_info', 'customer_name', 'photo_id', 'first_name', 'last_name', 'mobile_no', 'address',
          'assign_agent','city', 'postal_code', 'state', 'country')

          widgets={
              'mobile_no': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),
                        
              
          }

          labels={
              'buying_currency' :'Buying Currency',
              'selling_currency' :'Selling Currency',
              'buying_amount' :'Buying Amount',
              'selling_amount' : 'Selling Amount',
              'exchange_rate' :'Exchange Rate',
              'customer_info' :'Customer (optional)',
              'photo_id' :'Photo ID',
              'first_name' :'First Name',
              'last_name' :'Last Name',
              'mobile_no' :'Mobile Number',
              'address' : 'Address',
              'assign_agent' : 'Assigned Agent',
              'city' : 'City',
              'postal_code' : 'Postal Code (optional)',
              'state' : 'State (optional)',
              'country' : 'Country',

          }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.fields['selling_amount'].widget.attrs['readonly'] = True
        # self.fields['exchange_rate'].queryset = MoneyExchange.objects.none()
        self.helper.layout = Layout(
            HTML("<br>"),
            HTML("<h6 class=card-title> Basic Informantion </h6><hr>"),
            Row(
                Column('buying_currency', css_class='form-group col-md-4 mb-3'),
                Column('buying_amount', css_class='form-group col-md-4 mb-3'),
                Column('exchange_rate', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('selling_currency', css_class='form-group col-md-4 mb-3'),
                Column('selling_amount', css_class='form-group col-md-4 mb-3'),
                Column('assign_agent', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Customer Information </h6><hr>"),
            Row(
                Column('customer_info', css_class='form-group col-md-4 mb-3'),
                Column('customer_name', css_class='form-group col-md-4 mb-3'),
                Column('photo_id', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('first_name', css_class='form-group col-md-4 mb-3'),
                Column('last_name', css_class='form-group col-md-4 mb-3'),
                Column('mobile_no', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('address', css_class='form-group col-md-4 mb-3'),
                Column('city', css_class='form-group col-md-4 mb-3'),
                Column('postal_code', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('state', css_class='form-group col-md-4 mb-3'),
                Column('country', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            

        )      



class EditMoneyExchangeForm(forms.ModelForm):
   
    exchange_rate = forms.ModelChoiceField(queryset=CurrencyRate.objects.all(), to_field_name="total_commission")

    class Meta:
          model = MoneyExchange
          fields = ('buying_currency','selling_currency','buying_amount','selling_amount', 'exchange_rate',
          'customer_info', 'customer_name', 'photo_id', 'first_name', 'last_name', 'mobile_no', 'address',
          'assign_agent','city', 'postal_code', 'state', 'country')

          widgets={
              'mobile_no': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),
                        
              
          }

          labels={
              'buying_currency' :'Buying Currency',
              'selling_currency' :'Selling Currency',
              'buying_amount' :'Buying Amount',
              'selling_amount' : 'Selling Amount',
              'exchange_rate' :'Exchange Rate',
              'customer_info' :'Customer (optional)',
              'photo_id' :'Photo ID',
              'first_name' :'First Name',
              'last_name' :'Last Name',
              'mobile_no' :'Mobile Number',
              'address' : 'Address',
              'assign_agent' : 'Assigned Agent',
              'city' : 'City',
              'postal_code' : 'Postal Code (optional)',
              'state' : 'State (optional)',
              'country' : 'Country',

          }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.fields['selling_amount'].widget.attrs['readonly'] = True
        # self.fields['exchange_rate'].queryset = MoneyExchange.objects.none()
        self.helper.layout = Layout(
            HTML("<br>"),
            HTML("<h6 class=card-title> Basic Informantion </h6><hr>"),
            Row(
                Column('buying_currency', css_class='form-group col-md-4 mb-3'),
                Column('buying_amount', css_class='form-group col-md-4 mb-3'),
                Column('exchange_rate', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('selling_currency', css_class='form-group col-md-4 mb-3'),
                Column('selling_amount', css_class='form-group col-md-4 mb-3'),
                Column('assign_agent', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Customer Information </h6><hr>"),
            Row(
                Column('customer_info', css_class='form-group col-md-4 mb-3'),
                Column('customer_name', css_class='form-group col-md-4 mb-3'),
                Column('photo_id', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('first_name', css_class='form-group col-md-4 mb-3'),
                Column('last_name', css_class='form-group col-md-4 mb-3'),
                Column('mobile_no', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('address', css_class='form-group col-md-4 mb-3'),
                Column('city', css_class='form-group col-md-4 mb-3'),
                Column('postal_code', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('state', css_class='form-group col-md-4 mb-3'),
                Column('country', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            

        )      
