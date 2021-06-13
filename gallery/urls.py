from django.urls import path

from . import views


#TODO: 4th argument: arg="test_kwarg_in_path"
urlpatterns = [
    path("",views.index,name="index"),
    ]
#"name" kwarg is to be used in other parts of Django, e.g. in templates
