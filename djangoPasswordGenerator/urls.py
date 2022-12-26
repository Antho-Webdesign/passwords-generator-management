from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include


urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('generator.urls')),
        # path('', include('users.urls')),        # path('portfolio/', include('portfolio.urls')),
        path("", include("accounts.urls")),
        path("", include("django.contrib.auth.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
