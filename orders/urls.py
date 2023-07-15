from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'orders', views.OrderViewSet,basename="orders")

# orders_list = views.OrderViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# order_detail = views.OrderViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'delete': 'destroy'
# })

urlpatterns = [
    # path('orders/',views.OrderView.as_view(),name='orders'),
    # path('order/<int:pk>/',views.OrderIdView.as_view(),name='order'),
    # path('orders/',orders_list,name='orders'),
    # path('order/<int:pk>/',order_detail,name='order'),
    path('', include(router.urls)),
    path('order/update-status/<int:pk>/',views.UpdateOrderStatusView.as_view(),name='update_order_status'),
    path('user/<int:user_id>/orders/',views.UserOrdersView.as_view(),name='users_orders'),
    path('user/<int:user_id>/order/<int:order_id>/',views.UserOrderDetailView.as_view(),name='user_order_detail'),
]