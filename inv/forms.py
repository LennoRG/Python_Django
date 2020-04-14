from django import forms

from .models import Categoria, SubCategoria, Marca

class CategoriaForms(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['descripcion', 'estado']
        labels = {'descripcion': "Descripción de la Categoría",
                  "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    for field in iter(self.fields):
        self.fields[field].widget.attrs.update({
            'class':'form-control'
        })

class SubCategoriaForms(forms.ModelForm):
    categoria = forms.ModelChoiceField(
        queryset = Categoria.objects.filter(estado=True).order_by('descripcion') #No muestra las categorias inactivas
    )
    class Meta:
        model = SubCategoria
        fields = ['categoria', 'descripcion', 'estado']
        labels = {'descripcion': "Sub Categoría",
                  "estado":"Estado"}
        widget={'descripcion': forms.TextInput}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
               'class':'form-control'
            })

        self.fields['categoria'].empty_label = "Seleccione Categoria"

class MarcaForm(forms.ModelForm):
    class Meta:
        model=Marca
        fields = ['descripcion','estado']
        labels = {'descipcion': "Descripción de la Marca",
                 "estado": "Estado"}
        widget = {'descripcion': forms.TextInput()}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'forms-control'
            })
        
        