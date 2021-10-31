"""moneytransfer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from administration import views as administration_views
from django.conf.urls import handler404, handler500
from django.contrib.auth.views import (PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView,
                                       PasswordResetCompleteView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('administration.urls', namespace='administration')),
    path('transfer/',include('transfer.urls', namespace='transfer')),
    path('exchange/',include('exchange.urls', namespace='exchange')),
    path('customer/',include('customeraccess.urls', namespace='customeraccess')),
    path('reset_password/', PasswordResetView.as_view(template_name="auth/password-reset.html"),
         name="password_reset"),
    path('reset_password/done/', PasswordResetDoneView.as_view(template_name="auth/password-reset-done.html"),
         name="password_reset_done"),
    path('reset_password/confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name="auth/password-reset-confirm.html"),
         name="password_reset_confirm"),
    path('reset_password/complete/',
         PasswordResetCompleteView.as_view(template_name="auth/password-reset-complete.html"),
         name="password_reset_complete"),


    
    
]  



handler404 = administration_views.error_404
handler500 = administration_views.error_500
