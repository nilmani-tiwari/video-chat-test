from django.shortcuts import render
from chat.models import *

# Create your views here.
def home(request):
    # chat = ChatMessage.objects.all()
    chat={}
    return render(request,'index.html', {'chat':chat})


from django.shortcuts import render,redirect
 
from .models import Videos
 
# Create your views here.
 
def upload_video(request):
     
    if request.method == 'POST': 
         
        title = request.POST['title']
        # video = request.POST['video']
        video= request.FILES['video']
         
        content = Videos(title=title,video=video)
        content.save()
        return redirect('/upload')
     
    return render(request,'upload.html')
 
 
def display(request):
     
    videos = Videos.objects.all()
    context ={
        'videos':videos,
    }
     
    return render(request,'videos.html',context)



def cam(request):
    # chat = ChatMessage.objects.all()
    chat={}
    return render(request,'camra.html', {'chat':chat})


def cam2(request):
    # chat = ChatMessage.objects.all()
    chat={}
    return render(request,'cam2.html', {'chat':chat})
