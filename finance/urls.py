from django.contrib import admin
from django.urls import include, path
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to your Django App!")

urlpatterns = [
    path('', home_view),
    path('admin/', admin.site.urls),
    path('stocks/', include('finance.stocks.urls')),

]
