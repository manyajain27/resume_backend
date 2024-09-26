from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PersonalDetailViewSet
from . import views

router = DefaultRouter()
router.register(r'personal_details', PersonalDetailViewSet, basename='personal_detail')

urlpatterns = [
    path('', include(router.urls)),  # Change this to the empty path
    path('api/personal_details/', views.save_personal_details, name='save_personal_details'),
]
