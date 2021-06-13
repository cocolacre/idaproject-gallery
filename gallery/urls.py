from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls.static import static
from . import views

#TODO: 4th argument: arg="test_kwarg_in_path"

urlpatterns = [
    #path("", views.index, name = "index"),
    path("", views.image_list, name = "image_list"),
    path('upload_image/', views.upload_image, name = 'upload_image'),
    path('success/', views.success, name = 'success'),
    path('resizing_result/', views.resizing_result, name = 'resizing_result'),
    ]

#NOTE: "name" kwarg is to be used in other parts of Django, e.g. in templates

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
