from django.shortcuts import render,redirect
from django.http import HttpResponse
from college.models import Department,User,Teacher,Student
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def adminhome(request):
    return render(request,'adminhome.html')

def add_dep(request):
    if request.method=='POST':
        dep=request.POST['dep']
        x=Department.objects.create(dep_name=dep)
        x.save()
        return HttpResponse('success')
    else:
        return render(request,'adddep.html')
    
def teacheradd(request):
    if request.method=='POST':
        dep=request.POST['depname']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['usr']
        pas=request.POST['pass']
        age=request.POST['age']
        add=request.POST['add']
        q=request.POST['qual']

        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=pas,usertype='Teacher')
        x.save()
        y=Teacher.objects.create(Age=age,Address=add,Qualification=q,tid=x,depid_id=dep)
        y.save()
        return HttpResponse('success')
    else:
        x=Department.objects.all()
        return render (request,'addteacher.html',{'data':x})
    

def mainhome(request):
    return render (request,'mainhome.html')


def add_stud(request):
    if request.method=='POST':
        dep=request.POST['depname']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['usr']
        pas=request.POST['pass']
        age=request.POST['age']
        add=request.POST['add']
        ph=request.POST['phno']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=pas,usertype='Student',is_active=False)
        x.save()
        y=Student.objects.create(Age=age,Address=add,Phoneno=ph,depid_id=dep,sid=x)
        y.save()
        return HttpResponse('success')
    else:


        x=Department.objects.all()
        return render (request,'addstud.html',{'data':x})

def teacherhome(request):
    return render (request,'teacherhome.html')

def studenthome(request):
    return render (request,'studenthome.html')


def logins(request):
    if request.method=='POST':
        un=request.POST['uname']
        ps=request.POST['pass']
        user=authenticate(username=un,password=ps)
        if user is not None and user.is_superuser==1:
            return redirect(adminhome)
        elif user is not None and user.usertype=="Teacher":
            login(request,user)
            request.session['teacher_id']=user.id
            return redirect(teacherhome)
        elif user is not None and user.usertype=="Student":
            login(request,user)
            request.session['stud_id']=user.id
            return redirect(studenthome)
        else:
            return HttpResponse ('invalid')
    else:
        return render(request,'logins.html')
    

def Studentview(request):
    x=Student.objects.all()
    return render(request,'studentviewins.html',{'data':x})

def approve(request,aid):
    st=Student.objects.get(id=aid)
    st.sid.is_active=True
    st.sid.save()
    return redirect(Studentview)

def approvestud(request):
    x=Student.objects.filter(sid_id__is_active=1)
    return render (request,'approvestud.html',{'data':x})

def logouts(request):
    logout(request)
    return redirect(logins)

