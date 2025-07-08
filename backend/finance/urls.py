from django.urls import path
from . import views

urlpatterns = [
    path('new-instalment/', views.NewInstalmentRate.as_view(), name='new-instalment'),
    path('current-instalment/', views.CurrentInstalment.as_view(), name='current-instalment'),
    path('instalment-history/', views.InstalmentHistory.as_view(), name='instalment-history'),
]

