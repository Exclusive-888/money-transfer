from django.urls import path
from exchange import views

app_name='exchange'

urlpatterns = [
    path('money-exchange/',views.exchange_list,name='money_exchange'),
    path('new-money-exchange/', views.new_exchange,name='new_money_exchange'),
    path('view-money-exchange/<int:id>', views.view_exchange,name='view_exchange'),
    path('edit-exchange/<int:id>/', views.edit_exchange,name='edit_exchange'), # get and post req. for update operation
    path('delete-exchange/delete/<int:id>/',views.delete_exchange,name='delete_exchange'),

]