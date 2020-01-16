import datetime
from django.db import models, migrations
from django.utils import timezone
from django.contrib.auth.models import User


#standartinis vezejas yra 0. Duomenu bazeje turi atitikti kaip - nera vezejo irasa

# Create your models here.
class Vezejas(models.Model):
	vezejas_main_user = models.OneToOneField(User, limit_choices_to={'groups__name': 'vezejas'})
	imones_pavadinimas = models.CharField(max_length = 100, unique = True)
	imones_kodas = models.CharField(max_length = 100, unique = True)
	imones_regsalis = models.CharField(max_length = 100)
	telefono_numeris = models.CharField(max_length = 100)
	sukurimo_data = models.DateTimeField(auto_now_add=True, blank=False, null=False)
	#Galimos Surinkimo dienos
	surinkimas_pirmadienis = models.BooleanField(default = False)
	surinkimas_antradienis = models.BooleanField(default = False)
	surinkimas_treciadienis = models.BooleanField(default = False)
	surinkimas_ketvirtadienis = models.BooleanField(default = False)
	surinkimas_penktadienis = models.BooleanField(default = False)
	surinkimas_sestadienis = models.BooleanField(default = False)
	surinkimas_sekmadienis = models.BooleanField(default = False)
	def __str__(self):
		return self.imones_pavadinimas
	def was_published_recently(self):
		return self.sukurimo_data >= timezone.now() - datetime.timedelta(days=1)


class Siuntejas (models.Model):
	siuntejas_user = models.OneToOneField(User, limit_choices_to={'groups__name': 'siuntejas'})
	siuntejo_vardas = models.CharField(max_length = 100)
	siuntejo_pavarde = models.CharField(max_length = 100)
	sukurimo_data = models.DateTimeField(auto_now_add=True, blank=False, null=False)
	siuntejo_telefonas = models.CharField(max_length = 100)
#	pag_surinkimas_pirmadienis = models.BooleanField(default = False)
#	pag_surinkimas_antradienis = models.BooleanField(default = False)
#	pag_surinkimas_treciadienis = models.BooleanField(default = False)
#	pag_surinkimas_ketvirtadienis = models.BooleanField(default = False)
#	pag_surinkimas_penktadienis = models.BooleanField(default = False)
#	pag_surinkimas_sestadienis = models.BooleanField(default = False)
#	pag_surinkimas_sekmadienis = models.BooleanField(default = False)
	def __str__(self):
		return str(self.siuntejo_vardas + self.siuntejo_pavarde)
	
	

class Salys (models.Model):
	salies_pavadinimas = models.CharField(max_length = 100, unique = True)
	def __str__(self):
		return self.salies_pavadinimas


class Miestai (models.Model):
	miesto_pavadinimas = models.CharField(max_length = 100)
	salis = models.ForeignKey(Salys)
	salis_miestas = models.CharField(max_length = 200, blank=True, unique=True)
	def save(self):
		self.salis_miestas = str(self.salis) + " - " + str(self.miesto_pavadinimas)
		super(Miestai, self).save()
	def __str__(self):
		return self.salis_miestas

def Miestai_listas():
	miestai_list_final=[]	
	miestai_list = []
	miestai_list = Miestai.objects.all().values_list('salis_miestas')
	item2=[]
	mapping = { ',':'', '(':'', ')':'', "'":''}
	for item in miestai_list:
		if item != "":
			item2 = str(item)
			for k, v in mapping.items():
				item2 = item2.replace(k, v)
			miestai_list_final.append((str(item2), str(item2)))
	miestai_list_final = sorted(miestai_list_final,key=lambda l:l[1], reverse=True)
	return miestai_list_final
	
	
class Siuntiniai (models.Model):
	siuntejas = models.ForeignKey(User, unique=False, blank=False, null=False, limit_choices_to={'groups__name': 'siuntejas'})
	vezejas = models.ForeignKey(User, unique=False, null=True, blank=True, related_name="user_vezejas", limit_choices_to={'groups__name': 'vezejas'})
	siuntinio_svoris = models.FloatField()
	siuntinio_ilgis = models.FloatField()
	siuntinio_plotis = models.FloatField()
	siuntinio_aukstis = models.FloatField()
	siuntinio_vietos_miestas = models.ForeignKey(Miestai, related_name='Miestai1', null=False, blank=False)
	siuntinio_tikslo_miestas = models.ForeignKey(Miestai, related_name='Miestai2', null=False, blank=False)
	siuntinio_apibudinimas = models.CharField(max_length = 50, null=False, blank=False)
	siuntinio_vietos_namas = models.CharField(max_length = 10, null=False, blank=False)
	siuntinio_vietos_gatve = models.CharField(max_length = 50, null=False, blank=False)
	siuntinio_vietos_pastokodas = models.CharField(max_length = 20, null=False, blank=False)
	siuntinio_tikslo_namas = models.CharField(max_length = 10, null=False, blank=False)
	siuntinio_tikslo_gatve = models.CharField(max_length = 50, null=False, blank=False)
	siuntinio_tikslo_pastokodas = models.CharField(max_length = 20, null=False, blank=False)
	gavejo_telefonas = models.CharField(max_length = 50, null=False, blank=False)
	siuntinio_stadija = models.IntegerField(default=0, null=False, blank=False)
	sukurimo_data = models.DateTimeField(auto_now_add=True, blank=False, null=False)
	pristatymo_data = models.DateTimeField(unique=False, blank=True, null=True)
	surinkimo_data = models.DateTimeField(unique=False, blank=True, null=True)
	def __str__(self):
		return "Siuntejas: " + str(self.siuntejas) + ", Vezejas: " + str(self.vezejas) + ", svoris: " + str(self.siuntinio_svoris)	
		
		

	

	
#Bellow list for froms in the format: Country - city.

