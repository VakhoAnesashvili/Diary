from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views
from rest_framework.schemas import get_schema_view 
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swawgger_get_schema_view


schema_view = swawgger_get_schema_view(openapi.Info(title='Diary API schema',default_version='v1', description='API for Diary'),public=True)


urlpatterns = [
    path('swagger/', schema_view.with_ui('swagger'), name='swagger'),
    path('admin/', admin.site.urls),
    path('api/user/', include('user.urls')),
    path('api/diary/', include('diary_notes.urls')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]