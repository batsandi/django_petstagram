from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('asdf/', include('petstagram.main.urls'))
]
