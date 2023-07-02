import mysql.connector
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from datetime import date
# Create your views here.

def home(request):
    return render(request, 'home.html')

def adminlogin(request):
    return render(request,'adminlogin.html')
def adminhome(request):
    return render(request,'adminhome.html')
def adminvalidation(request):
    a=request.GET.get('gname')
    b=request.GET.get('cname')
    if a=='admin' and b=='admin':
        return render(request,'adminhome.html')
    else:
        return render(request,'adminlogin.html',{'check':' check the username & password'})
    

def admintutorrequest(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from tutor where status='create'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    print(row)
    rows=row
    mydb.close()



    return render(request,'admintutorrequest.html',{'rows':rows})    

def adminapproveform(request):
    aprovenumber=request.GET.get('approveid')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="UPDATE tutor SET status = 'approved' WHERE tutorid='"+str(aprovenumber)+"' "
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return admintutorrequest(request)



def admintutordetails(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from tutor where status='approved'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    print(row)
    rows=row
    mydb.close()
    return render(request,'admintutordetails.html',{'approvetutor':rows})

def adminviewparents(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from parent where status='create'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    print(row)
    rows=row
    mydb.close()
    return render(request,'adminparentview.html' ,{'parentview':rows})   
def adminbookmanage(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from ebooks"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    print(row)
    mydb.close()

    return render (request,'adminbookview.html',{'book':row}) 


def adminvideomanage(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from video"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    print(row)
    mydb.close()
    return render(request,'adminvideomanage.html',{'video':row})


def adminbookapprove(request):
    a=request.GET.get('bidholder')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q='UPDATE ebooks SET status = "approved" WHERE bookid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return adminbookmanage(request)

def adminvideoapprove(request):
    a=request.GET.get('bidholder')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q='UPDATE video SET status = "approved" WHERE videoid="'+str(a)+'"'
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return adminvideomanage(request)

def adminratingview(request):
    tname=request.session['tutorname']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from rating "
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    

    return render(request,'adminratingview.html',{'tutorname':tname,'rating':row})


def admintutordelete(request):
    deleteid=request.GET.get('deletevalue')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="delete from tutor where tutorid='"+str(deleteid)+"'"
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return admintutordetails(request)

def adminmarklistview(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from marklist"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    return render(request,'adminmarklistview.html',{'marklist':row})

    


    
#tutor
    
def tutorregister(request):
    return render(request,'tutorregister.html')
def  tutorlogin(request):
    return render(request,'tutorlogin.html')
def tutorhome(request):
    return render (request,'tutorhome.html',{'tutorname':request.session['tutorname']})
def tutorregisterhandler(request):
    path='myclass/static/tutorprofile'
    if request.FILES['file']:
         name=request.POST.get('name')
         gender=request.POST.get('gender')
         qualification=request.POST.get('qualification')
         number=request.POST.get('number')
         email=request.POST.get('email')
         dob=request.POST.get('dob')
         subject=request.POST.get('subject')
         date=request.POST.get('date')
         experience=request.POST.get('experience')
         fees=request.POST.get('fees')
         username=request.POST.get('username')
         password=request.POST.get('password')
         file=request.FILES['file']
         fs=FileSystemStorage(location=path)
         filename=fs.save(file.name,file)
         file_url=fs.url(filename)
         mydb=mysql.connector.Connect(host='localhost', user='root', password='akshaysajitha', database='onlineclassdb')
         mycursor=mydb.cursor()
         q = "INSERT INTO tutor (name, gender,qualification,phone,email,dob,subject,class,experience,fees,username,password,photo)VALUES('"+name+"','"+gender+"','"+qualification+"','"+number+"','"+email+"','"+dob+"','"+subject+"','"+date+"','"+experience+"','"+fees+"','"+username+"','"+password+"','"+str(file)+"')"
         print(q)
         mycursor.execute(q)
         mydb.commit()
         mydb.close()
         return tutorlogin(request)
    return tutorlogin(request)

    
    



def tutorloginhandler(request):
    a=request.GET.get('gname')
    b=request.GET.get('cname')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from tutor where username='"+a+"' and password='"+b+"'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchone()
    print(row)
    mydb.close()
    x=row
    if row is None:
        return render (request,'tutorlogin.html',{'nouser':'no user found'})
    elif x[13]=='create':
        return render (request,'tutorlogin.html',{'nouser':'not approved'})

    elif x[13]=='approved':
        
        request.session['tutorid']=x[0]
        request.session['tutorname']=x[1]
        request.session['tutorfees']=x[10]

        return render (request,'tutorhome.html',{'tutorname':request.session['tutorname']})
    else:
         return render (request,'tutorlogin.html')
    

def tutorprofileupdate(request):
    a=request.session['tutorid']
    print(a)
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from tutor where tutorid='"+str(a)+"' "
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchone()
    print(row)
    mydb.close()
    return render(request,'tutorprofileupdate.html',{'tutorname':request.session['tutorname'],'profile':row})    

def updatetutorform(request):
    a=request.GET.get('Qualification')
    b=request.GET.get('Phone')
    c=request.GET.get('Email')
    d=request.GET.get('subject')
    e=request.GET.get('class')
    f=request.GET.get('Experience')
    g=request.session['tutorid']
    h=request.GET.get('fees')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="update tutor set qualification='"+a+"',phone='"+b+"',email='"+c+"',subject='"+d+"',class='"+e+"',experience='"+f+"',fees='"+h+"' where tutorid='"+str(g)+"' "
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return tutorprofileupdate(request)

def tutoruploadpdf(request):
    return render(request,'tutorpdfupload.html',{'tutorname':request.session['tutorname']})

def tutorvideoupload(request):
    return render(request,'tutorvideoupload.html',{'tutorname':request.session['tutorname']})



def tutoruploadpdfform(request):
    path='myclass/static/ebook'
    if request.FILES['file']:
       tutorid=request.session['tutorid']
       name=request.POST.get('bookname')
       subject=request.POST.get('subject')
       class1=request.POST.get('class1')
       tutorname=request.session['tutorname']
       day= date.today()
       file=request.FILES['file']
       fs=FileSystemStorage(location=path)
       filename=fs.save(file.name,file)
       file_url=fs.url(filename)
       
       mydb=mysql.connector.Connect(host='localhost', user='root', password='akshaysajitha', database='onlineclassdb')
       mycursor=mydb.cursor()
       q = "INSERT INTO ebooks (bookname,bookpdf,subject,class,tutorid,tutorname,date)VALUES('"+str(name)+"','"+str(file)+"','"+str(subject)+"','"+str(class1)+"','"+str(tutorid)+"','"+tutorname+"','"+str(day)+"')"
       print(q)
       mycursor.execute(q)
       mydb.commit()
       mydb.close()
       
       return  tutoruploadpdf(request)
    return  tutoruploadpdf(request)


def tutoruploadvideoform(request):
    path='myclass/static/video'
    if request.FILES['file']:
       tutorname=request.session['tutorname']
       tutorid=request.session['tutorid']
       name=request.POST.get('videoname')
       subject=request.POST.get('subject')
       class1=request.POST.get('class1')
       day= date.today()
       file=request.FILES['file']
       fs=FileSystemStorage(location=path)
       filename=fs.save(file.name,file)
       file_url=fs.url(filename)
       mydb=mysql.connector.Connect(host='localhost', user='root', password='akshaysajitha', database='onlineclassdb')
       mycursor=mydb.cursor()
       q = "INSERT INTO video (videoname,videofile,subject,class,tutorid,tutorname,date)VALUES('"+str(name)+"','"+str(file)+"','"+str(subject)+"','"+str(class1)+"','"+str(tutorid)+"','"+tutorname+"','"+str(day)+"')"
       print(q)
       mycursor.execute(q)
       mydb.commit()
       mydb.close()
       
       return tutorvideoupload (request)
    return  tutorvideoupload(request)

def tutorparentrequest(request):
    tid=request.session['tutorid']
    tname=request.session['tutorname']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from payment where tutorid='"+str(tid)+"' and status='create'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    return render(request,'tutorparentrequest.html',{'rows':row,'tutorname':tname})

   
def tutorparentapproveform(request):
    aprovenumber=request.GET.get('approveid')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="UPDATE payment SET status ='approved' WHERE pid='"+str(aprovenumber)+"'"
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return tutorparentrequest(request)
def tutorparentdeleteform(request):
    aprovenumber=request.GET.get('approveid')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="delete from payment WHERE pid='"+str(aprovenumber)+"' "
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return tutorparentrequest(request)

def tutorviewpayment(request):
    tid=request.session['tutorid']
    tname=request.session['tutorname']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from payment where tutorid='"+str(tid)+"' and status='payed'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    return render(request,'tutorviewpayment.html',{'rows':row,'tutorname':tname})

def tutordiscussion(request):
    tid=request.session['tutorid']
    tname=request.session['tutorname']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from payment where tutorid='"+str(tid)+"' and status='payed'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    

    return render (request,'tutordiscussion.html',{'discussion':row,'tutorname':tname})

def tutordiscussionprofile(request):
    tid=request.session['tutorid']
    tname=request.session['tutorname']
    parentid=request.GET.get('pid')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from parent where parentid='"+str(parentid)+"'"
    print(q)
    mycursor.execute(q)
    onerow=mycursor.fetchone()
    
    request.session['chatparentid']=onerow[0]
    request.session['chatparentname']=onerow[1]
    spid=request.session['chatparentid'] 
    spname=request.session['chatparentname']
    chat="select * from discussion where fromid='"+str(spid)+"' and toid='"+str(tid)+"' " 
    mycursor.execute(chat)
    row=mycursor.fetchall()
    print(row)
    tchat="select * from discussion where fromid='"+str(tid)+"' and toid='"+str(spid)+"' " 
    print(tchat)
    mycursor.execute(tchat)
    trow=mycursor.fetchall()
    print(trow)


    mydb.close()

    return render(request,'tutormsgdiscussion.html',{'tutorname':tname,'discussion':onerow ,'tchat':trow,'chat':row})


def tutorchatadd(request):
    spid=request.session['chatparentid']
    spname=request.session['chatparentname']

    tid=request.session['tutorid']
    tname=request.session['tutorname']
    frid=request.GET.get('chatid')
    frname=request.GET.get('chatname')
    msg=request.GET.get('msg')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="insert into discussion(fromid,fromname,toid,toname,msg)values('"+str(tid)+"','"+str(tname)+"','"+str(spid)+"','"+str(spname)+"','"+str(msg)+"')"
    mycursor.execute(q)
    mydb.commit()
    count = 1
    if count > 0:
        chat="select * from discussion where fromid='"+str(spid)+"' and toid='"+str(tid)+"' " 
        mycursor.execute(chat)
        row=mycursor.fetchall()
        print(row)
        tchat="select * from discussion where fromid='"+str(tid)+"' and toid='"+str(spid)+"' " 
        print(tchat)
        mycursor.execute(tchat)
        trow=mycursor.fetchall()
        print(trow)
        return render(request,'tutormsgdiscussion.html',{'chat':row ,'tutorname':tname ,'parent':spname,'tchat':trow})



    mydb.close()
    
   

    return render(request,'tutormsgdiscussion.html',{'tutorname':tname ,'parent':spname})
    


def tutoronlinetest(request):
    tname=request.session['tutorname']
    
    return render (request,'tutoronlinetest.html',{'tutorname':tname})     

def tutoronlinetestform(request):
    tname=request.session['tutorname']
    tutorid=request.session['tutorid']
    day= date.today()
    question=request.GET.get('question')
    option1=request.GET.get('option1')
    option2=request.GET.get('option2')
    option3=request.GET.get('option3')
    option4=request.GET.get('option4')
    crtanswer=request.GET.get('crtanswer')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="insert into onlinetest(tutorid,tutorname,date,question,option1,option2,option3,option4,correctanswer)values('"+str(tutorid)+"','"+tname+"','"+str(day)+"','"+question+"','"+option1+"','"+option2+"','"+option3+"','"+option4+"','"+crtanswer+"')"
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return render (request,'tutoronlinetest.html',{'tutorname':tname})

def tutorsetprogresscard(request):
    tid=request.session['tutorid']
    tname=request.session['tutorname']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from payment where tutorid='"+str(tid)+"' and status='payed'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    

    return render (request,'tutorprogress.html',{'progress':row,'tutorname':tname})

def tutorprogressprofile(request):
    tid=request.session['tutorid']
    tname=request.session['tutorname']
    parentid=request.GET.get('pid')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from parent where parentid='"+str(parentid)+"'"
    print(q)
    mycursor.execute(q)
    onerow=mycursor.fetchone()
    
    request.session['chatparentid']=onerow[0]
    request.session['chatparentname']=onerow[1]
    spid=request.session['chatparentid']
    spname=request.session['chatparentname']
    tchat="select * from progress where tutorid='"+str(tid)+"' and parentid='"+str(spid)+"' " 
    print(tchat)
    mycursor.execute(tchat)
    trow=mycursor.fetchall()
    print(trow)


    mydb.close()

    return render(request,'tutorprogressprofile.html',{'tutorname':tname,'discussion':onerow ,'tchat':trow})

def tutorprogressadd(request):
    path='myclass/static/progress'
    if request.FILES['file']:
        spid=request.session['chatparentid']
        spname=request.session['chatparentname']
        tid=request.session['tutorid']
        tname=request.session['tutorname']
        name=request.POST.get('progressdtl')
        file=request.FILES['file']
        fs=FileSystemStorage(location=path)
        filename=fs.save(file.name,file)
        file_url=fs.url(filename)
        mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
        mycursor=mydb.cursor()
        q="insert into progress(tutorid,tutorname,parentid,parentname,progressdtl,progresscard)values('"+str(tid)+"','"+str(tname)+"','"+str(spid)+"','"+str(spname)+"','"+str(name)+"','"+str(file)+"')"
        mycursor.execute(q)
        mydb.commit()
        tchat="select * from progress where tutorid='"+str(tid)+"' and parentid='"+str(spid)+"' " 
        print(tchat)
        mycursor.execute(tchat)
        trow=mycursor.fetchall()
        mydb.close()
        print(trow)
        return render(request,'tutorprogressprofile.html',{'tutorname':tname ,'parent':spname,'tchat':trow})
    
    return render(request,'tutorprogressprofile.html',{'tutorname':tname ,'parent':spname})
def tutorviewfeedback(request):
    tid=request.session['tutorid']
    tname=request.session['tutorname']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from rating where tutorid='"+str(tid)+"'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    

    return render(request,'tutorratingview.html',{'tutorname':tname,'rating':row})

def tutordeleteuploadquestion(request):
    tid=request.session['tutorid']
    tname=request.session['tutorname']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from onlinetest where tutorid='"+str(tid)+"'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    return render (request,'tutordeleteuploadquestion.html',{'question':row,'tutorname':tname})

def tutorquestiondelete(request):
    a=request.GET.get('qid')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="delete from onlinetest where testid='"+str(a)+"'"
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return tutordeleteuploadquestion(request)

def tutorexammarklist(request):
    tid=request.session['tutorid']
    tname=request.session['tutorname']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from marklist where tutorid='"+str(tid)+"'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    return render(request,'tutorexammarklist.html',{'marklist':row,'tutorname':tname})




   


    
    




    #parents 

def parentlogin(request):
    return render (request,'parentlogin.html')    

def parentregister(request):
    return render(request,'parentregister.html')

def parenthome(request):
    return render(request,'parenthome.html')

def parentregisterhandler(request):
    path='myclass/static/parentprofile'
    if request.FILES['file']:
         
         name=request.POST.get('name')
         gender=request.POST.get('gender')
         qualification=request.POST.get('qualification')
         number=request.POST.get('number')
         email=request.POST.get('email')
         dob=request.POST.get('dob')
         address=request.POST.get('address')
         day= date.today()
         username=request.POST.get('username')
         password=request.POST.get('password')
         file=request.FILES['file']
         fs=FileSystemStorage(location=path)
         filename=fs.save(file.name,file)
         file_url=fs.url(filename)
         mydb=mysql.connector.Connect(host='localhost', user='root', password='akshaysajitha', database='onlineclassdb')
         mycursor=mydb.cursor()
         q = "INSERT INTO parent (name, gender,qualification,phone,email,dob,address,date,username,password,photo)VALUES('"+name+"','"+gender+"','"+qualification+"','"+number+"','"+email+"','"+dob+"','"+address+"','"+str(day)+"','"+username+"','"+password+"','"+str(file)+"')"
         print(q)
         mycursor.execute(q)
         mydb.commit()
         mydb.close()
         return parentlogin(request)
    return parentlogin(request)

    


    
def parentloginhandler(request):
    a=request.GET.get('gname')
    b=request.GET.get('cname')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from parent where username='"+a+"' and password='"+b+"'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchone()
    print(row)
    mydb.close()
    x=row
    print(x)
    if row is None:
        return render (request,'parentlogin.html',{'nouser':'no user found'})
    else:
         request.session['parentid']=x[0]
         b=request.session['parentname']=x[1]
         print(b)
         a=request.session['parentprofile']=x[12]
         print(a)
         return render (request,'parenthome.html',{'pname':request.session['parentname']})
def parentupdateprofile(request):
    a=request.session['parentid']
    print(a)
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from parent where parentid ='"+str(a)+"' "
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchone()
    print(row)
    mydb.close()
    return render(request,'parentupdateprofile.html',{'name':request.session['parentname'],'profile':row})    

def parentupdateform(request):
    a=request.GET.get('Qualification')
    b=request.GET.get('Phone')
    c=request.GET.get('Email')
    d=request.GET.get('address')
    e=request.GET.get('username')
    f=request.GET.get('password')
    g=request.session['parentid']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="update parent set qualification='"+a+"',phone='"+b+"',email='"+c+"',address='"+d+"',username='"+e+"',password='"+f+"' where parentid='"+str(g)+"' "
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return parentupdateprofile (request)

def parenttutorinfo(request):
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from tutor where status='approved'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    print(row)
    rows=row
    mydb.close()
    return render(request,'parenttutorinfo.html',{'approvetutor':rows  ,'pname':request.session['parentname']})
def parenttutorview(request):
    parentid =request.session['parentid']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from payment where parentid ='"+str(parentid)+"'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    print(row)
    mydb.close()
    return render(request,'parenttutorview.html',{'payment':row ,'pname':request.session['parentname']})
def parentpaymenthandler(request):
    tid=request.GET.get('tutorid')
    tname=request.GET.get('tutorname')
    cls=request.GET.get('classvalue')
    subject=request.GET.get('subject')
    price=request.GET.get('price')
    pname=request.session['parentname']
    parentd=request.session['parentid']
    parentphotoup=request.session['parentprofile']
    tprofile=request.GET.get('profile')
    day= date.today()
    mydb=mysql.connector.Connect(host='localhost', user='root', password='akshaysajitha', database='onlineclassdb')
    mycursor=mydb.cursor()
    check_query = "SELECT COUNT(*) FROM payment WHERE tutorid=%s AND parentid=%s"
    check_data = (tid, parentd)
    mycursor.execute(check_query, check_data)
    count = mycursor.fetchone()[0]
    if count > 0:
        # a payment record already exists, so display an error message
        message = "you already book this tutor."
        return render(request, 'parenttutorview.html', {'message': message})
    else:
        # insert a new payment record
        q = "INSERT INTO payment (tutorid,tutorname,class,subject,parentid,parentname,price,date,parentphoto,tutorphoto)VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        payment_data = (tid, tname, cls, subject, parentd, pname, price, day,parentphotoup,tprofile)
        mycursor.execute(q, payment_data)
        mydb.commit()
        mydb.close()
        return parenttutorview(request)

def parentpaytutor(request):
    payid=request.GET.get('payvalue')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="UPDATE payment SET status ='payed' WHERE pid='"+str(payid)+"'"
    print(q)
    mycursor.execute(q)
    mydb.commit()
    mydb.close()
    return  parenttutorview(request)
def parentbookview(request):
    parentid =request.session['parentid']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from payment where status='payed' and parentid ='"+str(parentid)+"'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    print (row)
    if len(row) > 0:
        request.session['tid'] = row[0][1]
        request.session['status'] = row[0][9]
        tid = request.session['tid']
        st = 'approved'
        bq = "SELECT * FROM ebooks WHERE tutorid = %s and status= %s "
        mycursor.execute(bq, (tid,st))
        brow = mycursor.fetchall()
        return render(request, 'parentbookview.html', {'bookrowpname': brow, 'pname': request.session['parentname']})
    return render(request,'parentbookview.html',{'pname':request.session['parentname']})

def parentvideoview(request):
    parentid =request.session['parentid']
    classmsg='please wait'
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from payment where status='payed' and parentid ='"+str(parentid)+"'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    print (row)
    if len(row) > 0:
        request.session['tid'] = row[0][1]
        request.session['status'] = row[0][9]
        tid = request.session['tid']
        st = 'approved'
        bq = "SELECT * FROM video WHERE tutorid = %s and status= %s "
        mycursor.execute(bq, (tid,st))
        brow = mycursor.fetchall()
        return render(request, 'parentvideoview.html', {'bookrowpname': brow, 'pname': request.session['parentname'],})
    else:
      return render(request,'parentvideoview.html',{'pname':request.session['parentname'],'cls':classmsg})
    
def parentdiscussion(request):
    parentid =request.session['parentid']
    pname=request.session['parentname']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from payment where status='payed' and parentid ='"+str(parentid)+"'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    return render (request,'parentdiscussion.html',{'discussion':row,'pname':request.session['parentname']})

def parentdiscussionprofile(request):
    pname=request.session['parentname']
    tutortid=request.GET.get('pid')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from tutor where tutorid='"+str(tutortid)+"'"
    print(q)
    mycursor.execute(q)
    onerow=mycursor.fetchone()
    
    request.session['chattutorid']=onerow[0]
    request.session['chattutorname']=onerow[1]

    spid=request.session['chatparentid']
    spname=request.session['chatparentname']
    chat="select * from discussion where fromid='"+str(spid)+"' and toid='"+str(tutortid)+"' " 
    mycursor.execute(chat)
    row=mycursor.fetchall()
    print(row)
    tchat="select * from discussion where fromid='"+str(tutortid)+"' and toid='"+str(spid)+"' " 
    print(tchat)
    mycursor.execute(tchat)
    trow=mycursor.fetchall()
    print(trow)
    mydb.close()



    return render(request,'parentmsgdiscussion.html',{'pname':pname,'discussion':onerow ,'tchat':trow,'chat':row})

def parentchatadd(request):
    spid=request.session['chattutorid']
    spname=request.session['chattutorname']

    pid=request.session['parentid']
    pname=request.session['parentname']
    msg=request.GET.get('msg')
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="insert into discussion(fromid,fromname,toid,toname,msg)values('"+str(pid)+"','"+str(pname)+"','"+str(spid)+"','"+str(spname)+"','"+str(msg)+"')"
    mycursor.execute(q)
    mydb.commit()
    count = 1
    if count > 0:
        chat="select * from discussion where fromid='"+str(pid)+"' and toid='"+str(spid)+"' " 
        mycursor.execute(chat)
        row=mycursor.fetchall()
        tchat="select * from discussion where fromid='"+str(spid)+"' and toid='"+str(pid)+"' " 
        mycursor.execute(tchat)
        print(tchat)
        trow=mycursor.fetchall()
        print(trow)
        return render(request,'parentmsgdiscussion.html',{'tchat':trow ,'tutorname':pname ,'parent':spname,'chat':row })



    mydb.close()
   

    return render(request,'parentmsgdiscussion.html',{'tutorname':pname ,'parent':spname})


def parentonlinetest(request):
    parentid =request.session['parentid']
    pname=request.session['parentname']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from payment where status='payed' and parentid ='"+str(parentid)+"'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()
    mydb.close()
    

    return render (request,'parentonlinetest.html',{'pname':request.session['parentname'],'discussion':row})

def parentstartonlinetest(request):
    tutortid = request.GET.get('pid')

    mydb = mysql.connector.connect(host='localhost', user='root', password='akshaysajitha', database='onlineclassdb')
    mycursor = mydb.cursor()

    q = "SELECT * FROM onlinetest WHERE tutorid = '" + str(tutortid) + "'"
    print(q)
    mycursor.execute(q)
    rows = mycursor.fetchall()
    

    mydb.close()
    request.session['answertid']=rows[0][1]
    request.session['answertname']=rows[0][2]
    antid=request.session['answertid']
    antname=request.session['answertname']

    print(antid)
    print(antname)

    return render(request, 'parentquesonlinetest.html', {'pname': request.session['parentname'], 'drows':rows})

def parentanswer(request):
    pname=request.session['parentname']
    pid=request.session['parentid']
    tutortid = request.session['answertid']
    tutorname=request.session['answertname']
    day=date.today()

    mydb = mysql.connector.connect(host='localhost', user='root', password='akshaysajitha', database='onlineclassdb')
    mycursor = mydb.cursor()

    q = "SELECT * FROM onlinetest WHERE tutorid = '" + str(tutortid) + "'"
    print(q)
    mycursor.execute(q)
    rows = mycursor.fetchall()
    

    
    correctanswer=[]
    examanswer=[]
    score = 0
    for x in rows:
        a=x[0]
      
        crtanswer=x[9]
        correctanswer.append(crtanswer)

        
        value=request.GET.get('op'+str(a))
        
        examanswer.append(value)
        
    for i in range(len(correctanswer)):
        if correctanswer[i]==examanswer[i]:
            score += 1

        
    
    totalmark=len(correctanswer)
    request.session['markget']=totalmark
    

    ansinsert = "INSERT INTO marklist (tutorid,tutorname,parentid,parentname,date,mark)VALUES('"+str(tutortid)+"','"+str(tutorname)+"','"+str(pid)+"','"+str(pname)+"','"+str(day)+"','"+str(score)+"')"
    mycursor.execute(ansinsert)
    print(ansinsert)
    mydb.commit()
    mydb.close()



    
    
        
        

    
    
    return render(request, 'parentmarkscore.html',{'mark':score,'pname': request.session['parentname'],'totalmark':totalmark})

def parentProgresscard(request):
    id=request.session['parentid']
    mydb=mysql.connector.Connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycurser=mydb.cursor()
    q="select * from progress where parentid='"+str(id)+"'"
    mycurser.execute(q)
    row=mycurser.fetchall()
    mydb.close()

    return render(request, 'parentprogresscard.html', {'pname': request.session['parentname'],'progresscard':row})


def parentrating(request):
    tid=request.GET.get('tid')
    tname=request.GET.get('tname')
    pid=request.session['parentid']
    pname=request.session['parentname']
    feed1=request.GET.get('feed')
    print(request.GET)
    print(feed1)
    rat=request.GET.get('rating')
    print(rat)
    mydb=mysql.connector.Connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycurser=mydb.cursor()
    q="insert into rating (parentid,parentname,tutorid,tutorname,rating,feedback)values('"+str(pid)+"','"+str(pname)+"','"+str(tid)+"','"+str(tname)+"','"+str(rat)+"','"+str(feed1)+"')"
    mycurser.execute(q)
    print(q)
    mydb.commit()
    mydb.close()
    return render(request,'parenttutorview.html',{'pname':request.session['parentname']})

def parentmarklist(request):
    pid=request.session['parentid']
    mydb=mysql.connector.connect(host='localhost',user='root',password='akshaysajitha',database='onlineclassdb')
    mycursor=mydb.cursor()
    q="select*from marklist where parentid='"+str(pid)+"'"
    print(q)
    mycursor.execute(q)
    row=mycursor.fetchall()

    return render(request,'parentmarklistpage.html',{'pname':request.session['parentname'],'marklist':row})

    

    








    

   


    


    




    



    





           



    



    
    




