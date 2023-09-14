from django.urls import path,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('loginform/',views.loginform,name="loginform"),
    path('login/',views.login,name="login"),
    path('registerform/',views.registerform,name="registerform"),
    path('register/',views.register,name="register"),
    path('logout/',views.logout,name="logout"),    
    path('trainform/',views.trainform,name="trainform"),    
    path('addtrain/',views.addtrain,name="addtrains"),   
    path('<train_id>',views.train_id,name="train_id"),
    path('book/',views.book,name="book"),   
    path('bookform/',views.bookform,name="bookform"),
    path('mybooking/',views.mybooking,name="mybooking"),
    path('booking/<train_id>',views.booking,name="booking"),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('daily_schedule/', views.daily_schedule, name='daily_schedule'),
    path('weekly_schedule/', views.weekly_schedule, name='weekly_schedule'),
]

 