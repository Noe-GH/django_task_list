from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="list"),
    # name se utiliza para la creación de links en HTML. Lo facilita.
    path('update_task/<str:pk>', views.update_task, name="update_task"),
    path('delete/<str:pk>', views.delete_task, name="delete_task"),
]
