from .views import ListCreateAboutUs, AboutRetrieveAPIView, AboutUsDelete 
from django.urls import path

urlpatterns = [
    path('',ListCreateAboutUs.as_view()),
    path('get/<int:pk>', AboutRetrieveAPIView.as_view()),
    path('delete/<int:pk>', AboutUsDelete.as_view()),

]
