"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.http import HttpResponse, HttpResponseForbidden
from django.views.generic.base import RedirectView


def is_authenticated(request):
    if request.user.is_authenticated:
        return HttpResponse('OK')
    else:
        return HttpResponseForbidden()


urlpatterns = [
    url(r'^$', RedirectView.as_view(url='login'), name='redirect-to-login'),
    url(r'^is_authenticated?$', is_authenticated),
    url(r'', include('mama_cas.urls')),
    url(r'^admin/', include('loginas.urls')),
    url(r'^admin/', admin.site.urls),
]
