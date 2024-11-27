from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Departamento(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class GrupoEspiritual(models.Model):
    nombre = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre

class PerfilUsuario(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL)
    es_encargado_nacional = models.BooleanField(default=False)
    es_encargado = models.BooleanField(default=False)
    es_asistente = models.BooleanField(default=False)
    
    @property
    def es_administrador(self):
        return self.usuario.is_staff or self.usuario.is_superuser
    
    def __str__(self):
        return f'{self.usuario, self.departamento}'

class FichaJoven(models.Model):
    foto_del_joven = models.ImageField(upload_to='imagenes/%y/%m/%d', null=True )
    nombre = models.CharField(max_length=100)
    sexo = models.CharField(max_length=50)
    fecha_de_nacimiento = models.DateField(auto_now_add=True)
    edad = models.IntegerField(default=0)
    iglesia = models.CharField(max_length=150)
    tribu = models.CharField(max_length=50)
    como_conocio_la_iglesia = models.CharField(max_length=100)
    estado_civil = models.CharField(max_length=50)
    familia_en_iglesia = models.BooleanField(default=False)
    hijos = models.BooleanField(default=False)
    conyuge = models.BooleanField(default=False)
    quienes_son_familiares = models.TextField()
    canatidad_de_hijos = models.IntegerField(default=0)
    codicion_del_joven = models.TextField()
    testimonio = models.TextField()
    # CONTACTO
    email = models.EmailField()
    telfijo = models.IntegerField(null=True)
    telcelular = models.IntegerField(null=True)
    whatsapp = models.IntegerField(null=True)
    telegram = models.CharField(max_length=150)
    instagram = models.CharField(max_length=150)
    facebook  = models.CharField(max_length=150)
    linkedin  = models.CharField(max_length=150)
    youtube = models.CharField(max_length=150)
    tiktok = models.CharField(max_length=150)
    # DOMICILIO
    direccion = models.CharField(max_length=250)
    nro_casa = models.IntegerField(null=True)
    barrio = models.CharField(max_length=250)
    ciudad = models.CharField(max_length=150)
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.SET_NULL)
    tipo_de_vivienda = models.CharField(max_length=250)
    otro_tipo_de_vivienda = models.CharField(max_length=250)
    tvotra = models.CharField(max_length=250)
    tconvivencia = models.CharField(max_length=150)
    tcotra = models.CharField(max_length=150)
    # ESPIRITUALIDAD
    fechaingiglesia = models.DateField(null=True)
    fechaingfju =  models.DateField(null=True)
    pregbautaguas = models.BooleanField(default=False)
    fecbautaguas = models.TextField()
    mombautaguas = models.TextField()
    obautaguas = models.TextField()
    pregbautEspirituSanto = models.BooleanField(default=False)
    fecbautEspSanto = models.DateField(null=True)
    expbautEspSanto = models.TextField()
    actobra = models.BooleanField(default=False)
    tiempoobra = models.IntegerField(null=True)
    servAltar = models.BooleanField(default=False)
    compintellimen = models.BooleanField(default=False)
    tiempointelli = models.CharField(max_length=150)
    probactual = models.CharField(max_length=150)
    probsup = models.CharField(max_length=150)
    probactualotro = models.CharField(max_length=150)
    psupotro = models.CharField(max_length=150)
    eapartado = models.BooleanField(default=False)
    porqueapart = models.CharField(max_length=250, blank=True)
    fecapart = models.DateField(null=True)
    encconDios = models.BooleanField(default=False)
    grupoespiritual = models.ForeignKey(GrupoEspiritual, null=True, on_delete=models.SET_NULL)
    obspastor = models.TextField()
    # PROYECTO
    proyjoven = models.CharField(max_length=150)
    funproyjoven = models.CharField(max_length=150)
    nivproyjoven = models.CharField(max_length=150)
    fecingproyjoven = models.CharField(max_length=150)
    respjoven = models.CharField(max_length=150)
    # ESTUDIO
    nivestudiojoven = models.CharField(max_length=150)
    estestudiojoven = models.CharField(max_length=150)
    areaestjoven = models.CharField(max_length=250)
    tituloestjoven = models.BooleanField(default=False)
    # LABORAL
    trabactualjoven = models.CharField(max_length=250)
    lugartrabjoven = models.CharField(max_length=250)
    tipoinsttrabjoven = models.CharField(max_length=250)
    alabtrabjoven = models.CharField(max_length=250)
    tipotrabjoven = models.CharField(max_length=250)
    # IDIOMAS
    idiomauno = models.CharField(max_length=250)
    niveliduno = models.CharField(max_length=250)
    idiomados = models.CharField(max_length=250)
    niveliddos = models.CharField(max_length=250)
    idiomatres = models.CharField(max_length=250)
    nivelidtres = models.CharField(max_length=250)
    # TALENTOS
    talentouno = models.CharField(max_length=250)
    niveltaluno = models.CharField(max_length=250)
    otrotalentouno = models.CharField(max_length=250)
    talentodos = models.CharField(max_length=250) 
    niveltaldos = models.CharField(max_length=250)
    otrotalentodos = models.CharField(max_length=250)
    talentotres = models.CharField(max_length=250)
    niveltaltres = models.CharField(max_length=250)
    otrotalentotres = models.CharField(max_length=250)
    # ARCHIVOS
    imagenantes = models.ImageField(null=True, blank=True)
    imagendespues = models.ImageField(null=True, blank=True)
    archivojoven = models.CharField(max_length=150)
    nacionalidadjoven = models.CharField(max_length=150)
    ascendenciajoven = models.CharField(max_length=150)
    usuarioqueregistro = models.ForeignKey(PerfilUsuario, null=True, on_delete=models.SET_NULL)
    idiomamadre = models.CharField(max_length=250)
    idiomaoriginario = models.CharField(max_length=250)
    
    def __str__(self):
        return f'{self.nombre, self.iglesia, self.departamento, self.grupoespiritual}'