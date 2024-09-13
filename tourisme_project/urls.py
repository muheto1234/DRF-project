"""
URL configuration for tourisme_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('tourisme/', include('tourisme_app.api.urls')),
    path('account/', include('user_app.api.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    # Body (en raw et sélectionnez JSON comme format) :
    # Envoyer une requête pour demander un reset de mot de passe: api/password_reset/
    # {
    # "email": "your_email@example.com"
    # }
    # Réinitialiser le mot de passe :api/password_reset/confirm/
    # {
    # "token": "your_reset_token",
    # "password": "your_new_password"
    # }
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
