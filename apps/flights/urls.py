from django.urls import path

from . import views


app_name = "flights"

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:flight_id>', views.flight, name="flight"),
    path('<int:flight_id>/book', views.book, name='book'),
    path('<int:flight_id>/edit', views.edit, name='edit'),
    path('<int:flight_id>/delete', views.delete, name='delete'),
    path('<int:flight_id>/<int:passenger_id>/delete', views.dpassenger, name='dpassenger'),
    path('add', views.add, name='add'),
    path('passengers/add', views.add_passenger, name='add_passenger'),
    path('passengers', views.passengers, name='passengers'),
    path('passengers/<int:passenger_id>/edit', views.edit_passenger, name='edit_passenger'),
    path('passengers/<int:passenger_id>', views.passenger, name='passenger')

]

