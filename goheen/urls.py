
from django import views
from django.urls import path,include

from goheen.forms import  UserPasswordResetForm
from . import views

from django.contrib.auth import views as auth_view

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('',views.homePage,name='homepage'),
    path('details/<str:pk>',views.blog_details,name = 'blog_details'),
    path('login/',views.loginview,name = 'login'),
    path('logout/',views.logoutview,name='logout'),
    path('signup/',views.singupview,name='signup'),
    path('profile/<str:pk>',views.profile,name = 'profile'),
    path('packages/',views.packageList,name = 'packages'),
    path('packagedetails/<str:pk>',views.packageDetails,name ='packagedetails' ),
    path('create blog/',views.createBlog,name = 'createblog'),
    path('update blog/<str:pk>/',views.updateBlog,name = 'updateblog'),
     path('delete/<str:pk>/',views.delete,name = 'delete'),
     path('createpackage/',views.createpackage,name = 'createpackage'),
    path('contact/',views.contact,name = 'contact'),
    path('about/',views.about,name='about'),
    path('pdf/<str:pk>',views.GenerateInvoice,name = 'pdfgenerate'),
    path('payment/<str:pk>/',views.payment,name = 'payment'),
    path('confirmpayment/<str:pk>/',views.confirm_payment,name = 'confirm_payment'),


    path('resetpassword/',auth_view.PasswordResetView.as_view(template_name='password_reset.html',
    form_class=UserPasswordResetForm),name = 'reset_password'),

    path('resetpasswordsent/',auth_view.PasswordResetDoneView.as_view(template_name = 'password_reset_done.html'),name = 'password_reset_done'),

   path('reset/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name = 'newpassword.html'),name = 'password_reset_confirm'),

   path('resetpasswordcomplete/',auth_view.PasswordResetCompleteView.as_view(template_name = 'pasword_reset_complete.html'),name = 'password_reset_complete'),




] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
