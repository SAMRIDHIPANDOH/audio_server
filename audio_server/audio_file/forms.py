from django import forms
from .models import song,audioType,podcast,audiobook
from datetime import date,datetime,timezone
from django.core.exceptions import ValidationError
from django.contrib.admin.widgets import AdminDateWidget
class SongForm(forms.ModelForm):
    class Meta:
        model=song
        fields="__all__"


        labels={
            'duration': 'Duration(in seconds)',
            'upload_time':'Upload Time'
        }


class PodcastForm(forms.ModelForm):
    class Meta:
        model=podcast
        fields="__all__"
        labels={
                'duration' : 'Duration(in seconds)',
                'upload_time':'Upload Time'
            }

    def __init__(self,*args,**kwargs):
        super(PodcastForm,self).__init__(*args,**kwargs)
        self.fields['participants'].required = False



class AudioBookForm(forms.ModelForm):
    class Meta:
        model=audiobook
        fields="__all__"
        labels={
            'duration': 'Duration(in seconds)',
            'upload_time':'Upload Time'
        }

class AudioForm(forms.ModelForm):
    class Meta:
        model=audioType
        fields="__all__"


audio_type={'song':SongForm,'podcast':PodcastForm,'audiobook':AudioBookForm}