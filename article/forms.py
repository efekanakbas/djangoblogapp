from django import forms
from .models import Article

class articlesForm(forms.ModelForm):
    class Meta:
        model=Article
        fields=["title","content","article_image"]