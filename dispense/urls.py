from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='dispense/index.html')),
    path('allot', TemplateView.as_view(template_name='dispense/allot.html')),
    path('weight', TemplateView.as_view(template_name='dispense/weight.html')),
    path('back', TemplateView.as_view(template_name='dispense/back.html')),
]
