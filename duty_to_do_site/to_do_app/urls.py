from django.urls import path
from django.conf.urls import include

from . import views

app_name = 'to_do_app'
urlpatterns = [
    path('accounts/register', views.register, name='register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', views.to_do, name='to_do'),
    path('<int:to_do_point_id>/', views.edit, name='edit'),
    path('<int:to_do_point_id>/edit', views.edit_save, name='edit_save'),
    path('<int:to_do_point_id>/delete', views.delete, name='delete'),
    path('add', views.add, name='add'),
    path('error/', views.error, name='error'),
]
