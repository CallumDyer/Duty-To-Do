from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('to-do-app/', include('to_do_app.urls')),
    path('admin/', admin.site.urls),
]
