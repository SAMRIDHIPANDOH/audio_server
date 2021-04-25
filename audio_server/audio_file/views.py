from django.shortcuts import render,redirect
from .forms import SongForm,AudioForm,PodcastForm,AudioBookForm,audio_type,forms
from .models import song,podcast,audioType,audiobook
from django.http import HttpResponse
from datetime import date,datetime


table={'song':song,'podcast':podcast,'audiobook':audiobook}

def audio_select(request):
        context = {'audio_type': audioType.objects.all()}
        return render(request, "audio_file/audio_type.html", context)



def create_api(request,audioFileType):
   for key , values in audio_type.items():
       if audioFileType==key:
           try:
               if request.method == "GET":
                   form = values()
                   return render(request,"audio_file/audio_form.html", {'form': form,'key':key})
               else:
                   form = values(request.POST)

                   if form.is_valid():
                       form.save()
                   return redirect("/audio/" + audioFileType + "/list")
           except:
               return HttpResponse("The request is invalid: 400 bad request", 400)


def get_api(request,audioFileType):
    for key, values in table.items():
        if audioFileType == key:
            try:
                if request.method == "GET":
                    form = values
                    context = {'audio_list': form.objects.all(), 'key': key}

                return render(request, "audio_file/audio_list.html", context)
            except:
                return HttpResponse("The request is invalid: 400 bad request", 400)


def update_api(request,audioFileType,audioFileID):

       for key, values in audio_type.items():
           if audioFileType == key:
               try:
                   if request.method == "GET":
                       type = table[key]
                       audio = type.objects.get(pk=audioFileID)
                       form = values(instance=audio)
                       return render(request, "audio_file/audio_form.html", {'form': form, 'key': key})
                   else:
                       type = table[key]
                       audio = type.objects.get(pk=audioFileID)
                       form = values(request.POST, instance=audio)
                       if form.is_valid():
                           form.save()
                       return redirect("/audio/" + audioFileType + "/list")
               except:
                   return HttpResponse("The request is invalid: 400 bad request", 400)







def delete_api(request,audioFileType,audioFileID):
    for key, values in audio_type.items():
        if audioFileType == key:
            try:
                audioFileType=key
                type=table[key]
                audio = type.objects.get(pk=audioFileID)
                audio.delete()
                return redirect("/audio/"+audioFileType+"/list")

            except:
                return HttpResponse("The request is invalid: 400 bad request", 400)
        