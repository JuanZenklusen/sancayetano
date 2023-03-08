from django.forms import ModelForm, DateInput, TextInput
from .models import Cronograma, Capilla, Misa, Musico

class CronogramaForm(ModelForm):
    class Meta:
        model = Cronograma
        fields = '__all__'
        widgets = {
            'date': DateInput(attrs={'type':'date'}),
        }
        
class CapillaForm(ModelForm):
    class Meta:
        model = Capilla
        fields = '__all__'
        
class MisaForm(ModelForm):
    class Meta:
        model = Misa
        fields = '__all__'
        widgets = {
            'fecha': DateInput(attrs={'type':'date'}),
            'cronograma': TextInput(attrs={'class':'no_mostrar'})
        }
        
class MusicoForm(ModelForm):
    class Meta:
        model = Musico
        fields = '__all__'