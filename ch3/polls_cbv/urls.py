# polls_cbv.urls
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'), # /polls_cbv/
]