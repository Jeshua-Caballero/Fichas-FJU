from django.urls import path
from . import views

app_name = 'ficha'

urlpatterns = [
    # Registro
    path('', views.home, name='home'),
    path('registro/', views.registro, name='registro'),
    path('editar/perfil/', views.editar_perfil, name='editar_perfil'),
    path('login/asistente/', views.login_asistente, name='login_asistente'),
    path('login/encargado/', views.login_encargado, name='login_encargado'),
    path('login/encargado/nacional/', views.login_encargado_nacional, name='login_encargado_nacional'),
    path('cerrar/sesion', views.cerrar_sesion, name='cerrar_sesion'),
    # Panel de Control
    path('ficha/inicio/', views.inicio, name='inicio'),
    path('inicio/<int:grupoespiritual_id>', views.inicio, name='inicio_grupos'),
    path('ficha/panel/de/control/', views.panel, name='panel'),
    path('panel/<int:departamento_id>/', views.panel, name='panel_departamento'),
    path('usuarios/registrados/', views.usuarios, name='usuarios'),
    path('editar/usuario/<int:usuario_id>', views.editar_usuario, name='editar_usuario'),
    # Registro de jovenes
    path('ficha/datos/principales/', views.principal_form, name='principal_form'),
    path('ficha/contacto/', views.contacto_form, name='contacto_form'),
    path('ficha/domicilio/', views.domicilio_form, name='domicilio_form'),
    path('ficha/espiritual/', views.espiritual_form, name='espiritual_form'),
    path('ficha/proyectos/', views.proyectos_form, name='proyectos_form'),
    path('ficha/estudios/', views.estudio_form, name='estudio_form'),
    path('ficha/laboral/', views.laboral_form, name='laboral_form'),
    path('ficha/idiomas/', views.idiomas_form, name='idiomas_form'),
    path('ficha/talentos/', views.talentos_form, name='talentos_form'),
    path('ficha/archivos/', views.archivos_form, name='archivos_form'),
    path('crear/ficha/joven', views.crear_ficha_joven, name='crear_ficha_joven'),
    path('ficha/<int:ficha_id>/', views.obtener_ficha, name='obtener_ficha'),
    # EDITAR FICHA
    path('editar/contacto/', views.editar_contacto, name='editar_contacto'),
    path('editar/domicilio/', views.editar_domicilio, name='editar_domicilio'),
    path('editar/espiritual/', views.editar_espiritual, name='editar_espiritual'),
    path('editar/proyectos/', views.editar_proyectos, name='editar_proyectos'),
    path('editar/estudio/', views.editar_estudio, name='editar_estudio'),
    path('editar/laboral/', views.editar_laboral, name='editar_laboral'),
    path('editar/idiomas/', views.editar_idiomas, name='editar_idiomas'),
    path('editar/talentos/', views.editar_talentos, name='editar_talentos'),
    path('editar/archivos/', views.archivos_form, name='editar_archivos'),
    # ELIMINAR FICHA
    path('ficha/<int:ficha_id>/eliminar/', views.eliminar_ficha, name='eliminar_ficha'),
]