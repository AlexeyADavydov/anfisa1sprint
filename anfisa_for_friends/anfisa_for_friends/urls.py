from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('homepage.urls', namespace='homepage')),
    path('description/', include('about.urls', namespace='description')),
    path('ice_cream/', include('ice_cream.urls', namespace='ice_cream')),
    path('admin/', admin.site.urls),
]
