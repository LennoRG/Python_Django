from django import forms

from .models import Categoria

class CategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción de la Categoría",
                  "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

def __init__(self, *args, **kwars):
    super().__init__(*args, **kwars)
    for field in iter(self.fields):
        self.fields[field].widget.attrs.update({
            'class':'form-control'
        })
        