from django.urls import path
from mainApp.views import *

urlpatterns = [
    path('', FormPageView.as_view(), name='form'),
    path('dummy/', DummyPageView.as_view(), name='dummy')
]