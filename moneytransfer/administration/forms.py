from django import forms
from administration.models import BankUser, CurrencyRate, Faq, MoneyUser, ReasonType
from django.contrib.auth.forms import UserChangeForm, UserCreationForm, PasswordChangeForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, HTML, Field
from django.core.exceptions import ValidationError

"**************************************NEW-AGENT-FORM************************************"     


class AgentForm(UserCreationForm):

    STATUS = (
        ('False', 'Inactive'),
        ('True', 'Active'),
    )
    is_active = forms.ChoiceField(choices=STATUS, label='Status')

    class Meta:
          model = MoneyUser
          fields = ('title_type','first_name','last_name','email','notes',
          'mobile_no', 'dob', 'address', 'city', 'postal_code', 'country', 'nationality', 'is_active')

          widgets={
              'email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'mobile_no': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),
              'dob': forms.DateInput(attrs={'type': 'date'}),
              'notes' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),
              
              
          }

          labels={
              'title_type' :'Title',
              'first_name' :'First Name',
              'last_name' :'Last Name',
              'email' : 'Email',
              'mobile_no' :'Mobile Number',
              'address' :'Address',
              'city' :'City',
              'postal_code' :'Postal Code (optional)',
              'country' :'Country',
              'is_active' :'Status',
              'notes' : 'Notes (optional)'

          }
         
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            HTML("<br>"),
            HTML("<h6 class=card-title>  Info </h6><hr>"),
            Row(
                Column('title_type', css_class='form-group col-md-4 mb-3'),
                Column('first_name', css_class='form-group col-md-4 mb-3'),
                Column('last_name', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='form-group col-md-4 mb-3'),
                Column('mobile_no', css_class='form-group col-md-4 mb-3'),
                Column('dob', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-4 mb-3'),
                Column('password2', css_class='form-group col-md-4 mb-3'),
                Column('is_active', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Address Info </h6><hr>"),
            Row(
                Column('address', css_class='form-group col-md-4 mb-3'),
                Column('city', css_class='form-group col-md-4 mb-3'),
                Column('postal_code', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('country', css_class='form-group col-md-4 mb-3'),
                Column('nationality', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Notes Info </h6><hr>"),
            Row(
                Column('notes', css_class='form-group col-md-8 mb-3'),
                css_class='row'
            ),

            
        )      
def save(self, commit=True):
    user = super(AgentForm, self).save(commit=False)
    user.title_type = self.cleaned_data["title_type"]
    user.first_name = self.cleaned_data["first_name"]
    user.last_name = self.cleaned_data["last_name"]
    user.mobile_no = self.cleaned_data["mobile_no"]
    user.city = self.cleaned_data["city"]
    user.postal_code = self.cleaned_data["postal_code"]
    user.country = self.cleaned_data["country"]
    user.nationality = self.cleaned_data["nationality"]
    user.status = self.cleaned_data["status"]
    
    if commit:
        user.save()
    return user

"**************************************EDIT-AGENT-FORM************************************"     

class EditAgentForm(forms.ModelForm):
    
    STATUS = (
        ('False', 'Inactive'),
        ('True', 'Active'),
    )
    is_active = forms.ChoiceField(choices=STATUS, label='Status')
    class Meta:
          model = MoneyUser
          fields = ('title_type','first_name','last_name','email','notes',
          'mobile_no', 'dob', 'address', 'city', 'postal_code', 'country', 'nationality', 'is_active')


          widgets={
              'email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'mobile_no': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),
              'dob': forms.DateInput(attrs={'type': 'date'}),
              'notes' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),
              
          }

          labels={
              'title_type' :'Title',
              'first_name' :'First Name',
              'last_name' :'Last Name',
              'email' : 'Email',
              'mobile_no' :'Mobile Number',
              'address' :'Address',
              'city' :'City',
              'postal_code' :'Postal Code (optional)',
              'country' :'Country',
              'is_active' :'Status',
              'notes' : 'Notes (optional)',

          }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            HTML("<br>"),
            HTML("<h6 class=card-title> Basic Info </h6><hr>"),
            Row(
                Column('title_type', css_class='form-group col-md-4 mb-3'),
                Column('first_name', css_class='form-group col-md-4 mb-3'),
                Column('last_name', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='form-group col-md-4 mb-3'),
                Column('mobile_no', css_class='form-group col-md-4 mb-3'),
                Column('dob', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(    
                Column('is_active', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Address Info </h6><hr>"),
            Row(    
                Column('address', css_class='form-group col-md-4 mb-3'),
                Column('city', css_class='form-group col-md-4 mb-3'),
                Column('postal_code', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(       
                Column('country', css_class='form-group col-md-4 mb-3'),
                Column('nationality', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Notes Info </h6><hr>"),
            Row(
                Column('notes', css_class='form-group col-md-8 mb-3'),
                css_class='row'
            ),
            
            
        )   

class AgentChangeForm(UserChangeForm):

    
    class Meta:
        model = MoneyUser
        fields = ['first_name', 'last_name', 'email', 'mobile_no', 'notes']
        
        widgets={
              'email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'mobile_no': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),
              'notes' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),
              
          }

        labels={
              'first_name' :'First Name',
              'last_name' :'Last Name',
              'email' : 'Email',
              'mobile_no' :'Mobile Number',
              'notes' : 'Notes (optional)',

          }

        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-3'),
                Column('last_name', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-3'),
                Column('mobile_no', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            'notes',
            
        )      
def save(self, commit=True):
    user = super(AgentChangeForm, self).save(commit=False)
    user.first_name = self.cleaned_data["first_name"]
    user.last_name = self.cleaned_data["last_name"]
    user.mobile_no = self.cleaned_data["mobile_no"]
    
    
    if commit:
        user.save()
    return user


class CustomerChangeForm(UserChangeForm):
    
    class Meta:
        model = MoneyUser
        fields = ['first_name', 'last_name', 'email', 'mobile_no', 'notes']


        widgets={
              'email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'mobile_no': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),
              'notes' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),
              
          }

        labels={
              'first_name' :'First Name',
              'last_name' :'Last Name',
              'email' : 'Email',
              'mobile_no' :'Mobile Number',
              'notes' : 'Notes (optional)',

          }


    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-3'),
                Column('last_name', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('email', css_class='form-group col-md-6 mb-3'),
                Column('mobile_no', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            'notes',

            
        )      
def save(self, commit=True):
    user = super(CustomerChangeForm, self).save(commit=False)
    user.first_name = self.cleaned_data["first_name"]
    user.last_name = self.cleaned_data["last_name"]
    user.mobile_no = self.cleaned_data["mobile_no"]
    
    
    if commit:
        user.save()
    return user


class PasswordChangeForm(PasswordChangeForm):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('old_password', css_class='form-group col-md-6 mb-3'),
                Column('new_password1', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('new_password2', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            
        )
    



    



"**************************************NEW-CUSTOMER-FORM************************************"     
class CustomerForm(UserCreationForm):
    STATUS = (
        ('False', 'Inactive'),
        ('True', 'Active'),
    )
    is_active = forms.ChoiceField(choices=STATUS, label='Status')
    # def clean(self):
 
    #     # data from the form is fetched using super function
    #     super(CustomerForm, self).clean()
         
    #     # extract the username and text field from the data
    #     documents_type = self.cleaned_data.get('documents_type')
    #     first_name = self.cleaned_data.get('first_name')
    #     last_name = self.cleaned_data.get('last_name')
 
    #     # conditions to be met for the username length
    #     if documents_type != 'other':
    #         self._errors['documents_type'] = self.error_class([
    #             'Select other Field required'])
    #     if len(last_name) <10:
    #         self._errors['last_name'] = self.error_class([
    #             'Post Should Contain a minimum of 10 characters'])

    #     if first_name == "":
    #         self._errors['first_name'] = self.error_class([
    #             'Post Should Contain a minimum of 10 characters'])        
 
    #     # return any errors if found
    #     return self.cleaned_data

    class Meta:
          model = MoneyUser
          fields = ('title_type','first_name','last_name','arabic_name', 'email','office_no', 'home_no',
          'mobile_no', 'dob', 'address', 'city', 'postal_code', 'country', 'nationality',
          'documents_type', 'document_upload', 'document_no', 'doc_start_date', 'doc_end_date',
          'prof_address', 'notes', 'is_active')

          widgets={
              'email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'mobile_no': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),
              'dob': forms.DateInput(attrs={'type': 'date'}),
              'doc_start_date': forms.DateInput(attrs={'type': 'date'}),
              'doc_end_date': forms.DateInput(attrs={'type': 'date'}),
              'document_upload': forms.FileInput(attrs={'class': 'form-control'}),
              'notes' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),
              'arabic_name' : forms.TextInput(attrs={'dir': 'rtl',}),


              
          }
    

          labels={
              'title_type' :'Title',
              'first_name' :'First Name',
              'last_name' :'Last Name',
              'arabic_name' : 'Arabic Name (optional)',
              'email' : 'Email',
              'office_no' : 'Office Phone Number (optional)',
              'home_no' : 'Home Phone Number (optional)',
              'mobile_no' :'Mobile Number',
              'address' :'Address',
              'city' :'City',
              'postal_code' :'Postal Code (optional)',
              'country' :'Country',
              'nationality' : 'Nationality',
              'documents_type' : 'Document Type (optional)',
              'document_upload' : 'Document Upload (optional)',
              'document_no' : 'Document Number (optional)',
              'doc_start_date' : 'Date Start (optional)',
              'doc_end_date' : 'Date End (optional)',
              'prof_address' : 'Proof of Address (optional)',
              'notes' : 'Notes (optional)',
              'is_active' :'Status',

          }  
    
          
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            HTML("<br>"),
            HTML("<h6 class=card-title> Basic Info </h6><hr>"),
            Row(
                Column('title_type', css_class='form-group col-md-4 mb-3'),
                Column('first_name', css_class='form-group col-md-4 mb-3'),
                Column('last_name', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('arabic_name', css_class='form-group col-md-4 mb-3'),
                Column('email', css_class='form-group col-md-4 mb-3'),
                Column('mobile_no', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('office_no', css_class='form-group col-md-4 mb-3'),
                Column('home_no', css_class='form-group col-md-4 mb-3'),
                Column('dob', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('password1', css_class='form-group col-md-4 mb-3'),
                Column('password2', css_class='form-group col-md-4 mb-3'),
                Column('is_active', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Address Info </h6><hr>"),
            Row(
                Column('address', css_class='form-group col-md-4 mb-3'),
                Column('city', css_class='form-group col-md-4 mb-3'),
                Column('country', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('postal_code', css_class='form-group col-md-4 mb-3'),
                Column('nationality', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Document Info </h6><hr>"),
            Row(
                Column('documents_type', css_class='form-group col-md-4 mb-3'),
                Column('document_upload', css_class='form-group col-md-4 mb-3'),
                Column('document_no', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('doc_start_date', css_class='form-group col-md-4 mb-3'),
                Column('doc_end_date', css_class='form-group col-md-4 mb-3'),
                Column('prof_address', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Notes Info </h6><hr>"),
            Row(
                Column('notes', css_class='form-group col-md-8 mb-3'),
                css_class='row'
            ),

        )      

def save(self, commit=True):
    user = super(AgentForm, self).save(commit=False)
    user.title_type = self.cleaned_data["title_type"]
    user.first_name = self.cleaned_data["first_name"]
    user.last_name = self.cleaned_data["last_name"]
    user.mobile_no = self.cleaned_data["mobile_no"]
    user.office_no = self.cleaned_data["office_no"]
    user.postal_code = self.cleaned_data["postal_code"]
    user.country = self.cleaned_data["country"]
    user.nationality = self.cleaned_data["nationality"]
    user.home_no = self.cleaned_data["home_no"]
    user.documents_type = self.cleaned_data["documents_type"]
    user.document_upload = self.cleaned_data["document_upload"]
    user.doc_start_date = self.cleaned_data["doc_start_date"]
    user.doc_end_date = self.cleaned_data["doc_end_date"]
    user.notes = self.cleaned_data["notes"]
   
    
    if commit:
        user.save()
    return user

"**************************************EDIT-CUSTOMER-FORM************************************"     

class EditCustomerForm(forms.ModelForm):
    STATUS = (
        ('False', 'Inactive'),
        ('True', 'Active'),
    )
    is_active = forms.ChoiceField(choices=STATUS, label='Status')

    
    class Meta:
          model = MoneyUser
          fields = ('title_type','first_name','last_name','arabic_name', 'email','office_no', 'home_no',
          'mobile_no', 'dob', 'address', 'city', 'postal_code', 'country', 'nationality',
          'documents_type', 'document_upload', 'document_no', 'doc_start_date', 'doc_end_date',
          'prof_address', 'notes', 'is_active')

          widgets={
              'email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'mobile_no': forms.TextInput(attrs={ 'placeholder': '+90123456789'}),
              'dob': forms.DateInput(attrs={'type': 'date'}),
              'doc_start_date': forms.DateInput(attrs={'type': 'date'}),
              'doc_end_date': forms.DateInput(attrs={'type': 'date'}),
              'document_upload': forms.FileInput(attrs={'class': 'form-control'}),
              'notes' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),

              
          }

          labels={
              'title_type' :'Title',
              'first_name' :'First Name',
              'last_name' :'Last Name',
              'arabic_name' : 'Arabic Name (optional)',
              'email' : 'Email',
              'office_no' : 'Office Phone Number (optional)',
              'home_no' : 'Home Phone Number (optional)',
              'mobile_no' :'Mobile Number',
              'address' :'Address',
              'city' :'City',
              'postal_code' :'Postal Code (optional)',
              'country' :'Country',
              'nationality' : 'Nationality',
              'documents_type' : 'Document Type (optional)',
              'document_upload' : 'Document Upload (optional)',
              'document_no' : 'Document Number (optional)',
              'doc_start_date' : 'Date Start (optional)',
              'doc_end_date' : 'Date End (optional)',
              'prof_address' : 'Proof of Address (optional)',
              'notes' : 'Notes (optional)',
              'is_active' :'Status',

          }  
          
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            HTML("<br>"),
            HTML("<h6 class=card-title> Basic Info </h6><hr>"),
            Row(
                Column('title_type', css_class='form-group col-md-4 mb-3'),
                Column('first_name', css_class='form-group col-md-4 mb-3'),
                Column('last_name', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('arabic_name', css_class='form-group col-md-4 mb-3'),
                Column('email', css_class='form-group col-md-4 mb-3'),
                Column('mobile_no', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('office_no', css_class='form-group col-md-4 mb-3'),
                Column('home_no', css_class='form-group col-md-4 mb-3'),
                Column('dob', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('is_active', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Address Info </h6><hr>"),
            Row(
                Column('address', css_class='form-group col-md-4 mb-3'),
                Column('city', css_class='form-group col-md-4 mb-3'),
                Column('country', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('postal_code', css_class='form-group col-md-4 mb-3'),
                Column('nationality', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Document Info </h6><hr>"),
            Row(
                Column('documents_type', css_class='form-group col-md-4 mb-3'),
                Column('document_upload', css_class='form-group col-md-4 mb-3'),
                Column('document_no', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('doc_start_date', css_class='form-group col-md-4 mb-3'),
                Column('doc_end_date', css_class='form-group col-md-4 mb-3'),
                Column('prof_address', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            HTML("<br>"),
            HTML("<h6 class=card-title> Notes Info </h6><hr>"),
            Row(
                Column('notes', css_class='form-group col-md-8 mb-3'),
                css_class='row'
            ),

        )   
        
def save(self, commit=True):
    user = super(AgentForm, self).save(commit=False)
    user.title_type = self.cleaned_data["title_type"]
    user.first_name = self.cleaned_data["first_name"]
    user.last_name = self.cleaned_data["last_name"]
    user.mobile_no = self.cleaned_data["mobile_no"]
    user.office_no = self.cleaned_data["office_no"]
    user.postal_code = self.cleaned_data["postal_code"]
    user.country = self.cleaned_data["country"]
    user.nationality = self.cleaned_data["nationality"]
    user.home_no = self.cleaned_data["home_no"]
    user.documents_type = self.cleaned_data["documents_type"]
    user.document_upload = self.cleaned_data["document_upload"]
    user.doc_start_date = self.cleaned_data["doc_start_date"]
    user.doc_end_date = self.cleaned_data["doc_end_date"]
    user.notes = self.cleaned_data["notes"]
   
    
    if commit:
        user.save()
    return user
         

"**************************************NEW-CURRENCY-FORM************************************"  

class CurrencyForm(forms.ModelForm):
    class Meta:
          model = CurrencyRate
          fields = ('from_currency','to_currency','market_rate','our_rate',
          'total_commission', )


          
          labels={
                'from_currency' :'From Currency',
                'to_currency' :'To Currency',
                'market_rate' : 'Market Rate',
                'our_rate' :'Our Rate',
                'total_commission' : 'Total Commmission',

          }

    
   


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.fields['total_commission'].widget.attrs['readonly'] = True
        self.helper.layout = Layout(
            Row(
                Column('from_currency', css_class='form-group col-md-6 mb-3'),
                Column('to_currency', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('market_rate', css_class='form-group col-md-6 mb-3'),
                Column('our_rate', css_class='form-group col-md-6 mb-3'),                
                css_class='row'
            ),
            Row(
                Column('total_commission', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),      
        )      

"**************************************EDIT-CURRENCY-FORM************************************"  

class EditCurrencyForm(forms.ModelForm):

    class Meta:
          model = CurrencyRate
          fields = ('from_currency','to_currency','market_rate','our_rate',
          'total_commission')

          labels={
            'from_currency' :'From Currency',
            'to_currency' :'To Currency',
            'market_rate' : 'Market Rate',
            'our_rate' :'Our Rate',
            'total_commission' : 'Total Commmission',

           }      


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.fields['total_commission'].widget.attrs['readonly'] = True
        self.helper.layout = Layout(
            Row(
                Column('from_currency', css_class='form-group col-md-6 mb-3'),
                Column('to_currency', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),
            Row(
                Column('market_rate', css_class='form-group col-md-6 mb-3'),
                Column('our_rate', css_class='form-group col-md-6 mb-3'),                
                css_class='row'
            ),
            Row(
                Column('total_commission', css_class='form-group col-md-6 mb-3'),
                css_class='row'
            ),      
        )      

"**************************************REASON-FORM************************************"  

class ReasonForm(forms.ModelForm):

    class Meta:
        model = ReasonType
        fields=('reason_type',)

        labels={
         'reason_type' :'Reason Type',

         }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('reason_type', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            
        )

"**************************************EDIT-REASON-FORM************************************"  

class EditReasonForm(forms.ModelForm):

    class Meta:
        model = ReasonType
        fields=('reason_type',)

        labels={
            'reason_type' :'Reason Type',

        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('reason_type', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            
        )


"**************************************AGENT-BANK-FORM************************************"  
class AgentBankForm(forms.ModelForm):

    class Meta:
          model = BankUser
          fields = ('bank_name','bank_branch_code','bank_address','bank_email',
          'bank_agent', 'account_name', 'bank_contact', 'bank_country', 'notes', 
          'account_no', 'account_type', 'sort_code', 'iban', 'swift_code')

          widgets={
              'bank_email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'bank_contact': forms.TextInput(attrs={ 'placeholder': 'Enter Bank Contact No'}),
              'notes' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),
              
              
          }

          labels={
               'bank_name' :'Bank Name',
               'bank_branch_code' : 'Bank Brach Code',
               'bank_address' : 'Bank Address',
               'bank_email' : 'Bank Email',
               'bank_agent' : 'Bank Agent',
               'account_name' : 'Accout Name',
               'bank_contact' : 'Bank Contact',
               'bank_country' : 'Bank Country',
               'notes' : 'Notes (optional)',
               'account_no' : 'Account Number',
               'account_type' : 'Account Type',
               'sort_code' : 'Sort Code',
               'iban' : 'Iban',
               'swift_code' : 'Swift Code',

              }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('bank_name', css_class='form-group col-md-4 mb-3'),
                Column('bank_branch_code', css_class='form-group col-md-4 mb-3'),
                Column('bank_address', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('bank_email', css_class='form-group col-md-4 mb-3'),
                Column('bank_agent', css_class='form-group col-md-4 mb-3'),
                Column('account_name', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(  
                Column('account_no', css_class='form-group col-md-4 mb-3'),
                Column('account_type', css_class='form-group col-md-4 mb-3'),
                Column('swift_code', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('sort_code', css_class='form-group col-md-4 mb-3'),
                Column('iban', css_class='form-group col-md-4 mb-3'),
                Column('bank_country', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            Row(
                Column('notes', css_class='form-group col-md-8 mb-3'),
                css_class='row'            
            ),
            
        )      

"**************************************EDIT-AGENT-BANK-FORM************************************"  

class EditAgentBankForm(forms.ModelForm):

    class Meta:
          model = BankUser
          fields = ('bank_name','bank_branch_code','bank_address','bank_email',
          'bank_agent', 'account_name', 'bank_contact', 'bank_country', 'notes', 
          'account_no', 'account_type', 'sort_code', 'iban', 'swift_code', 'bank_country',
          'notes')

          widgets={
              'bank_email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'bank_contact': forms.TextInput(attrs={ 'placeholder': 'Enter Bank Contact No'}),
              'notes' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),
              
              
          }

          labels={
               'bank_name' :'Bank Name',
               'bank_branch_code' : 'Bank Brach Code',
               'bank_address' : 'Bank Address',
               'bank_email' : 'Bank Email',
               'bank_agent' : 'Bank Agent',
               'account_name' : 'Accout Name',
               'bank_contact' : 'Bank Contact',
               'bank_country' : 'Bank Country',
               'notes' : 'Notes (optional)',
               'account_no' : 'Account Number',
               'account_type' : 'Account Type',
               'sort_code' : 'Sort Code',
               'iban' : 'Iban',
               'swift_code' : 'Swift Code',

              }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('bank_name', css_class='form-group col-md-4 mb-3'),
                Column('bank_branch_code', css_class='form-group col-md-4 mb-3'),
                Column('bank_address', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('bank_email', css_class='form-group col-md-4 mb-3'),
                Column('bank_agent', css_class='form-group col-md-4 mb-3'),
                Column('account_name', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(  
                Column('account_no', css_class='form-group col-md-4 mb-3'),
                Column('account_type', css_class='form-group col-md-4 mb-3'),
                Column('swift_code', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('sort_code', css_class='form-group col-md-4 mb-3'),
                Column('iban', css_class='form-group col-md-4 mb-3'),
                Column('bank_country', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            Row(
                Column('notes', css_class='form-group col-md-8 mb-3'),
                css_class='row'            
            ),
            
        )      

"**************************************CUSTOMER-BANK-FORM************************************"  
class CustomerBankForm(forms.ModelForm):

    class Meta:
          model = BankUser
          fields = ('bank_name','bank_branch_code','bank_address','bank_email',
          'bank_customer', 'account_name', 'bank_contact', 'bank_country', 'notes', 
          'account_no', 'account_type', 'sort_code', 'iban', 'swift_code', 'bank_country',
          'notes')

          widgets={
              'bank_email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'bank_contact': forms.TextInput(attrs={ 'placeholder': 'Enter Bank Contact No'}),
              'notes' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),
              
              
          }

          labels={
               'bank_name' :'Bank Name',
               'bank_branch_code' : 'Bank Brach Code',
               'bank_address' : 'Bank Address',
               'bank_email' : 'Bank Email',
               'bank_customer' : 'Bank Customer',
               'account_name' : 'Accout Name',
               'bank_contact' : 'Bank Contact',
               'bank_country' : 'Bank Country',
               'notes' : 'Notes (optional)',
               'account_no' : 'Account Number',
               'account_type' : 'Account Type',
               'sort_code' : 'Sort Code',
               'iban' : 'Iban',
               'swift_code' : 'Swift Code',

              }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('bank_name', css_class='form-group col-md-4 mb-3'),
                Column('bank_branch_code', css_class='form-group col-md-4 mb-3'),
                Column('bank_address', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('bank_email', css_class='form-group col-md-4 mb-3'),
                Column('bank_customer', css_class='form-group col-md-4 mb-3'),
                Column('account_name', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(  
                Column('account_no', css_class='form-group col-md-4 mb-3'),
                Column('account_type', css_class='form-group col-md-4 mb-3'),
                Column('swift_code', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('sort_code', css_class='form-group col-md-4 mb-3'),
                Column('iban', css_class='form-group col-md-4 mb-3'),
                Column('bank_country', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            Row(
                Column('notes', css_class='form-group col-md-8 mb-3'),
                css_class='row'            
            ),
            
        )      

"**************************************EDIT-AGENT-BANK-FORM************************************"  

class EditCustomerBankForm(forms.ModelForm):

    class Meta:
          model = BankUser
          fields = ('bank_name','bank_branch_code','bank_address','bank_email',
          'bank_customer', 'account_name', 'bank_contact', 'bank_country', 'notes', 
          'account_no', 'account_type', 'sort_code', 'iban', 'swift_code', 'bank_country',
          'notes')

          widgets={
              'bank_email': forms.TextInput(attrs={ 'placeholder': 'example@email.com'}),
              'bank_contact': forms.TextInput(attrs={ 'placeholder': 'Enter Bank Contact No'}),
              'notes' : forms.Textarea(attrs={'placeholder': 'Write Your Notes'}),
              
              
          }

          labels={
               'bank_name' :'Bank Name',
               'bank_branch_code' : 'Bank Brach Code',
               'bank_address' : 'Bank Address',
               'bank_email' : 'Bank Email',
               'bank_customer' : 'Bank Customer',
               'account_name' : 'Accout Name',
               'bank_contact' : 'Bank Contact',
               'bank_country' : 'Bank Country',
               'notes' : 'Notes (optional)',
               'account_no' : 'Account Number',
               'account_type' : 'Account Type',
               'sort_code' : 'Sort Code',
               'iban' : 'Iban',
               'swift_code' : 'Swift Code',

              }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('bank_name', css_class='form-group col-md-4 mb-3'),
                Column('bank_branch_code', css_class='form-group col-md-4 mb-3'),
                Column('bank_address', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('bank_email', css_class='form-group col-md-4 mb-3'),
                Column('bank_customer', css_class='form-group col-md-4 mb-3'),
                Column('account_name', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(  
                Column('account_no', css_class='form-group col-md-4 mb-3'),
                Column('account_type', css_class='form-group col-md-4 mb-3'),
                Column('swift_code', css_class='form-group col-md-4 mb-3'),
                css_class='row'
            ),
            Row(
                Column('sort_code', css_class='form-group col-md-4 mb-3'),
                Column('iban', css_class='form-group col-md-4 mb-3'),
                Column('bank_country', css_class='form-group col-md-4 mb-3'),
                css_class='row'            

            ),
            Row(
                Column('notes', css_class='form-group col-md-8 mb-3'),
                css_class='row'            
            ),
            
        )   

"**************************************FAQ-FORM************************************"  

class FaqForm(forms.ModelForm):

    class Meta:
        model = Faq
        fields=('faq_question','faq_answer',)


        widgets={
              'faq_question': forms.TextInput(attrs={ 'placeholder': 'Frequently asked question ?'}),
              'faq_answer' : forms.Textarea(attrs={'placeholder': 'Write Your Awsome Solution !!'}),
              
              
          }

        labels={
         'faq_question' :'Frequently asked question (FAQ)',
         'faq_answer' : 'FAQ Answer',

         }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('faq_question', css_class='form-group col-md-6 mb-3'),
                Column('faq_answer', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            
        )

"**************************************EDIT-REASON-FORM************************************"  

class EditFaqForm(forms.ModelForm):

    class Meta:
        model = Faq
        fields=('faq_question','faq_answer',)


        widgets={
              'faq_question': forms.TextInput(attrs={ 'placeholder': 'Frequently asked question ?'}),
              'faq_answer' : forms.Textarea(attrs={'placeholder': 'Write Your Awsome Solution !!'}),
              
              
          }

        labels={
         'faq_question' :'Frequently asked question (FAQ)',
         'faq_answer' : 'FAQ Answer',

         }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.use_custom_control = False
        self.helper.layout = Layout(
            Row(
                Column('faq_question', css_class='form-group col-md-6 mb-3'),
                Column('faq_answer', css_class='form-group col-md-6 mb-3'),
                css_class='form-row'
            ),
            
        )
