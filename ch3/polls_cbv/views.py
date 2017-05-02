from django.views.generic import ListView, DetailView
from .models import Question, Choice


#--- ListView
#--- 객체들이 들어있는 리스트를 컨텍스트 변수에 담아서 템플릿에 넘긴다.
#--- 리스트가 테이블의 모든 레코드인 경우 모델 클래스만 지정 필요
class IndexView(ListView):
    template_name = 'polls_cbv/index.html'
    model = Question
    # 컨텍스트 변수 : object_list  (모델의 모든 레코드)
    # 템플릿 파일 : 모델명 소문자_list.html (question_list.html)


#--- DetailView
#--- 특정한 객체 하나를 컨텍스트 변수에 담아서 템플릿에 넘긴다.
#--- 조회시 사용할 Primary Key 값은 URLconf에서 추출하여 뷰로 넘어온 파라미터를 사용한다.
class DetailView(DetailView):
    template_name = 'polls_cbv/detail.html'
    model = Question
    context_object_name = 'question' # 컨텍스트 디폴트 변수명 object => question 으로 변경
    # 컨텍스트 변수 : object (모델의 특정 레코드, 조회용 pk는 urlConf에서 추출)
    # 템플릿 파일 : 모델명 소문자_detail.html (question_detail.html)
