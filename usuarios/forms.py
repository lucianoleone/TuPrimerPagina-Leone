
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormRegistro(UserCreationForm):
    email = forms.EmailField(label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Agregar clases de Bootstrap a cada campo
        for campo in self.fields.values():
            campo.widget.attrs.update({
                "class": "form-control",
                "placeholder": campo.label
            })

# from django import forms
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
# class FormularioRegistroUsuario(UserCreationForm):
#     email = forms.EmailField(required=True)
#     password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Confirmar Contraseña', widget=forms.PasswordInput)


#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')
#         help_texts ={
#             'username': None
#         } #los que se crearon no tienen helpdesk
#         # otra forma es con un for keys
#         # help_texts = {k:None for k in fields}