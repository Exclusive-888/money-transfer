from django.urls import path
from administration import views


app_name='administration'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('my-dashboard/', views.my_dashboard,name='my_dashboard'),
    path('logout/', views.logoutUser, name="logout"),
    path('agent/',views.agent_list,name='agent'),
    path('add-new-agent/', views.new_agent,name='add-new-agent'),
    path('view-agent/<int:id>', views.view_agent,name='view_agent'),
    path('edit-agent/<int:id>/', views.edit_agent,name='edit_agent'), # get and post req. for update operation
    path('edit-agent-admin-profile/',views.agentprofile, name='agent_profile'),
    path('edit-customer-admin-profile/',views.customerprofile, name='customer_profile'),
    path('agent-profile-change-password', views.agentchangepassword, name='agent_change_password'),
    path('customer-profile-change-password', views.customerchangepassword, name='customer_change_password'),
    path('delete-agent/delete/<int:id>/',views.delete_agent,name='delete_agent'),
    path('customer/', views.customer_list,name='customer'),
    path('add-new-customer/', views.new_customer,name='add-new-customer'),
    path('view-customer/<int:id>', views.view_customer,name='view_customer'),
    path('edit-customer/<int:id>/', views.edit_customer,name='edit_customer'), # get and post req. for update operation
    path('delete-customer/delete/<int:id>/',views.delete_customer,name='delete_customer'),
    path('currency/', views.currency_list,name='currency'),
    path('add-currency/', views.new_currency,name='add-currency'),
    path('view-currency/<int:id>', views.view_currency,name='view_currency'),
    path('edit-currency/<int:id>/', views.edit_currency,name='edit_currency'), # get and post req. for update operation
    path('delete-currency/delete/<int:id>/',views.delete_currency,name='delete_currency'),
    path('agent-bank/', views.agent_bank,name='agent_bank'),
    path('add-agent-bank/', views.add_agentbank,name='add_agent_bank'),
    path('view-agent-bank/<int:id>', views.view_agentbank,name='view_agent_bank'),
    path('edit-agent-bank/<int:id>/', views.edit_agentbank,name='edit_agent_bank'), # get and post req. for update operation
    path('delete-agent-bank/delete/<int:id>/',views.delete_agentbank,name='delete_agent_bank'),
    path('customer-bank/', views.customer_bank,name='customer_bank'),
    path('add-customer-bank/', views.add_customerbank,name='add_customer_bank'),
    path('view-customer-bank/<int:id>', views.view_customerbank,name='view_customer_bank'),
    path('edit-customer-bank/<int:id>/', views.edit_customerbank,name='edit_customer_bank'), # get and post req. for update operation
    path('delete-customer-bank/delete/<int:id>/',views.delete_customerbank,name='delete_customer_bank'),
    path('reason/',views.reason_list,name='reason'),
    path('add-reason/', views.new_reason,name='new_reason'),
    path('view-reason/<int:id>', views.view_reason,name='view_reason'),
    path('edit-reason/<int:id>/', views.edit_reason,name='edit_reason'), # get and post req. for update operation
    path('delete-reason/delete/<int:id>/',views.delete_reason,name='delete_reason'),
    path('faq/',views.faq_list,name='faq_list'),
    path('add-faq/', views.add_faq,name='add_faq'),
    path('edit-faq/<int:id>/', views.edit_faq,name='edit_faq'), # get and post req. for update operation
    path('delete-faq/delete/<int:id>/',views.delete_faq,name='delete_faq'),
    path('search/',views.GlobalSearchView,name='search'),




]

