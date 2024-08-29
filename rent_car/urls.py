
from .views import *


from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import path, re_path
from django.urls import path, re_path, include
#from firstapp import routing
# handler404 = custom_404




urlpatterns = [
                  # new car rent
                  path('', home_redirect, name='home'),
                  path('car-rents/', car_rent_list, name='car_rent_list'),
                  path('car-rents/new/', car_rent_create, name='car_rent_create'),
                  path('car-rents/<int:id>/', car_rent_detail, name='car_rent_detail'),
                  path('car-rents/<int:id>/edit/', car_rent_update, name='car_rent_update'),
                  path('car-rents/<int:id>/delete/', car_rent_delete, name='car_rent_delete'),

                  path('business-home',home,name="business-home"),
                  path('about',about,name="business-about"),
                  path("clients",clients ,name="business-clients"),
                  path("pricing",pricing,name="business-pricing"),
                  path("blog",blog,name="business-blog"),
                  path("contact",contact,name="business-contact"),
                  #path('services',service,name="services-list"),
                  #path('single' ,single,name="single" ),
                  path('register/',register_view,name="business-register"),
                  path('buslogin',login_view , name="business-login"),
                  path('all-password/', update_register, name='update_register'),
                  path('change-password/', change_password, name='change_password'),
                  #path('profile', simple_view, name='profile'),
                  path('profile/update/', update_profile, name='profile_update'),
                  path('profile/', get_profile, name='profile_view'),
                  path('profile/delete/', delete_profile, name='profile_delete'),
                  path('logout/', LogoutView.as_view(next_page='business-register'), name='logout'),
                  re_path(r'^.*/$', TemplateView.as_view(template_name='404.html'), name='catchall-404'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
settings.DEBUG = True
