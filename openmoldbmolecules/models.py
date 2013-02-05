from django.db import models

# Create your models here.
#class TypeOfCompound(models.Model):
#    nameOfType = models.CharField(max_length=20)
#    def __unicode__(self):
#        return self.nameOfType

class Molecule(models.Model):
    """
    Molecule models
    Only name needed, date is added automatically
    """
    name = models.CharField(max_length=500, blank=True) # Chemical name1
    name2 = models.CharField(max_length=500, blank=True) # Chemical name2
    storageID = models.CharField(max_length=30, blank=True) # StorageID
    CAS = models.CharField(max_length=12, blank=True)
    supp1 = models.CharField(max_length=100, blank=True)
    suppID1 = models.CharField(max_length=100, blank=True)
    supp2 = models.CharField(max_length=100, blank=True)
    suppID2 = models.CharField(max_length=100, blank=True)
    supp3 = models.CharField(max_length=100, blank=True)
    suppID3 = models.CharField(max_length=100, blank=True)
    SMILES = models.CharField(max_length=500, blank=True)
    RMW = models.FloatField(null=True, blank=True, verbose_name='MW, provided by supplier') # MW
    CMW = models.FloatField(null=True, blank=True, verbose_name='MW, calculated') # from SMILES calculated MW
    CHN = models.CharField(max_length=20, blank=True, verbose_name='Brutto formula')
    HBA = models.IntegerField(null=True, blank=True, verbose_name='H-bond acceptors')
    HBD = models.IntegerField(null=True, blank=True, verbose_name='H-bond donors')
    logP = models.FloatField(null=True, blank=True)
    tpsa = models.FloatField(null=True, blank=True, verbose_name='Polar surface area')
    fingerprint = models.TextField(blank=True, verbose_name='Fingerprint') #Fingerprint disabled for now
    nrb = models.IntegerField(null=True, blank=True, verbose_name='Number of rotatable bonds')
    complexity = models.IntegerField(null=True, blank=True, verbose_name='Molecular complexity')
    amount = models.FloatField(null=True, blank=True, verbose_name='Quantity') # kolicina
    unit = models.CharField(max_length=10, blank=True, verbose_name='Unit') # enota
    comment = models.TextField(blank=True, verbose_name='Comment')
    molfile = models.TextField(blank=True, verbose_name='MolFile')
    added = models.DateField(auto_now=True, auto_now_add=True) #automatically updates date and adds date upon creation
    typeOfCompound = models.CharField(max_length=30, verbose_name='Type of compound')
    
    def __unicode__(self):
        return u'%s, %s' % (self.name, self.CAS)
    
    class Meta:
        ordering = ['name']

