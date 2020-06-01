from django.contrib import admin
from django.urls import path
from .  import views

urlpatterns = [
    path('',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('aboutus',views.aboutus,name='aboutus'),
    path('plans',views.plans,name='plans'),
    path('checkout',views.checkout,name='checkout'),
    path('picnic',views.picnic,name='picnic'),
    path('ballondeco',views.ballondeco,name='ballondeco'),
    path('surprising',views.surprising,name='surprising'),
    path('birthdaycard',views.birthdaycard,name='birthdaycard'),
    path('miniroadtrip',views.miniroadtrip,name='miniroadtrip'),
    path('visitingamu',views.visitingamu,name='visitingamu'),
    path('showincity',views.showincity,name='showincity'),
    path('aroyaldinner',views.aroyaldinner,name='aroyaldinner'),
    path('dinnerondunes',views.dinnerondunes,name='dinnerondunes'),
    path('privatemovie',views.privatemovie,name='privatemovie'),
    path('dineronterace',views.dineronterace,name='dineronterace'),
    path('bigcute',views.bigcute,name='bigcute'),
    path('bouqet',views.bouqet,name='bouqet'),
    path('surprisebox',views.surprisebox,name='surprisebox'),
    path('heartcollege',views.heartcollege,name='heartcollege'),
    path('photoshoot',views.photoshoot,name='photoshoot'),
    path('artframe',views.artframe,name='artframe'),
    path('clipapic',views.clipapic,name='clipapic'),
    path('bir',views.bir,name='bir'),
    path('comicart',views.comicart,name='comicart'),
    path('ecomic',views.ecomic,name='ecomic'),
    path('memories',views.memories,name='memories'),
    path('customize', views.customize, name='customize'), 
    
   
    
 
]