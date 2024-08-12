from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from .models import *
from django.db.models import Sum
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,"index.html")

def Register(request):
    if request.method == "POST":
        messages.success(request, "Registration Successfully Completed Please Login to continue")

        f = request.POST["fname"]
        u = request.POST["uname"]
        p = request.POST["password"]
        m = request.POST["mobile"]
        pr = request.FILES["file"]

        s = register(name=f,username=u,password=p,contact=m,photo=pr)
        s.save()
        return redirect("/")
    else:
        return redirect("/register")

def registration(request):
    if request.method == "POST":
        u = request.POST["username"]
        p = request.POST["password"]

        data = register.objects.all().filter(username=u,password=p)
        if data:
            messages.success(request,"Login Successfully Completed")

            request.session['username'] = u                           # session start
            return redirect("/dashboard")
        else:
            messages.warning(request, "Incorrect Username or Password")
            return redirect("/")


def dashboard(request):
    if request.session.get('username') is not None:
        email = request.session.get('username')
        data = register.objects.all().filter(username=email)
        return render(request,"dashboard.html",{'data':data})
    else:
        return redirect("/")



def add_tenant(request):
    if request.session.get('username') is not None:

        return render(request,"add_tenant.html")
    else:
        return redirect("/")


def add(request):
    if request.method == "POST":
        messages.success(request, "Record Added Successfully")
        u = request.POST["username"]
        r = request.POST["roomno"]
        t = request.POST["tname"]
        a = request.POST["address"]
        o = request.POST["occupation"]
        c = request.POST["contact"]
        d = request.POST["date"]


        s = tenant(username=u,roomno=r,tname=t,address=a,occupation=o,contact=c,date=d)
        s.save()



        return redirect("/view_tenant")
    else:
        return HttpResponse("Fail")

def view_tenant(request):
    if request.session.get('username') is not None:
       username =  request.session.get('username')
       data = tenant.objects.all().filter(username=username)
       return render(request,"view_tenant.html",{'data':data})
    else:
        return redirect("/")

def tenant_delete(request):
    messages.warning(request, " Record Deleted Successfully")
    id = request.GET["id"]
    tenant.objects.all().filter(id=id).delete()
    return redirect("/view_tenant")

def tenant_edit(request):
    id = request.GET["id"]
    data = tenant.objects.all().filter(id=id)
    return render(request,"modify.html",{'data':data})

def update_data(request):
    if request.method == "POST":
        messages.info(request, "Record Updated Successfully")
        i = request.POST["id"]
        r = request.POST["roomno"]
        t = request.POST["tname"]
        a = request.POST["address"]
        o = request.POST["occupation"]
        c = request.POST["contact"]
        # r = request.POST["rent"]
        d = request.POST["date"]


        tenant.objects.all().filter(id=i).update(roomno=r,tname=t,address=a,occupation=o,contact=c,date=d)

        return redirect("/view_tenant")
    else:
        return redirect("/view_tenant")


def Logout(request):
    messages.info(request, "Logout Successfully")
    del request.session['username']              # session End
    return redirect("/")


def main_add(request):
    if request.session.get('username') is not None:
       data = tenant.objects.all()
       return render(request,"main_add.html",{'data':data})
    else:
        return redirect("/")


def addition(request):
    if request.method == "POST":
        messages.success(request, "Record Added Successfully")
        u = request.POST["username"]
        r = request.POST["roomno"]
        m = request.POST["month"]
        y = request.POST["year"]
        n = request.POST["unit"]
        # a = request.POST["amount"]
        ba = 5
        ta = int(n) * ba
        s = main(username=u,roomno=r,month=m,year=y,unit=n,amount=ta)
        s.save()



        return redirect("/main_view")
    else:
        return HttpResponse("Fail")

def main_view(request):
    if request.session.get('username') is not None:
       username = request.session.get('username')
       data = main.objects.all().filter(username=username)
       return render(request,"main_view.html", {'data':data})
    else:
        return redirect("/")

def main_delete(request):
    messages.warning(request, "Record Deleted Successfully")
    id = request.GET["id"]
    main.objects.all().filter(id=id).delete()
    return redirect("/main_view")

def main_edit(request):
    id = request.GET["id"]
    data = main.objects.all().filter(id=id)
    return render(request,"modify_main.html",{'data':data})


def update_main(request):
    if request.method == "POST":
        messages.info(request, "Record Updated Successfully")
        i = request.POST["id"]
        r = request.POST["roomno"]
        m = request.POST["month"]
        y = request.POST["year"]
        n = request.POST["unit"]
        a = request.POST["amount"]

        main.objects.all().filter(id=i).update(roomno=r,month=m,year=y,unit=n,amount=a)

        return redirect("/main_view")
    else:
        return redirect("/main_view")











def profile(request):
    if request.session.get('username') is not None:
        email = request.session.get('username')
        data = register.objects.all().filter(username=email)
        return render(request,"profile.html",{'data':data})
    else:
        return redirect("/")

def profile_edit(request):
    messages.warning(request, "You can Edit only name,password and mobile number")
    id = request.GET["id"]
    data = register.objects.all().filter(id=id)
    return render(request, "profile_edit.html", {'data': data})


def update_profile(request):
    if request.method == "POST":
        messages.success(request, "Save Changes Successfully")

        i = request.POST["id"]
        f = request.POST["fname"]
        # u = request.POST["uname"]
        p = request.POST["password"]
        m = request.POST["mobile"]
        # pr = request.FILES["file"]

        register.objects.all().filter(id=i).update(name=f,password=p, contact=m)

        return redirect("/profile")
    else:
        return redirect("/profile")









def sub_add(request):
    if request.session.get('username') is not None:
       data = tenant.objects.all()
       return render(request,"sub_add.html",{'data':data})
    else:
        return redirect("/")

def additions(request):
    if request.method == "POST":
        messages.success(request, "Record Added Successfully")
        u = request.POST["username"]
        r = request.POST["roomno"]
        p = request.POST["previous"]
        e = request.POST["reading"]
        t = request.POST["tmonth"]
        y = request.POST["tyear"]



        s = sub(username=u,roomno=r,previous=p,reading=e,tmonth=t,tyear=y,)
        s.save()
        #
        # ds = dsub(roomno=r,previous=p,reading=e,tmonth=t,tyear=y,)
        # ds.save()



        return redirect("/sub_view")
    else:
        return HttpResponse("Fail")



def sub_view(request):
    if request.session.get('username') is not None:
      username = request.session.get('username')
      data = sub.objects.all().filter(username=username)
      return render(request,"sub_view.html",{'data':data})
    else:
        return redirect("/")

def sub_delete(request):
    messages.warning(request, "Record Deleted Successfully")
    id = request.GET["id"]
    sub.objects.all().filter(id=id).delete()
    return redirect("/sub_view")

def sub_edit(request):
    id = request.GET["id"]
    data = sub.objects.all().filter(id=id)
    return render(request,"modify_sub.html",{'data':data})

def update_sub(request):
    if request.method == "POST":
        messages.info(request, "Record Updated Successfully")
        i = request.POST["id"]
        r = request.POST["roomno"]
        p = request.POST["previous"]
        e = request.POST["reading"]
        t = request.POST["tmonth"]
        y = request.POST["tyear"]

        sub.objects.all().filter(id=i).update(roomno=r,previous=p,reading=e,tmonth=t,tyear=y)

        return redirect("/sub_view")
    else:
        return redirect("/sub_view")



def previous_reading(request):
    if request.method == "POST":
        roomid= request.POST["roomid"]
        data = main.objects.all().filter(roomno=roomid)
        return JsonResponse(list(data.values('unit')), safe = False)
    else:
        return HttpResponse("Fail")


def tanker_add(request):
    if request.session.get('username') is not None:
      data = tenant.objects.all()
      return render(request,"tanker_add.html",{'data':data})
    else:
        return redirect("/")

def tanker_addition(request):
    if request.method == "POST":
        messages.success(request, "Record Added Successfully")
        u = request.POST["username"]
        m = request.POST["month"]
        y = request.POST["year"]
        t = request.POST["ttanker"]
        # a = request.POST["amt"]
        s = request.POST["stenant"]
        at = 300
        ta = int(t) * at

        s = tanker(username=u,month=m,year=y,ttanker=t,amt=ta,stenant=s)
        s.save()
        return redirect("/tanker_view")
    else:
        return HttpResponse("Fail")


def tanker_view(request):
    if request.session.get('username') is not None:
        username = request.session.get('username')
        # email = request.session.get('username')
        data = tanker.objects.all().filter(username=username)
        return render(request,"tanker_view.html",{'data':data})
    else:
        return redirect("/")
def tanker_delete(request):
    messages.warning(request, "Record Deleted Successfully")
    id = request.GET["id"]
    tanker.objects.all().filter(id=id).delete()
    return redirect("/tanker_view")



def tanker_edit(request):
    id = request.GET["id"]
    data = tanker.objects.all().filter(id=id)
    return render(request,"modify_tanker.html",{'data':data})

def update_tanker(request):
    if request.method == "POST":
        messages.success(request, "Record Updated Successfully")
        i = request.POST["id"]
        m = request.POST["month"]
        y = request.POST["year"]
        t = request.POST["ttanker"]
        s = request.POST["stenant"]


        tanker.objects.all().filter(id=i).update(month=m,year=y,ttanker=t,stenant=s)

        return redirect("/tanker_view")
    else:
        return redirect("/tanker_view")




































def report(request):
    if request.session.get('username') is not None:
       return render(request,"report.html")
    else:
        return redirect("/")

def monthly_report(request):
    if request.session.get('username') is not None:
       return render(request,"monthly_report.html")
    else:
        return redirect("/")

def tanker_report(request):
    if request.session.get('username') is not None:
       return render(request,"tanker_report.html")
    else:
        return redirect("/")

def search(request):
    if request.method == "POST":
        s = request.POST["search"]
        data = tanker.objects.all().filter(year = s)
        total = tanker.objects.filter(year = s).aggregate(Total_Amount=Sum('amt'))
        # print(total['total_value'])
        return render(request,"tanker_report.html",{'data':data,'data1':total})
    else:
        return redirect("/tanker_report")

def main_search(request):
    if request.method == "POST":
        s = request.POST["search"]
        data = main.objects.all().filter(month=s)
        total = main.objects.filter(month=s).aggregate(Total_Amount=Sum('amount')) 
        # print(total['total_value'])
        return render(request, "monthly_report.html", {'data': data, 'data1': total})
    else:
        return redirect("/monthly_report")









