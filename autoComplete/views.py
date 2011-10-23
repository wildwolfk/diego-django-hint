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
    if request.GET.has_key('term'):
        html.append(request.GET['term'])
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
    
    if request.GET.has_key('term'):
        from django.utils import simplejson
        try:
            prefix=request.GET['term']
            temp=[]
            # only display top 10 result
            for i in words.objects.filter(word__icontains=prefix)[:10]:
                temp.append(i.word)
            json_data=simplejson.dumps(temp)

            return HttpResponse(json_data,mimetype='application/json')
        except :
            return HttpResponse(simplejson.dumps([]),mimetype='application/json')
    
    
    end=words.objects.all()
    for tag in end:
        end1=tag.word
    
    end="<b>test"
    
    # html = t.render(Context({"gogogo": end1}))
    # return HttpResponse(html)
    return render_to_response("autoComplete/test.html", {"gogogo": end})
    
def testAdmin(request):
    from autoComplete.models import words
    if request.method == 'GET' :
        if request.GET.has_key('action') :
            if (request.GET["action"] == "refresh")  :
                end=words.objects.all()
                table=""
                for tag in end:
                    table += "<tr><td><checkbox id="+str(tag[0])+"></td><td>"+str(tag[0])+"</td></tr>"
                    
                return HttpResponse(table)
            
#    if (request.POST.get("action",'') == "add")  :
    elif request.method == 'POST':
        if request.POST.get('action', '') :
            if (request.POST['action'] == "add")  :
                response=HttpResponse()  
                response['Content-Type']="text/javascript"  
                
#                p=words(word=request.POST.get("word",'')  )
                p=words(word=request.POST["word"])
                p.save()
           
                response.write(1)
                return response
       
        if (request.POST.get("action",'') == "del")  :
            response=HttpResponse()  
            response['Content-Type']="text/javascript"  
            queryTag = request.POST.get("title",'')  
        
            words.objects.filter(word=request.POST['word']).delete()
        
            response.write(1)
            return response        
        return 
    
    table=""
    end=words.objects.all()
    for tag in end:
        table += "<tr><td><checkbox id="+str(tag.word)+"></td><td>"+str(tag.word)+"</td></tr>"
    # html = t.render(Context({"gogogo": end1}))
    # return HttpResponse(html)
    return render_to_response("autoComplete/testAdmin.html", {"gogogo": table})