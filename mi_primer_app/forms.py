from django import forms


class CursoForm(forms.Form):
    nombre = forms.CharField(max_length=100, label = 'Nombre del Curso')
    descripcion = forms.CharField(widget=forms.Textarea, label='Descripcion')
    duracion_semanas = forms.IntegerField(label='Duracion (semanas)')
    fecha_inicio = forms.DateField(
        widget=forms.SelectDateWidget, label = 'Fecha de inicio')
    fecha_fin = forms.DateField(
        widget=forms.SelectDateWidget, label='Fecha de fin')
    activo = forms.BooleanField(
        required=False, initial=True, label='Activo') #Campo Opcional

    def __str__(self):
        return self.nombre