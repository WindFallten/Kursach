from unicodedata import name
from xml.etree.ElementInclude import include
from django.urls import path,include, re_path
from . import views
from main.views import register

urlpatterns = [
    path('', views.index , name = "home"),
    path('i18n/', include('django.conf.urls.i18n')),
    path('vacanse/', views.vacanse , name = "vacanse"),
    path('category/<slug:url>/', views.vacanse__category , name = "vacanse__category"),
    path('vacanse/<int:pk>' , views.VacanseDetailView.as_view() , name = 'vacase-detail'),
    path('vacanse/rabotadatel' , views.rabotadatel , name = 'rabotadatel'),
    path('vacanse/addform' , views.addform , name = 'addform'),
    path('vacanse/<int:pk>/update' , views.VacanseUpdateView.as_view() , name = 'vacanse-update'),
    path('vacanse/<int:pk>/delete' , views.VacanseDeleteView.as_view() , name = 'vacanse-delete'),
    path('users/' , include('django.contrib.auth.urls')),
    path('register/' , register.as_view() , name = 'register'),
    path('vacanse/rabotadatel/vacanseRabotadatel' , views.vacanseRabotadatel , name = 'vacanseRabotadatel'),
]

# urlpatterns += i18n_patterns(
#     path('vacanse/', views.vacanse , name = "vacanse"),
#     path('vacanse/<int:pk>' , views.VacanseDetailView.as_view() , name = 'vacase-detail'),
#     path('vacanse/rabotadatel' , views.rabotadatel , name = 'rabotadatel'),
#     path('vacanse/addform' , views.addform , name = 'addform'),
#     path('vacanse/<int:pk>/update' , views.VacanseUpdateView.as_view() , name = 'vacanse-update'),
#     path('vacanse/<int:pk>/delete' , views.VacanseDeleteView.as_view() , name = 'vacanse-delete'),
#     path('users/' , include('django.contrib.auth.urls')),
#     path('register/' , register.as_view() , name = 'register'),
#     path('vacanse/rabotadatel/vacanseRabotadatel' , views.vacanseRabotadatel , name = 'vacanseRabotadatel')
# )