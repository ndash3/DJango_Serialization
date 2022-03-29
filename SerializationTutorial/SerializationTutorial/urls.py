from django.contrib import admin
from django.urls import path, re_path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('FirstApi.urls'))
]
