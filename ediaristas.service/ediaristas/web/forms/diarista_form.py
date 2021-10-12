from django import forms
from ..models import Diarista


class DiaristaForm(forms.ModelForm):
    cpf = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '000.000.000-00'}))
    cep = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '00000-000'}))
    telefone = forms.CharField(widget=forms.TextInput(attrs={'data-mask': '(00)00000-0000'}))

    class Meta:
        model = Diarista
        fields = '__all__'
