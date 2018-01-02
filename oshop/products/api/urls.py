from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProductCreateView.as_view(), name='product_list_create'),
    url(r'^category/$', views.CateGoryCreateView.as_view(), name="category_list_create"),
]