from django.urls import path, include
from .views import *

urlpatterns = [
    path('registration', RegistrationView().as_view()),
    path('user-update/<int:pk>', UserDetail().as_view()),
]
urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
