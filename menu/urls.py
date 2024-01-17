from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

app_name = "menu"

urlpatterns = [
    path('', views.index, name="index"),
    path('info/<int:pizza_id>/', views.pizza_info, name="info"),
]

