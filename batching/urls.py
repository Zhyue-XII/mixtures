from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='batching/index.html')),
    path('addTask', TemplateView.as_view(template_name='batching/addTask.html')),
    path('select', TemplateView.as_view(template_name='batching/select.html')),
]
