from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    def _init_(self,*args,**kwargs):
        super(CommentForm,self)._init_(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs={'class':'form-control'}

        self.fields['bio'].widget.attrs['rows'] = 10
        self.fields['bio'].widget.attrs['cols'] = 50
        self.fields['bio'].widget.attrs['placeholder'] = "Yorum yaz..."

    class Meta:
            model = Comment
            fields = ['ad_soyad','bio']
