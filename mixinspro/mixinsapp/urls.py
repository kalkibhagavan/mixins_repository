from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^product/',views.productlist.as_view()),
    url(r'^product/(?P<pk>[0-9]+)/$',views.productdetails.as_view())
]