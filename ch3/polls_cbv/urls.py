# polls_cbv.urls
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'), # /polls_cbv/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'), # /polls_cbv/5/
    url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'), # /polls_cbv/5/vote/
]
