from django.shortcuts import render
from django.views.generic import DetailView, ListView
from bookmark.models import Bookmark

class BookmarkLV(ListView):
	"""
	ListView 디폴트 지정 속성
	1) 컨텍스트 변수 : object_list
	2) 템플릿 파일 : bookmark_list.html (모델명소문자_list.html)
	"""
	model = Bookmark


class BookmarkDV(DetailView):
	"""
	DetailView 디폴트 지정 속성
	1) 컨텍스트 변수 : object (URLConf 에서 pk 파라미터 값을 활용하여 DB 레코드 조회)
	2) 템플릿 파일 : bookmark_detail.html (모델명소문자_detail.html)
	"""
	model = Bookmark
