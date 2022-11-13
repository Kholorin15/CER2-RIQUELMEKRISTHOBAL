from django.db import models

from django.db import models

class Residencia(models.Model):
    num= models.IntegerField(unique=True,primary_key=True)
    dueno = models.CharField(max_length=50)
    telefono= models.IntegerField()
    correo= models.CharField(max_length=50)

    def str(self) -> str:
        return "Residencia "+ str(self.num)

class Correspondencia(models.Model):
    fecha_recepcion= models.DateField()
    conserje= models.CharField(max_length=50)
    remitente= models.CharField(max_length=50)
    destinatario= models.CharField(max_length=50)
    estados=(
            ("Entregado","Recibido"),
            ("No Entregado","No recibido") )
    estado=models.CharField(max_length=20, choices=estados, default="S")
    residencia= models.ForeignKey(Residencia, on_delete=models.CASCADE)
