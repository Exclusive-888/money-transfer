
from django.urls import path
from transfer import views

app_name='transfer'

urlpatterns = [
    path('money-transfer/',views.transfer_list,name='money_transfer'),
    path('new-money-transfer/', views.new_transfer,name='new_money_transfer'),
    path('view-money-transfer/<int:id>', views.view_transfer,name='view_transfer'),
    path('edit-transfer/<int:id>/', views.edit_transfer,name='edit_transfer'), # get and post req. for update operation
    path('delete-transfer/delete/<int:id>/',views.delete_transfer,name='delete_transfer'),
    path('debt-money-transfer/',views.debt_list,name='debt_transfer'),
    path('edit-debt-transfer/<int:id>/', views.edit_debt,name='edit_debt'),
    path('view-debt-transfer/<int:id>', views.view_debt,name='view_debt'),
    path('', views.load_rate,name='load_rate'),
    path('ajax/load-cities/', views.load_cities, name='ajax_load_cities'),  # <-- this one here



]