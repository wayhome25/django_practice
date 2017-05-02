# polls_cbv.urls
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'), # /polls_cbv/
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name='detail'), # /polls_cbv/5/ - DetailView 에서 특정 레코드 조회시 URLconf의 pk 변수를 사용
    url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'), # /polls_cbv/5/vote/
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'), # /polls_cbv/5/results/
]
