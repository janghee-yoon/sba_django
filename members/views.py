from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members

# Create your views here.

def index(request):
    print(dir(req))
    return HttpResponse("<h1>hello</h1>")

def test(req):
    return HttpResponse("<h2>test</h2>")

def signup(req):
    if req.method == 'POST':
        username = req.POST['username']
        email = req.POST['email']

        #username == exit
        # h2 로 나가기를 출력
        #if username == 'exit' :
        #    return HttpResponse("나가기")
        #codi를 입력하면 b.html로
        #elif username == 'codi' :
        #    return render(req, 'b.html')
        member = Members(
                username = username,
                useremail = email
                )
        
        member.save()

        res_data = {}
        res_data['res'] = '등록성공'
        return render(req, 'a.html', res_data)
    
    
    return render(req, "a.html") 
