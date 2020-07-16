from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name ="index"),
    path('search/', views.image_search, name = "image_search"),
    path('locations/<str:location>', views.location_images, name = "locations")
]