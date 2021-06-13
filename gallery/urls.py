from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views


#TODO: 4th argument: arg="test_kwarg_in_path"
urlpatterns = [
    path("",views.index,name="index"),
    path('upload_image', image_view, name = 'upload_image'),
    path('success', success, name = 'success'),
    ]
#"name" kwarg is to be used in other parts of Django, e.g. in templates
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
