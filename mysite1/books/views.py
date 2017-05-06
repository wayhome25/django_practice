from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Book, Author, Publisher


#--- TemplateView
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super(BooksModelView, self).get_context_data(**kwargs)
        context['object_list'] = ['Book', 'Author', 'Publisher']
        return context


#--- ListView
#--- 객체들이 들어있는 리스트를 컨텍스트 변수에 담아서 템플릿에 넘긴다.
#--- 리스트가 테이블의 모든 레코드인 경우 모델 클래스만 지정 필요
class BookList(ListView):
    model = Book
    # 컨텍스트 변수 : object_list  (모델의 모든 레코드)
    # 템플릿 파일 : 모델명 소문자_list.html (book_list.html)

class AuthorList(ListView):
    model = Author


class PublisherList(ListView):
    model = Publisher


#--- DetailView
#--- 특정한 객체 하나를 컨텍스트 변수에 담아서 템플릿에 넘긴다.
#--- 조회시 사용할 Primary Key 값은 URLconf에서 추출하여 뷰로 넘어온 파라미터를 사용한다.
class BookDetail(DetailView):
    model = Book
    # 컨텍스 변수 : object (모델의 특정 레코드, 조회용 pk는 urlConf에서 추출)
    # 템플릿 파일 : 모델명 소문자_detail.html (book_detail.html)


class AuthorDetail(DetailView):
    model = Author


class PublisherDetail(DetailView):
    model = Publisher
