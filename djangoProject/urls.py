"""djangoProject URL Configuration

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
from django.urls import path, include

from cars.router import router as car_router
from rate.router import router as rate_router
from data_services.router import router as data_services_router

"""
POST /cars
DELETE /cars/{id}
GET /cars
POST /rate/
* Add a rate for a car from 1 to 5
{
car_id; : 1,
rating; : 5,
}
GET /popular
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(car_router.urls)),
    path('api/v1/', include(rate_router.urls)),
    path('api/v1/', include(data_services_router.urls))

]
