from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.ProductCreateView.as_view(), name='product_list_create'),
    url(r'^(?P<pk>\d+)/$', views.ProductRetrieveUpdateAPIView.as_view(), name='product_retrieve_update'),
    url(r'^category/$', views.CateGoryCreateView.as_view(), name="category_list_create"),
    url(r'^shopping-cart/$', views.ShoppingCartListCreateView.as_view(), name='shopping_cart_list_create'),
    url(r'^shopping-cart/(?P<pk>.+)/$', views.ShoppingCartRetrieveUpdateAPIView.as_view(), 
        name='shopping_cart_retrieve_update')
]