from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PerfilUsuario, FichaJoven, Departamento, GrupoEspiritual
from .forms import EditarPerfilForm, EditarFichaJoven, PrincipalForm, ContactoForm, DomicilioForm, EspiritualForm, ProyectosForm, EstudiosForm, LaboralForm, IdiomasForm, TalentosForm, ArchivosForm, UsuaruioForm
# Create your views here.

# REGISTROS Y LOGIN DE USUARIOS
def home(request):
    return render(request, 'ficha/home.html')

def registro(request):
    
    if request.method == 'GET':
        return render(request, 'ficha/registro/registro.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                form = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
                login(request, form)
                return redirect('ficha:editar_perfil')
            except IntegrityError:
                return render(request, 'ficha/registro/registro.html', {
                    'error': 'El usuario ya existe',
                    'form': UserCreationForm
                })
        else:
            return render(request, 'ficha/registro/registro.html', {
                'error': 'Las contraseñas no coinciden',
                'form': UserCreationForm
            })

@receiver(post_save, sender=User)
def crear_perfil_usuario(sender, instance, created, **kwargs):
    if created:
        # Creando perfil si no existe 
        PerfilUsuario.objects.create(usuario=instance)
    # else:
    #     # Si el perfil ya existe, no hagas nada
    #     instance.perfilusuario.save()

@receiver(post_save, sender=User)
def guardar_perfil_usuario(sender, instance, **kwargs):
    instance.perfilusuario.save()

def editar_perfil(request):
    
    if request.method =='POST':
        perfil_usuario = PerfilUsuario.objects.get(usuario=request.user)
        formulario_perfil = EditarPerfilForm(request.POST, instance=perfil_usuario )
        if formulario_perfil.is_valid():
            formulario_perfil = formulario_perfil.save(commit=False)
            # formulario_perfil.usuario = request.user
            formulario_perfil.save()
            # print(f'{formulario_perfil}___formulario')
            return redirect('ficha:login_asistente')
    else:
        return render(request, 'ficha/registro/editar_perfil.html', {
            'form': EditarPerfilForm
        })

def login_asistente(request):
    
    if request.method == 'POST':
        # print(request.POST)
        nombre_usuario = request.POST['username']
        contraseña = request.POST['password']
        usuario = authenticate(request, username=nombre_usuario, password=contraseña)
        if usuario is not None and usuario.perfilusuario.es_asistente:
            login(request, usuario)
            return redirect('ficha:inicio')
        else:
            return render(request, 'ficha/registro/login_asistente.html', { 'error': 'Datos inválidos o no eres un asistente',})
    return render(request, 'ficha/registro/login_asistente.html')

def login_encargado(request):
    
    if request.method == 'POST':
        nombre = request.POST['username']
        contraseña = request.POST['password']
        usuario = authenticate(request, username=nombre, password=contraseña)
        if usuario is not None and usuario.perfilusuario.es_encargado:
            login(request, usuario)
            return redirect('ficha:inicio')
        else:
            return render(request, 'ficha/registro/login_encargado.html', {'error': 'Datos invalidos o no eres el Encargado'})
    else:
        return render(request, 'ficha/registro/login_encargado.html')

def login_encargado_nacional(request):
    
    if request.method == 'POST':
        nombre = request.POST['username']
        contraseña = request.POST['password']
        usuario = authenticate(request, username=nombre, password=contraseña)
        if usuario is not None and usuario.is_superuser:
            login(request, usuario)
            return redirect('ficha:inicio')
        else:
            return render(request, 'ficha/registro/login_encargado_nacional.html', {'error':'Datos invalidos o no eres el Encargado Nacional'})
    else:
        return render(request, 'ficha/registro/login_encargado_nacional.html')    

def cerrar_sesion(request):
    logout(request)
    return redirect('ficha:home')

# PANEL'S DE CONTROL SEGUN EL TIPO DE USUARIO
def inicio(request, grupoespiritual_id=None): 
    
    perfil = request.user.perfilusuario
    grupoespiritual = GrupoEspiritual.objects.all()
    
    grupo_estilos = {
        "agua": {
            "bg_class": "bg-agua",
            "texto": "Jóvenes en el Grupo <br>Agua",
            "imagen": "ficha/image/gotas.png",
        },
        "aceite": {
            "bg_class": "bg-aceite",
            "texto": "Jóvenes en el Grupo <br>Aceite",
            "imagen": "ficha/image/petroleo.png",
        },
        "sal": {
            "bg_class": "bg-sal",
            "texto": "Jóvenes en el Grupo <br>Sal",
            "imagen": "ficha/image/salFB.png",
        },
        "luz": {
            "bg_class": "bg-luz",
            "texto": "Jóvenes en el Grupo <br>Luz",
            "imagen": "ficha/image/luz-de-tungsteno.png",
        },
        "altar": {
            "bg_class": "bg-altar",
            "texto": "Jóvenes que desean <br>Servir en el Altar",
            "imagen": "ficha/image/altar.png",
        },
        "registrado": {
            "bg_class": "bg-agregado",
            "texto": "Jóvenes <br>Registrados",
            "imagen": "ficha/image/addJoven.png",
        },
        "apartados": {
            "bg_class": "bg-apartado",
            "texto": "Jóvenes <br>Apartados",
            "imagen": "ficha/image/removeJoven.png",
        },
        "iglesias": {
            "bg_class": "bg-iglesias",
            "texto": "Iglesias <br>Registradas",
            "imagen": "ficha/image/iglesia.png",
        },
        # Añada mas grupos aqui si es necesario
    }

    # print(f'Este es el dict: {grupo_estilos}')Depuracion
    if perfil.es_encargado_nacional:
        
        if grupoespiritual_id:
            g_espiritual = GrupoEspiritual.objects.get(id=grupoespiritual_id)
            jovenes = FichaJoven.objects.filter(grupoespiritual=g_espiritual)
            return render(request, 'ficha/panels/jovenes.html', {'grupos': grupoespiritual, 'jovenes': jovenes, 'grupo_estilos': grupo_estilos})
        else:
            return render(request, 'ficha/panels/inicio.html', {'grupos': grupoespiritual, 'grupo_estilos': grupo_estilos})
        
    elif perfil.es_asistente or perfil.es_encargado:
        if grupoespiritual_id:
            g_espiritual = GrupoEspiritual.objects.get(id=grupoespiritual_id)
            jovenes = FichaJoven.objects.filter(grupoespiritual=g_espiritual, departamento=perfil.departamento)
            return render(request, 'ficha/panels/jovenes.html', {'grupos': grupoespiritual, 'jovenes': jovenes, 'grupo_estilos': grupo_estilos})
        else:
            return render(request, 'ficha/panels/inicio.html', {'grupos': grupoespiritual, 'grupo_estilos': grupo_estilos})
    return render(request, 'ficha/panels/inicio.html', {'grupos': grupoespiritual, 'grupo_estilos': grupo_estilos})

def panel(request, departamento_id=None):
    
    perfil = request.user.perfilusuario
    
    if perfil.es_encargado_nacional:
        departamentos = Departamento.objects.all()
        if departamento_id:
            departamento = Departamento.objects.get(id=departamento_id)
            jovenes = FichaJoven.objects.filter(departamento=departamento)
        else:
            jovenes = FichaJoven.objects.all()
        return render(request, 'ficha/panels/panel.html', {'jovenes': jovenes, 'departamentos': departamentos})
    
    elif perfil.es_asistente or perfil.es_encargado:
        jovenes = FichaJoven.objects.filter(departamento=perfil.departamento)
        return render(request, 'ficha/panels/panel.html', {'jovenes': jovenes})

def usuarios(request):
    
    usuarios_list = PerfilUsuario.objects.all()
    return render(request, 'ficha/panels/usuarios.html', {'usuarios': usuarios_list})


def crear_ficha_joven(request):
    
    if request.method == 'POST':
        usuario_created = PerfilUsuario.objects.get(usuario=request.user)
        form = EditarFichaJoven(request.POST)
        
        if form.is_valid():
            nuevo_registro = form.save(commit=False)
            nuevo_registro.usuarioqueregistro = usuario_created
            nuevo_registro.save()                   
            return render(request, 'ficha/panels/crear_ficha.html', {'form': EditarFichaJoven})
        else:
            return render(request, 'ficha/panels/crear_ficha.html', {'form': EditarFichaJoven, 'error': 'Datos invalidos'})
    else:
        return render(request, 'ficha/panels/crear_ficha.html', {'form': EditarFichaJoven})

# REGISTRAR UN JOVEN
def principal_form(request):
    
    if request.method == 'POST':
        usuario_created = PerfilUsuario.objects.get(usuario=request.user)
        form = PrincipalForm(request.POST)
        if form.is_valid():
            nuevo_registro = form.save(commit=False)
            nuevo_registro.usuarioqueregistro = usuario_created
            nuevo_registro.save()
            request.session['ficha_id'] = nuevo_registro.id
            request.session['registro_completado'] = True
            return redirect('ficha:contacto_form')
        else:
            return render(request, 'ficha/crear_ficha/principal_form.html', {'form': PrincipalForm, 'error':'Datos Invalidos'})
    else:
        return render(request, 'ficha/crear_ficha/principal_form.html', {'form': PrincipalForm})

def contacto_form(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=ficha)
        if form.is_valid():
            nuevo_registro = form.save(commit=False)
            nuevo_registro.save()
            return redirect('ficha:domicilio_form')
        else:
            return render(request, 'ficha/crear_ficha/contacto_form.html', {'form': ContactoForm, 'error': 'Datos invalidos'})
    else:
        return render(request, 'ficha/crear_ficha/contacto_form.html', {'form': ContactoForm})

def domicilio_form(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = DomicilioForm(request.POST, instance=ficha)
        
        if form.is_valid():
            completando_form = form.save(commit=False)
            completando_form.save()
            return redirect('ficha:espiritual_form')
        else:
            return render(request, 'ficha/crear_ficha/domicilio_form.html', {'form': DomicilioForm, 'error': 'Datos invalidos'})
    else:
        return render(request, 'ficha/crear_ficha/domicilio_form.html', {'form': DomicilioForm})

def espiritual_form(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = EspiritualForm(request.POST, instance=ficha)
        if form.is_valid():
            completando_form = form.save(commit=False)
            completando_form.save()
            return redirect('ficha:proyectos_form')
        else:
            return render(request, 'ficha/crear_ficha/espiritual_form.html', {'form': EspiritualForm, 'error': 'Datos invalidos'})
    else:
        return render(request, 'ficha/crear_ficha/espiritual_form.html', {'form': EspiritualForm})

def proyectos_form(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = ProyectosForm(request.POST, instance=ficha)
        
        if form.is_valid():
            completar_form = form.save(commit=False)
            completar_form.save()
            return redirect('ficha:estudio_form')
        else: 
            return render(request, 'ficha/crear_ficha/proyectos_form.html', {'form': ProyectosForm, 'error': 'Datos invalidos'})
    else:
        return render(request, 'ficha/crear_ficha/proyectos_form.html', {'form': ProyectosForm})

def estudio_form(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = EstudiosForm(request.POST, instance=ficha)
        
        if form.is_valid():
            completar_form = form.save(commit=False)
            completar_form.save()
            return redirect('ficha:laboral_form')
        else:
            return render(request, 'ficha/crear_ficha/principal_form.html', {'form': EstudiosForm, 'error': 'Datos invalidos'})
    else:
        return render(request, 'ficha/crear_ficha/principal_form.html', {'form': EstudiosForm})

def laboral_form(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = LaboralForm(request.POST, instance=ficha)
        
        if form.is_valid():
            completar_form = form.save(commit=False)
            completar_form.save()
            return redirect('ficha:idiomas_form')
        else:
            return render(request, 'ficha/crear_ficha/laboral_form.html', {'form':  LaboralForm, 'error': 'Datos invalidos'})
    else:
        return render(request, 'ficha/crear_ficha/laboral_form.html', {'form':  LaboralForm})

def idiomas_form(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = IdiomasForm(request.POST, instance=ficha)
        
        if form.is_valid():
            complatar_form = form.save(commit=False)
            complatar_form.save()
            return redirect('ficha:talentos_form')
        else:
            return render(request, 'ficha/crear_ficha/idiomas_form.html', {'form': IdiomasForm, 'error': 'Datos invalidos'})
    else:
        return render(request, 'ficha/crear_ficha/idiomas_form.html', {'form': IdiomasForm})

def talentos_form(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = TalentosForm(request.POST, instance=ficha)
        
        if form.is_valid():
            completar_form = form.save(commit=False)
            completar_form.save()
            # Deshabilirar cuadno este archivos_form
            if 'registro_completado' in request.session:
                del request.session['registro_completado']
                return redirect('ficha:panel')
            return redirect('ficha:panel')
        else:
            return render(request, 'ficha/crear_ficha/talentos_form.html', {'form': TalentosForm, 'error': 'Datos invalidos'})
    else:
        return render(request, 'ficha/crear_ficha/talentos_form.html', {'form': TalentosForm})

def archivos_form(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = ArchivosForm(request.POST, instance=ficha)
        
        if form.is_valid():
            completar_form = form.save(commit=False)
            completar_form.save()
            
            if 'registro_completado' in request.session:
                del request.session['registro_completado']
            return redirect('ficha:panel_encargado')
        else:
            return render(request, 'ficha/crear_ficha/archivos_form.html', {'form': ArchivosForm, 'error': 'Datos invalidos'})
    else:
        return render(request, 'ficha/crear_ficha/archivos_form.html', {'form': ArchivosForm})

# EDITAR FICHA
def obtener_ficha(request, ficha_id):
    
    perfil = request.user.perfilusuario
    
    if perfil.es_encargado_nacional or User.is_superuser:
        ficha = get_object_or_404(FichaJoven, pk=ficha_id)
    else:
        ficha = get_object_or_404(FichaJoven, pk=ficha_id, departamento=request.user.perfilusuario.departamento)
    request.session['ficha_id'] = ficha.id
    if request.method == 'POST':
        form = PrincipalForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            # request.session['ficha_id'] = form.id
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})
    else:
        form = PrincipalForm(instance=ficha)
        return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form})

def editar_contacto(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})
        else:
            return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form, 'error': 'Datos invalidos revise los campos a rellenar'})
    else:
        form = ContactoForm(instance=ficha)
        return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form})

def editar_domicilio(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = DomicilioForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})
        else:
            return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form, 'error': 'Datos invalidos revise los campos a rellenar'})
    else:
        form = DomicilioForm(instance=ficha)
        return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form})

def editar_espiritual(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = EspiritualForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})
        else:
            return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form, 'error': 'Datos invalidos revise los campos a rellenar'})
    else:
        form = EspiritualForm(instance=ficha)
        return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form})

def editar_proyectos(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = ProyectosForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})
        else:
            return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form, 'error': 'Datos invalidos revise los campos a rellenar'})
    else:
        form = ProyectosForm(instance=ficha)
        return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form})

def editar_estudio(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = EstudiosForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form})
        else:
            return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form, 'error': 'Datos Invalidos, revise los campos'})
    else:
        form = EstudiosForm(instance=ficha)
        return render(request, 'ficha/panels/obtener_ficha.html', {'ficha': ficha, 'form': form} )

def editar_laboral(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = LaboralForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})
        else:
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha, 'error': 'Datos Invalidos, revise los campos'})
    else:
        form = LaboralForm(instance=ficha)
        return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})

def editar_idiomas(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = IdiomasForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})
        else:
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha, 'error':'Datos Invalidos, revise los campos'})
    else:
        form = IdiomasForm(instance=ficha)
        return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})

def editar_talentos(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = TalentosForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})
        else:
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha, 'error':'Datos Invalidos, revise los campos'})
    else:
        form = TalentosForm(instance=ficha)
        return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})

def editar_archivos(request):
    
    ficha_id = request.session.get('ficha_id')
    ficha = get_object_or_404(FichaJoven, id=ficha_id)
    
    if request.method == 'POST':
        form = ArchivosForm(request.POST, instance=ficha)
        if form.is_valid():
            form.save()
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})
        else:
            return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha, 'error':'Datos Invalidos, revise los campos'})
    else:
        form = ArchivosForm(instance=ficha)
        return render(request, 'ficha/panels/obtener_ficha.html', {'form': form, 'ficha': ficha})

def editar_usuario(request, usuario_id):
    
    usuario = get_object_or_404(PerfilUsuario, id=usuario_id)
    
    if request.method == 'POST':
        form = UsuaruioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('ficha:usuarios')
        else:
            return render(request, 'ficha/panels/editar_usuario.html', {'form': form, 'usuario': usuario, 'error':'Datos Invalidos, revise los campos'})
    else:
        form = UsuaruioForm(instance=usuario)
        return render(request, 'ficha/panels/editar_usuario.html', {'form': form, 'usuario': usuario})

def eliminar_ficha(request, ficha_id):
    
    ficha = get_object_or_404(FichaJoven, pk=ficha_id, departamento=request.user.perfilusuario.departamento)
    if request.method == 'POST':
        ficha.delete()
        return redirect('ficha:panel')

# GRUPOS ESPIRITUALES
