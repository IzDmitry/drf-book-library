from django.contrib import admin
from django.urls import include, path
from books import views as api_books
from user.views import UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'book', api_books.BookViewSet, basename='BookViewSet')
router.register(r'user', UserViewSet, basename='UserViewSet')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
