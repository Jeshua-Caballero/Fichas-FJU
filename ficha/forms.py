from django import forms
from .models import PerfilUsuario, FichaJoven
# create your forms here.

class EditarPerfilForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['departamento', 'es_asistente']
        
        # Agregar atributos globales a todos los campos del formulario
        def __init__(self, *args, **kwargs):
            super(EditarPerfilForm, self).__init__(*args, **kwargs)
            
            for field in self.fields.values():
                field.widget.attrs.update({
                    'class': 'perfil-form',  # Aplicar la clase 'perfil-form' a todos los campos
                    'placeholder': f'Ingrese {field.label}'  # Aplicar un placeholder genérico según el nombre del campo
                })
class EditarFichaJoven(forms.ModelForm):
    class Meta:
        model = FichaJoven
        fields = ['nombre', 'iglesia', 'tribu', 'departamento']
        
        # Agregar atributos globales a todos los campos del formulario
        def __init__(self, *args, **kwargs):
            super(EditarPerfilForm, self).__init__(*args, **kwargs)
            
            for field in self.fields.values():
                field.widget.attrs.update({
                    'class': 'perfil-form',  # Aplicar la clase 'perfil-form' a todos los campos
                    'placeholder': f'Ingrese {field.label}'  # Aplicar un placeholder genérico según el nombre del campo
                })

class PrincipalForm(forms.ModelForm):
    class Meta:
        model = FichaJoven
        fields = [ 'nombre', 'sexo', 'edad', 'iglesia', 'tribu', 'como_conocio_la_iglesia', 'estado_civil', 'familia_en_iglesia', 'hijos', 'conyuge', 'quienes_son_familiares', 'canatidad_de_hijos', 'codicion_del_joven', 'testimonio']
                
        # Agregar atributos globales a todos los campos del formulario
    def __init__(self, *args, **kwargs):
        super(PrincipalForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'principal-form',  # Aplicar la clase 'perfil-form' a todos los campos
                'placeholder': f'Ingrese {field.label}'  # Aplicar un placeholder genérico según el nombre del campo
            })

class ContactoForm(forms.ModelForm):
    class Meta:
        model = FichaJoven
        fields = ['email', 'telfijo', 'telcelular', 'whatsapp', 'telegram', 'instagram', 'facebook', 'linkedin', 'youtube', 'tiktok']
    def __init__(self, *args, **kwargs):
        super(ContactoForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'contacto-form',
                'placeholder': f'{field.label}'
            })

class DomicilioForm(forms.ModelForm):
    class Meta:
        model = FichaJoven
        fields = ['direccion', 'nro_casa', 'barrio', 'ciudad', 'departamento', 'tipo_de_vivienda', 'otro_tipo_de_vivienda', 'tvotra', 'tconvivencia', 'tcotra']
    def __init__(self, *args, **kwargs):
        super(DomicilioForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'domicilio-form',
                'placeholder' : f'{field.label}'
            })

class EspiritualForm(forms.ModelForm):
    class Meta:
        model = FichaJoven
        fields = ['fechaingiglesia', 'fechaingfju', 'pregbautaguas', 'fecbautaguas', 'mombautaguas', 'obautaguas', 'pregbautEspirituSanto', 'fecbautEspSanto', 'expbautEspSanto', 'actobra', 'tiempoobra', 'servAltar', 'compintellimen', 'tiempointelli', 'probactual', 'probsup', 'probactualotro', 'psupotro', 'eapartado', 'porqueapart', 'fecapart', 'encconDios', 'grupoespiritual', 'obspastor']
    def __init__(self, *args, **kwargs):
        super(EspiritualForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'espiritual-form',
                'placeholder': f'{field.label}'
            })

class ProyectosForm(forms.ModelForm):
    class Meta:
        model = FichaJoven
        fields = ['proyjoven', 'funproyjoven', 'nivproyjoven', 'fecingproyjoven', 'respjoven']
    def __init__(self, *args, **kwargs):
        super(ProyectosForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'proyectos-form',
                'placeholder': f'{field.label}'
            })

class EstudiosForm(forms.ModelForm):
    class Meta:
        model = FichaJoven
        fields = ['nivestudiojoven', 'estestudiojoven', 'areaestjoven', 'tituloestjoven']
    def __init__(self, *args, **kwargs):
        super(EstudiosForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'estudios-form',
                'placeholder': f'{field.label}'
            })

class LaboralForm(forms.ModelForm):
    class Meta:
        model = FichaJoven
        fields = ['trabactualjoven', 'lugartrabjoven', 'tipoinsttrabjoven', 'alabtrabjoven', 'tipotrabjoven']
    def __init__(self, *args, **kwargs):
        super(LaboralForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'laboral-form', 
                'placeholder': f'{field.label}'
            })

class IdiomasForm(forms.ModelForm):
    class Meta:
        model = FichaJoven
        fields = ['idiomauno', 'niveliduno', 'idiomados', 'niveliddos', 'idiomatres', 'nivelidtres']
    def __init__(self, *args, **kwargs):
        super(IdiomasForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'idiomas-form',
                'placeholder': f'{field.label}'
            })

class TalentosForm(forms.ModelForm):
    class Meta:
        model = FichaJoven
        fields = ['talentouno', 'niveltaluno', 'otrotalentouno', 'talentodos', 'niveltaldos', 'otrotalentodos', 'talentotres', 'niveltaltres', 'otrotalentotres']
    def __init__(self, *args, **kwargs):
        super(TalentosForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'talentos-form',
                'placeholder': f'{field.label}'
            })

class ArchivosForm(forms.ModelForm):
    class Meta:
        model = FichaJoven
        fields = ['imagenantes', 'imagendespues', 'archivojoven', 'nacionalidadjoven', 'ascendenciajoven', 'idiomamadre', 'idiomaoriginario']
    def __init__(self, *args, **kwargs):
        super(ArchivosForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'archivos-form',
                'placeholder': f'{field.label}'
            })

class UsuaruioForm(forms.ModelForm):
    class Meta:
        model = PerfilUsuario
        fields = ['usuario', 'departamento', 'es_encargado_nacional', 'es_encargado', 'es_asistente']