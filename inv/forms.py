from django import forms

from .models import Categoria, SubCategoria

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

class SubCategoriaForms(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset = Categoria.objects.filter(estado=True).order_by('descripcion')
    )
    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        labels = {'descripcion': "Sub Categoría",
                  "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwars):
        super().__init__(*args, **kwars)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
               'class':'form-control'
            })

        self.fields['categoria'].empty_label = "Seleccione Categoria"
        