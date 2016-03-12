from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.views.decorators.csrf import csrf_exempt
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^myapp/',include('myproject.myapp.urls')),
    url(r'^$', RedirectView.as_view(url='/myapp/list/', permanent=True)),
    url(r'^progressbarupload/', include('progressbarupload.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
