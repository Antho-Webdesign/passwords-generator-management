from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.urls import path, include

from users.views import profile

urlpatterns = [
        path('admin/', admin.site.urls),
        path('', include('generator.urls')),
        path('', include('users.urls')),
        path('profile/', profile, name='profile'),
        # path('portfolio/', include('portfolio.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
