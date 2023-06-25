from django.contrib import admin
from django.urls import path
from auapp.views import uhome,usignup,uwelcome,ulogout,ucp
from fbapp.views import fb
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",uhome,name="uhome"),
    path("usignup",usignup,name="usignup"),
    path("uwelcome",uwelcome,name="uwelcome"),
    path("ulogout",ulogout,name="ulogout"),
    path("ucp",ucp,name="ucp"),
    path("fb",fb,name="fb"),
]

handler404="fbapp.views.pnf"