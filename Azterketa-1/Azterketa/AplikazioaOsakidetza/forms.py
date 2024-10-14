from django import forms
from .models import Medikua,Paziente,Zitak
class MedikuForm(forms.ModelForm):
 class Meta:
    model=Medikua
    fields=['izena','abizena','jaiotze_data']
class MedikuaAldatuForm(forms.ModelForm):
 class Meta:
     model=Medikua
     fields=['izena','abizena','jaiotze_data']
class PazienteForm(forms.ModelForm):
 class Meta:
    model=Paziente
    fields=['izena','abizena','jaiotze_data']
class ZitakForm(forms.ModelForm):
 class Meta:
    model=Zitak
    fields=['pazientekodea','medikukodea','zita_data']
class ZitakGehituForm(forms.ModelForm):
 class Meta:
    model=Zitak
    fields=['pazientekodea','medikukodea','zita_data']