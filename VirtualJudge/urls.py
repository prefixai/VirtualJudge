"""PyJudge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path, include

from VirtualJudge import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', include('html_doc.urls')),
    path('login_required', views.login_required_url, name='login_required'),
    path('api/', include('problem.urls')),
    path('api/', include('account.urls')),
    path('api/', include('submission.urls')),
    path('api/', include('config.urls')),
]
