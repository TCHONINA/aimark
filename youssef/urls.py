"""youssef URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from aimark import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
                  path('admin/', admin.site.urls),

                  # ##################### auth #####################

                  path('login', views.loginpage),
                  path('loginclick', views.loginclick),
                  path('logoutclick', views.logoutclick),


                  path('mark/add', views.add),
                  path('', views.add),

                  path('mark/edit/<int:id>', views.edit),
                  path('mark/delete/<int:id>', views.delete),

                  path('temp_exemple', views.temp_exemple, name="temp_exemple"),
                  #
                  path('mark/points/add/<int:id>', views.addpoint),
                  path('mark/points/delete/<int:id>', views.deletepoint),
                  path('mark/search', views.recherche),

                  path('mark/login', views.loginPage),



              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
