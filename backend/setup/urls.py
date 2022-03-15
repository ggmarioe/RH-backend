from django.urls import path
from rest_framework_simplejwt import views as jwt_views

from .views.custom_user import CustomUserCreate
from .views.hello_world_view import HelloWorldView
from .views.extra_hour_view import ExtraHourView

urlpatterns = [
    path('user/create/', CustomUserCreate.as_view(), name="create_user"),
    path('token/obtain/', jwt_views.TokenObtainPairView.as_view(), name='token_create'),  # override sjwt stock token
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('hello/', HelloWorldView.as_view(), name='hello_world'),
    path('extra-hour/',ExtraHourView.as_view(), name='extra-hour'),
    # path('extra-hour/',ExtraHourView.as_view(), name='extra-hour'),
    path('extra-hour/<int:id>/',ExtraHourView.extra_hour_detail, name='extra-hour-detail'),
    path('extra-hour/<str:username>/',ExtraHourView.extra_hour_by_username, name='extra-hour-by-username'),
]