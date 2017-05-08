from django.views.generic.base import TemplateView

class HomeView(TemplateView):
	template_name = 'home.html' #템플릿 파일이 위치하는 디렉터리는 settings.py 파일의 TEMPLATE_DIRS 항목으로 지정
