from django.urls import path

from . import views

app_name = 'to_do_app'
urlpatterns = [
    path('', views.to_do, name='to_do'),
    path('<int:to_do_point_id>/', views.edit, name='edit'),
    path('<int:to_do_point_id>/edit', views.edit_save, name='edit_save'),
    path('error', views.error, name='error'),
]
