from django.contrib import admin
from django.urls import include, path
from apps.persons.api import api

urlpatterns = [
    # Admin route
    path('admin/', admin.site.urls),

    # Include the URLs from persons app.
    path('', include('apps.persons.urls')),

    # API routes Django Ninja
    path("api/", api.urls),
]
