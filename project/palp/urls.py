from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='dashboard/')), 
    path('login/', include('users.urls')),
    path('logout/', include('users.urls')),
    path('signup/', include('users.urls')),
    path('dashboard/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('conversations/', include('conversations.urls')),
]