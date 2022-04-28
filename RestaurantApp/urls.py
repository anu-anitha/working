from django.urls import path
from . import views

app_name = 'RestaurantApp'

urlpatterns = [
    path('list', views.RestListView, name = 'rest-list'),
    path('tables', views.TableListView, name = 'table-list'),
    path('select-table/<str:id>', views.SelectTableView, name = 'select-table'),
    # path('select-foodtype/',views.SelectFoodTypeView,name='food-type'),
    path('confirm/', views.ConfirmDetailsVIew, name = 'confirm-delivery'),
    path('delivery-details', views.DeliveryDetailView, name = 'delivery-details'),
    path('end-today', views.EndTodayView, name = 'end-today'),
    path('gif',views.gif,name='gif-gif'),
    path('gif1',views.gif1,name='gif-gif1'),
]
