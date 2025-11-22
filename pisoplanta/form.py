import django.forms as forms
class CrearCentro(forms.Form):
    nombre = forms.CharField(max_length=100)
    operacion = forms.CharField(max_length=100)
    activo = forms.BooleanField(required=False)
    imagen=forms.ImageField(required=False)

class BuscarCentro(forms.Form):
    nombre = forms.CharField(max_length=100, required=False)