from django.urls import path
from customeraccess import views

app_name='customeraccess'

urlpatterns = [
    path('faq-list/', views.faq_list,name='faq_list'),
    path('add-receiver/', views.add_receiver,name='add_receiver'),
    path('my-receiver/', views.my_receiver,name='my_receiver'),  
    path('edit-my-receiver/<int:id>/', views.edit_receiver,name='edit_receiver'),
    path('view-my-receiver/<int:id>/',views.view_receiver,name='view_receiver'),
    path('delete-my-receiver/<int:id>/', views.delete_receiver,name='delete_receiver'),
    path('make-new-transaction/', views.make_transaction,name='make_transaction'),
    path('my-transaction-history/', views.my_transaction,name='my_transaction'),
    path('view-my-transaction<int:id>/', views.view_transaction,name='view_transaction'),
    path('track-my-transfer/', views.track_transfer,name='track_transfer'),
    path('track-my-transfer-details/', views.track_details,name='track_details'), 
    path('find-my-nearest-agent/', views.find_agent,name='find_agent'),
    path('find-my-nearest-agent-location/', views.agent_location,name='agent_location'),
    path('logout/', views.logoutCustomer, name="logout"),
    path('under-progress/', views.construction, name="construction"),
    
    


]