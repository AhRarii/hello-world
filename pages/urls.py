from django.urls import path
from .views import homePageView

# Homepage
urlpatterns = [
    path('', homePageView, name='home'),
]
