# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cancelacion(models.Model):
    idcancelacion = models.AutoField(db_column='idCancelacion', primary_key=True)  # Field name made lowercase.
    motivo = models.CharField(max_length=45)
    reservas_id_reservas = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='reservas_id_reservas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancelacion' 


class Cancha(models.Model):
    idcancha = models.AutoField(db_column='idCancha', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='canch')
    ubicacion = models.CharField(max_length=45)
    nombre = models.CharField(max_length=100,  )
    descripcion = models.TextField()
    image = models.ImageField(upload_to="Canchas/")
    precio = models.FloatField()
    estado = models.CharField(max_length=45)
    canchacol = models.CharField(db_column='Canchacol', max_length=45)  # Field name made lowercase.
    estado_idestado = models.ForeignKey('Estado', models.DO_NOTHING, db_column='Estado_idEstado', blank=True, null=True)  # Field name made lowercase.
    reservas_id_reservas = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='reservas_id_reservas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cancha'

    def __str__(self):
        return self.nombre

class Canchas(models.Model):
    idcancha = models.AutoField(db_column='idCancha', primary_key=True)  # Field name made lowercase.
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='canchas')
    ubicacion = models.CharField(max_length=45)
    nombre = models.CharField(max_length=100,  )
    telefono = models.BigIntegerField()
    correo_electronico = models.CharField(max_length=100, )
    descripcion = models.TextField()
    image = models.ImageField(upload_to="Canchas/")
    precio = models.FloatField()
    estado = models.CharField(max_length=45)
    
    def __str__(self):
        return self.nombre

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Estado(models.Model):
    idestado = models.AutoField(db_column='idEstado', primary_key=True)  # Field name made lowercase.
    disponible = models.CharField(db_column='Disponible', max_length=45, blank=True, null=True)  # Field name made lowercase.
    fuera_de_servicio = models.CharField(max_length=45, blank=True, null=True)
    reservada = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'estado'


class FranjaHorarios(models.Model):
    idfranja_horarios = models.AutoField(db_column='idFranja_horarios', primary_key=True)  # Field name made lowercase.
    hora_entrada = models.DateTimeField(db_column='Hora_entrada', blank=True, null=True)  # Field name made lowercase.
    hora_salida = models.DateTimeField(db_column='Hora_salida', blank=True, null=True)  # Field name made lowercase.
    horario_idhorario = models.ForeignKey('Horario', models.DO_NOTHING, db_column='Horario_idHorario', blank=True, null=True)  # Field name made lowercase.
    reservas_id_reservas = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='reservas_id_reservas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'franja_horarios'


class Horario(models.Model):
    idhorario = models.AutoField(db_column='idHorario', primary_key=True)  # Field name made lowercase.
    horario = models.DateTimeField()
    asignacion = models.CharField(max_length=45, blank=True, null=True)
    horario_apertura = models.DateTimeField(db_column='Horario_apertura', blank=True, null=True)  # Field name made lowercase.
    horario_cierre = models.DateTimeField(db_column='Horario_cierre')  # Field name made lowercase.
    dias = models.DateField()

    class Meta:
        managed = False
        db_table = 'horario'


class Personas(models.Model):
    idpersonas = models.AutoField(db_column='idPersonas', primary_key=True)  # Field name made lowercase.
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    direccion = models.CharField(max_length=45)
    telefono = models.BigIntegerField(blank=True, null=True)
    correo_electronico = models.CharField(max_length=100, blank=True, null=True)
    edad = models.IntegerField(blank=True, null=True)
    tipo_documento_idtipo_documento = models.ForeignKey('TipoDocumento', models.DO_NOTHING, db_column='tipo_documento_idtipo_documento', blank=True, null=True)
    tipo_persona_idtipo_persona = models.ForeignKey('TipoPersona', models.DO_NOTHING, db_column='tipo_persona_idtipo_persona', blank=True, null=True)
    reservas_id_reservas = models.ForeignKey('Reservas', models.DO_NOTHING, db_column='reservas_id_reservas', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personas'


class Reservas(models.Model):
    id_reservas = models.AutoField(primary_key=True)
    fecha_reserva = models.DateField(blank=True, null=True)
    fecha_solicitud = models.DateField(blank=True, null=True)
    cantidad_personas = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'reservas'


class Servicios(models.Model):
    idservicios = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45, blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="galeria/", null=True, blank=True)
   

    class Meta:
        managed = False
        db_table = 'servicios'


class TipoCancha(models.Model):
    idtipo_cancha = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45)
    descripcion = models.TextField(blank=True, null=True)
    num_jugadores = models.IntegerField(blank=True, null=True)
    tipo_canchacol = models.CharField(max_length=45, blank=True, null=True)
    cancha_idcancha = models.ForeignKey(Cancha, models.DO_NOTHING, db_column='Cancha_idCancha', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipo_cancha'


class TipoDocumento(models.Model):
    idtipo_documento = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_documento'


class TipoPersona(models.Model):
    idtipo_persona = models.AutoField(primary_key=True)
    descripcion = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipo_persona'


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='yorny.jpeg')
    descripcion = models.TextField()


    def  __str__(self):
         return f'Perfil de {self.user.username}'

class perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='yorny.jpeg')
    descripcion = models.TextField()


    def  __str__(self):
         return f'Perfil de {self.user.username}'
    

class post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    Timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    #class Meta:
        #ordering = ['-timestamp']

    def __str__(self):
         return f'{self.user.username}: {self.content}'  
    