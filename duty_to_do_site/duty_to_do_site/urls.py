from django.urls import include, path

urlpatterns = [
    path('to_do/', include('to_do_app.urls')),
]
