from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
from django.db.models.functions import Length

# Create your views here.
def insert_topic(request):
    tn=input('Enter your tn')
    TUTO=Topic.objects.get_or_create(topic_name=tn)
    if TUTO[1]:
        return HttpResponse('New topic are created')
    else:
        return HttpResponse('topic is already present')

def insert_webpage(request):
    print('available Topic names are:------------')
    for i in Topic.objects.all():
        print(i.topic_name)
    tn=input('Enter your tn:-')
    LTO=Topic.objects.filter(topic_name=tn)
    if LTO:
        TO=LTO[0]
        name=input('enter a name:- ')
        url=input('enter a url:-')
        email=input('enter a email:-')
        mobile=input('enter a mobile:-')
        TUWO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email,mobile=mobile)
        if TUWO[1]:
            return HttpResponse ('new webpage created')
        else:
            return HttpResponse ('webpage already exists')
    else:
        return HttpResponse('Given topic is not available')
def insert_AccessRecord(request):
    print("available Access records are:----")
    for i in Webpage.objects.all():
        print(i.name)
    tn=input('enter names:-')
    LARO=Webpage.objects.filter(name=tn)
    if LARO:
        name=LARO[0]
        author=input('enter author name:-')
        date=input('yyyy-mm-dd:-')
        TUARO=AccessRecord.objects.get_or_create(name=name,author=author,date=date)
        if TUARO[1]:
            return HttpResponse('new object created')
        else:
            return HttpResponse ('webpage already exists')
    else:
        return HttpResponse('Given topic is not available')    
def display_topics(request):
    QSLTO=Topic.objects.all()
    d={'QSLTO':QSLTO}
    return render(request,'display_topics.html',d)

def display_webpages(request):
    Webpages=Webpage.objects.all()
    Webpages=Webpage.objects.filter(topic_name='Cricket')
    Webpages=Webpage.objects.exclude(topic_name='Cricket')
    Webpages=Webpage.objects.all()[1:4:1]
    Webpages=Webpage.objects.all().order_by('name')
    Webpages=Webpage.objects.all().order_by('-name')
    Webpages=Webpage.objects.all().order_by(Length('name'))
    Webpages=Webpage.objects.all()
    Webpages=Webpage.objects.all().order_by(Length('name').desc())
    Webpages=Webpage.objects.filter(name__startswith='s')
    Webpages=Webpage.objects.filter(name__endswith='h')
    Webpages=Webpage.objects.filter(name__contains='u')
    Webpages=Webpage.objects.filter(name__regex='^S\w+')
    Webpages=Webpage.objects.filter(name__regex='a\w+$')

    d={'Webpages':Webpages}
    return render(request,'display_webpages.html',d)
def display_accessrecords(request):
    records=AccessRecord.objects.all()
    records=AccessRecord.objects.filter(date__gt='2026-01-01')
    records=AccessRecord.objects.filter(date__lt='2026-10-01')
    records=AccessRecord.objects.filter(date__year='2026')
    records=AccessRecord.objects.filter(date__month='11')
    records=AccessRecord.objects.filter(date__day='12')
    records=AccessRecord.objects.all()
    records=AccessRecord.objects.filter(date__isnull=True)
    records=AccessRecord.objects.filter(date__isnull=False)
    d={'records':records}
    return render(request,'display_accessrecords.html',d)
def insert_topic(request):
    tn=input('enter your topic')
    TTO=Topic.objects.get_or_create(topic_name=tn)
    if TTO[1]:
        return HttpResponse('New topic is created')
    else:
        return HttpResponse('Topic is already present' )



def insert_webpage_by_form(request):
    QSLTO=Topic.objects.all()
    d={'QSLTO':QSLTO}

    if request.method=='POST':
        topic=request.POST['topic']
        TO=Topic.objects.get(topic_name=topic)
        name=request.POST['name']
        url=request.POST['url']
        email=request.POST['email']
        TWO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)
       
        if TWO[1]:
            return HttpResponse('Created')
        else:
            return HttpResponse('Present')
    return render(request,'insert_webpage_by_form.html',d)

# def insert_AccessRecord_by_form(request):
#     QSLATO=AccessRecord.objects.all()
#     d={'QSLATO':QSLATO}






def select_multiple(request):
    QSLTO=Topic.objects.all()
    d={'QSLTO':QSLTO}

    if request.method=='POST':
        topics=request.POST.getlist('topicS')
        print(topics)
        QSLTO=Webpage.objects.none()
        for topic in topics:
            QSLWO=QSLWO | Webpage.objects.filter(topic_name=topic)

        d1={'QSLWO':QSLWO}
        return render (request ,'display_webpages.html',d1)
    return render(request,'select_multiple.html',d)

def checkbox(request):
    QSLTO=Topic.objects.all()
    d={'QSLTO':QSLTO}
    return render(request,'checkbox.html',d)

        
    
 