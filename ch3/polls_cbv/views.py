from django.views.generic import ListView
from .models import Question, Choice


#--- ListView
#--- 객체들이 들어있는 리스트를 컨텍스트 변수에 담아서 템플릿에 넘긴다.
#--- 리스트가 테이블의 모든 레코드인 경우 모델 클래스만 지정 필요
class IndexView(ListView):
    model = Question
    # 컨텍스트 변수 : object_list  (모델의 모든 레코드)
    # 템플릿 파일 : 모델명 소문자_list.html (question_list.html)
