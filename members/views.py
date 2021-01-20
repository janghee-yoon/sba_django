from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Members

# Create your views here.

def index(request):
    print(dir(req))
    return HttpResponse("<h1>hello</h1>")

def git(req):
    return HttpResponse("<h2>hello22</h2>")

def test(req):
    return HttpResponse("<h2>test</h2>")

def gu(req):
    num = req.GET.get('num','')
    return HttpResponse(f"<h1> gugu : <br> {num_gugu(num)} </h1>")

def num_gugu(num):
    str = ""
    for i in range(9):
        str += f"{int(num)} * {i+1} = {int(num) * (i+1)} <br>"
    return str

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
