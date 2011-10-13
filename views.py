from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
import os.path

TEMPLATE_DIRS = (
   os.path.join(os.path.dirname(__file__),'templates').replace('\\','/'),

)

def hello(request):
	
	return HttpResponse('Hello world')


def autoComplete(request):
	'''
	fp = open('E:/django/workspace/hint/templates/autoComplete.html')
	t = Template(fp.read())
	'''
	t=get_template('autoComplete.html')
	fp.close()
	html = t.render(Context({'data': "mydata"}))
	
	return HttpResponse(html)