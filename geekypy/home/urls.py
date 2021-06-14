from django.contrib import admin
from django.urls import path, include
from . import views
from .views import HomeView , CreateEntryView
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url
from django.conf import settings


urlpatterns = [
    # path('cs2/' , PaperView.as_view() , name = 'home-Paper'),
    path('', views.home, name='home'),
    path('ccodes', views.ccodes, name='ccodes'),
    path('c1codes', views.c1codes, name='c1codes'),
    path('pythoncodes', views.pythoncodes, name='pythoncodes'),
    path('javacodes', views.javacodes, name='javacodes'),
    path('dsacodes', views.dsacodes, name='dsacodes'),
    path('cproject', views.cproject, name='cproject'),
    path('guiproject', views.guiproject, name='guiproject'),
    path('webdevlopmentproject', views.webdevlopmentproject, name='webdevlopmentproject'),
    path('ebooks', views.ebooks, name='ebooks'),
    path('contact', views.contact, name='contact'),
    path('firstyear', views.firstyear, name='firstyear'),
    path('secondyear', views.secondyear, name='secondyear'),
    path('thirdyear', views.thirdyear, name='thirdyear'),
    path('fourthyear', views.fourthyear, name='fourthyear'),
    path('create_entry/' , CreateEntryView.as_view(success_url='/') , name ='create_entry' ),
    path('pythonproject/' , HomeView.as_view() , name = 'blog-home'),
    path('ethicalhacking', views.ethicalhacking, name='ethicalhacking'),
    path('it2', views.it2, name='it2'),
    path('it3', views.it3, name='it3'),
    path('it4', views.it4, name='it4'),
    path('cs2', views.cs2, name='cs2'),
    path('cs3', views.cs3, name='cs3'),
    path('cs4', views.cs4, name='cs4'),
    path('che2', views.che2, name='che2'),
    path('che3', views.che3, name='che3'),
    path('che4', views.che4, name='che4'),
    path('cve2', views.cve2, name='cve2'),
    path('cve3', views.cve3, name='cve3'),
    path('cve4', views.cve4, name='cve4'),
    path('ece2', views.ece2, name='ece2'),
    path('ece3', views.ece3, name='ece3'),
    path('ece4', views.ece4, name='ece4'),
    path('ee2', views.ee2, name='ee2'),
    path('ee3', views.ee3, name='ee3'),
    path('ee4', views.ee4, name='ee4'),
    path('me2', views.me2, name='me2'),
    path('me3', views.me3, name='me3'),
    path('me4', views.me4, name='me4'),

    # path('free', views.free, name='free'),
    path('search/' , views.search , name='search'),
    path('ebookssearch/' , views.ebookssearch , name='ebookssearch'),
    

    
 ] +static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)



 
