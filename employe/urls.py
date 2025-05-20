from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Sign_Up_View,Login_View,Profile_View,Employer_View,All_Employers_View

router = DefaultRouter()
router.register(r'employers', Employer_View, basename='employers')

urlpatterns = [
    path('auth/signup/', Sign_Up_View.as_view(), name='signup'),
    path('auth/login/', Login_View.as_view(), name='login'),
    path('auth/profile/', Profile_View.as_view(), name='profile'),
    path('', include(router.urls)),
    path('employers/list', All_Employers_View.as_view(), name='employers-list')
]
