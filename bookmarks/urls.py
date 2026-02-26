"""
URL configuration for bookmark_manager project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from .views import BookmarkViewSet, bookmark_list, bookmark_add, bookmark_edit, bookmark_delete

router = DefaultRouter()
router.register(r'bookmarks', BookmarkViewSet)

urlpatterns = [
    path("api/", include(router.urls)),

    path("", bookmark_list, name="bookmark_list"),
    path("add/", bookmark_add, name="bookmark_add"),
    path("edit/<int:pk>/", bookmark_edit, name="bookmark_edit"),
    path("delete/<int:pk>/", bookmark_delete, name="bookmark_delete"),
]
