from django.db import models

class SeisakuNumberModel(models.Model):
    seisaku_number = models.CharField(max_length=4, primary_key=True)   # AA98
    part_number = models.CharField(max_length=30)                       # PFR5B11
    po = models.CharField(max_length=4)                                 # P10
    # make a float field with 2 decimal places
    part_length = models.FloatField()                                   # 73.83
    gata_3 = models.BooleanField()                                      # True    
    gata_5 = models.BooleanField()                                      # False   

    def __str__(self):
        return self.seisaku_number

class FuranjiModel(models.Model):
    furanji = models.PositiveIntegerField()
    seisaku_number = models.ForeignKey('SeisakuNumberModel', on_delete=models.CASCADE)
    gata = models.CharField(max_length=2)
    condition = models.CharField(max_length=20)
    pedra = models.ForeignKey('ListaPedraModel', on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return str(self.furanji)

class PedraFabricanteModel(models.Model):
    fabricante = models.CharField(max_length=20, primary_key=True)

    def __str__(self):
        return self.fabricante

class PedraTypeModel(models.Model):
    fabricante = models.ForeignKey('PedraFabricanteModel', on_delete=models.CASCADE)
    haba = models.PositiveIntegerField()

    def __str__(self):
        return str(self.haba)

class KumikaeOperationsModel(models.Model):
    operation = models.CharField(max_length=20, primary_key=True)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.operation

class KumikaeModel(models.Model):
    date = models.DateTimeField()
    flange_montado = models.ForeignKey('FuranjiModel', on_delete=models.CASCADE, related_name='flange_montado')
    name = models.CharField(max_length=100)
    usada = models.PositiveIntegerField()  # Used quantity
    descarte = models.PositiveIntegerField()  # Discarded quantity
    flange_desmontado = models.ForeignKey('FuranjiModel', on_delete=models.CASCADE, related_name='flange_desmontado')
    feito = models.ForeignKey('KumikaeOperationsModel', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.date} - Name {self.name}"

class ListaPedraModel(models.Model):
    pedra_number = models.AutoField(primary_key=True)
    pedra_fabricante = models.ForeignKey('PedraTypeModel', on_delete=models.CASCADE)  # Updated to reflect PedraTypeModel changes
    pedra_haba = models.PositiveIntegerField()                                       # 65, 90, 95, 100, 115         
    date = models.DateField()

    def __str__(self):
        return str(self.pedra_number)
