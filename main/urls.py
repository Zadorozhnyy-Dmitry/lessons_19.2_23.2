from django.urls import path

from main.views import contact, StudentListViews, StudentDetailVIew
from main.apps import MainConfig

app_name = MainConfig.name

urlpatterns = [
    path('', StudentListViews.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>', StudentDetailVIew.as_view(), name="view_student")
]
