from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='batching/index.html')),
    path('addTask', TemplateView.as_view(template_name='batching/addTask.html')),
    path('select', TemplateView.as_view(template_name='batching/select.html')),
    path('weight', TemplateView.as_view(template_name='batching/weight.html')),
    path('shelling', TemplateView.as_view(template_name='batching/shelling.html')),   # 称重
    path('recheck', TemplateView.as_view(template_name='batching/recheck.html')),  # 条码复核
    path('reckon', TemplateView.as_view(template_name='batching/reckon.html')),   # 点袋
    path('barcode', TemplateView.as_view(template_name='batching/barcode.html')),   # 条码点袋
    path('subitem', TemplateView.as_view(template_name='batching/subitem.html')),   # 子配方
    path('qaweight', TemplateView.as_view(template_name='batching/qaWeight.html')),   # 子配方去皮称重
    path('finish', TemplateView.as_view(template_name='batching/finish.html')),
]
