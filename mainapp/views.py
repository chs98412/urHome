from django.shortcuts import render,redirect
from .models import bad,money
# Create your views here.
def test(request):
    if(request.method == 'POST'):

        form = bad()
        form.who=request.POST["who"]
        form.when=request.POST["when"]
        form.what=request.POST["what"]
        form.why=request.POST["why"]
        form.save()
        print(form)
        total=money.objects.get(name="name")
        total.total= total.total+500
        total.save()

        return redirect('/main/test/')
    else:
        badwords=bad.objects.all()
        try:
            total=money.objects.get(name="name")
        except:
            m=money()
            m.total=0
            m.name="name"
            m.save()
        total=money.objects.get(name="name")
        context={"bad":badwords,"total":total}
        return render(request,'index.html',context=context)
def delete(request):
    q=money.objects.all()
    q.delete()
    a=bad.objects.all()
    a.delete()
    return redirect('/main/test/')