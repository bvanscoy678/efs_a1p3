from django.contrib import admin
from django.conf.urls import include,url
from django.urls import path
from django.contrib.auth import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('portfolio.urls')),
    url(r'^accounts/login/$', views.login, name='login'),
    url(r'^accounts/logout/$', views.logout, name='logout', kwargs={'next_page': '/'}),
    #change password urls
    path('password_change/',
         views.PasswordChangeView.as_view(),
         name='password_change'),
    path('password_change/done/',
         views.PasswordChangeDoneView.as_view(),
         name='password_change_done'),
    #reset password views
    path('password_reset_form/',
         views.PasswordResetView.as_view(),
         name='password_reset_form'),
    url(r'^password_reset/done/$', views.password_reset_done, name='password_reset_done'),
    path('reset/<uidb64>/token/',
         views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('reset/done/',
         views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

]
