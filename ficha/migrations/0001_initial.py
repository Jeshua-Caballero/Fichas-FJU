# Generated by Django 5.1 on 2024-08-26 21:06

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FichaJovenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto_del_joven', models.ImageField(upload_to='')),
                ('nombre', models.CharField(max_length=100)),
                ('sexo', models.CharField(max_length=50)),
                ('fecha_de_nacimiento', models.DateField()),
                ('edad', models.IntegerField()),
                ('iglesia', models.CharField(max_length=150)),
                ('tribu', models.CharField(max_length=50)),
                ('como_conocio_la_iglesia', models.CharField(max_length=100)),
                ('estado_civil', models.CharField(max_length=50)),
                ('familia_en_iglesia', models.BooleanField(default=False)),
                ('hijos', models.BooleanField(default=False)),
                ('conyuge', models.BooleanField(default=False)),
                ('quienes_son_familiares', models.TextField()),
                ('canatidad_de_hijos', models.IntegerField()),
                ('codicion_del_joven', models.TextField()),
                ('testimonio', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('telfijo', models.IntegerField()),
                ('telcelular', models.IntegerField()),
                ('whatsapp', models.IntegerField()),
                ('telegram', models.CharField(max_length=150)),
                ('instagram', models.CharField(max_length=150)),
                ('facebook', models.CharField(max_length=150)),
                ('linkedin', models.CharField(max_length=150)),
                ('youtube', models.CharField(max_length=150)),
                ('tiktok', models.CharField(max_length=150)),
                ('direccion', models.CharField(max_length=250)),
                ('nro_casa', models.IntegerField()),
                ('barrio', models.CharField(max_length=250)),
                ('ciudad', models.CharField(max_length=150)),
                ('tipo_de_vivienda', models.CharField(max_length=250)),
                ('otro_tipo_de_vivienda', models.CharField(max_length=250)),
                ('tvotra', models.CharField(max_length=250)),
                ('tconvivencia', models.CharField(max_length=150)),
                ('tcotra', models.CharField(max_length=150)),
                ('fechaingiglesia', models.DateField()),
                ('fechaingfju', models.DateField()),
                ('pregbautaguas', models.BooleanField(default=False)),
                ('fecbautaguas', models.TextField()),
                ('mombautaguas', models.TextField()),
                ('obautaguas', models.TextField()),
                ('pregbautEspirituSanto', models.BooleanField(default=False)),
                ('fecbautEspSanto', models.DateField()),
                ('expbautEspSanto', models.TextField()),
                ('actobra', models.BooleanField(default=False)),
                ('tiempoobra', models.IntegerField()),
                ('servAltar', models.BooleanField(default=False)),
                ('compintellimen', models.BooleanField(default=False)),
                ('tiempointelli', models.CharField(max_length=150)),
                ('probactual', models.CharField(max_length=150)),
                ('probsup', models.CharField(max_length=150)),
                ('probactualotro', models.CharField(max_length=150)),
                ('psupotro', models.CharField(max_length=150)),
                ('eapartado', models.BooleanField(default=False)),
                ('porqueapart', models.CharField(max_length=250)),
                ('fecapart', models.DateField()),
                ('encconDios', models.BooleanField(default=False)),
                ('obspastor', models.TextField()),
                ('proyjoven', models.CharField(max_length=150)),
                ('funproyjoven', models.CharField(max_length=150)),
                ('nivproyjoven', models.CharField(max_length=150)),
                ('fecingproyjoven', models.CharField(max_length=150)),
                ('respjoven', models.CharField(max_length=150)),
                ('nivestudiojoven', models.CharField(max_length=150)),
                ('estestudiojoven', models.CharField(max_length=150)),
                ('areaestjoven', models.CharField(max_length=250)),
                ('tituloestjoven', models.BooleanField(default=False)),
                ('trabactualjoven', models.CharField(max_length=250)),
                ('lugartrabjoven', models.CharField(max_length=250)),
                ('tipoinsttrabjoven', models.CharField(max_length=250)),
                ('alabtrabjoven', models.CharField(max_length=250)),
                ('tipotrabjoven', models.CharField(max_length=250)),
                ('idiomauno', models.CharField(max_length=250)),
                ('niveliduno', models.CharField(max_length=250)),
                ('idiomados', models.CharField(max_length=250)),
                ('niveliddos', models.CharField(max_length=250)),
                ('idiomatres', models.CharField(max_length=250)),
                ('nivelidtres', models.CharField(max_length=250)),
                ('talentouno', models.CharField(max_length=250)),
                ('niveltaluno', models.CharField(max_length=250)),
                ('otrotalentouno', models.CharField(max_length=250)),
                ('talentodos', models.CharField(max_length=250)),
                ('niveltaldos', models.CharField(max_length=250)),
                ('otrotalentodos', models.CharField(max_length=250)),
                ('talentotres', models.CharField(max_length=250)),
                ('niveltaltres', models.CharField(max_length=250)),
                ('otrotalentotres', models.CharField(max_length=250)),
                ('imagenantes', models.ImageField(upload_to='')),
                ('imagendespues', models.ImageField(upload_to='')),
                ('archivojoven', models.CharField(max_length=150)),
                ('nacionalidadjoven', models.CharField(max_length=150)),
                ('ascendenciajoven', models.CharField(max_length=150)),
                ('usuarioqueregistro', models.CharField(max_length=250)),
                ('idiomamadre', models.CharField(max_length=250)),
                ('idiomaoriginario', models.CharField(max_length=250)),
                ('departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ficha.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='PerfiUsuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('es_encargado_nacional', models.BooleanField(default=False)),
                ('es_ecargado', models.BooleanField(default=False)),
                ('es_asistente', models.BooleanField(default=False)),
                ('departamento', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ficha.departamento')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]