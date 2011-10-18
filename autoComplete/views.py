from django.http import HttpResponse
from django.shortcuts import render_to_response
# Create your views here.
def hello(request):
    return HttpResponse("Hello world")

def getMeta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))
    
def autoComplete(request):
    
#    import os.path
#
#    TEMPLATE_DIRS = (
#                     os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
#                    )
#    t = render_to_response("test.html", {"gogogo": "Now from server"})

    # fp = open('C:/django/hint/templates/autoComplete/test.html')
    # from django.template import Template, Context
    # 
    # t = Template(fp.read())
    # fp.close()
    from autoComplete.models import words
    
    
    end=words.objects.filter(word='test')[:10]
    for tag in end:
        end1=tag.word
    for i in end:
        pass
    # html = t.render(Context({"gogogo": end1}))
    # return HttpResponse(html)
    return render_to_response("autoComplete/test.html", {"gogogo": end})

def detail(request):
#    from django.utils import simplejson
    from autoComplete.models import words
    if request.GET.has_key('q'):
        tags = words.objects.filter(word='test')[:10]
#        tags = words.objects.filter(word__icontains=request.GET['q'])[:10]
        return HttpResponse('\n'.join(tag.word for tag in tags))
#        return HttpResponse('\n'.join('test'))   name__icontains=request.GET['q']
    
    return HttpResponse()
    