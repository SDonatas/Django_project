#!/usr/bin/python
# vim: set fileencoding=<utf-8> :

from django import forms
from .models import Miestai, Miestai_listas, Siuntiniai, Siuntejas, Vezejas


#to be switched in migrations
#miestai_choice = [[]]
miestai_choice = Miestai_listas()
#miestai_choice = []


class Create_new_vezejas(forms.ModelForm):


	vezejo_vardas = forms.CharField(label='Kontakto vardas', max_length=100, widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	vezejo_pavarde = forms.CharField(label='Kontakto pavardė', max_length=100, widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	vezejo_slaptazodis = forms.CharField(label='Slaptažodis', max_length=50, widget=forms.PasswordInput(attrs={'class' : 'naujas_siunt_class'}))
	vezejo_elpastas = forms.EmailField(label='El.paštas', help_text='Įveskite teisingą el.pašto adresą', max_length=100, widget=forms.EmailInput(attrs={'class' : 'naujas_siunt_class'}))

	class Meta:
		model = Vezejas
		fields = ['imones_pavadinimas', 'imones_kodas', 'imones_regsalis', 'telefono_numeris']

		
		widgets = {'imones_pavadinimas': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'imones_kodas': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'imones_regsalis': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'telefono_numeris': forms.TextInput(attrs={'class' : 'naujas_siunt_class'})
				}




class Create_new_siuntejas(forms.ModelForm):


	siuntejo_slaptazodis = forms.CharField(label='Slaptažodis', max_length=50, widget=forms.PasswordInput(attrs={'class' : 'naujas_siunt_class'}))
	siuntejo_elpastas = forms.EmailField(label='El.paštas', help_text='Įveskite teisingą el.pašto adresą', max_length=100, widget=forms.EmailInput(attrs={'class' : 'naujas_siunt_class'}))

	class Meta:
		model = Siuntejas
		fields = ['siuntejo_vardas', 'siuntejo_pavarde', 'siuntejo_telefonas']
		
		widgets = {"siuntejo_vardas": forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					"siuntejo_pavarde": forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					"siuntejo_telefonas": forms.TextInput(attrs={'class' : 'naujas_siunt_class'})
				}
		
		
		
		



class SiuntiniaiForm(forms.ModelForm):

	#siuntejas
	#vezejas
	#siuntinio_vietos_miestas
	#siuntinio_tikslo_miestas
	#siuntinio_stadija
	#sukurimo_data
	#pristatymo_data
	#surinkimo_data
	
	siuntinio_vieta = forms.ChoiceField(choices=miestai_choice, widget=forms.Select(attrs={'class' : 'naujas_siunt_class'}))
	siuntinio_tikslas = forms.ChoiceField(choices=miestai_choice, widget=forms.Select(attrs={'class' : 'naujas_siunt_class'}))
	
	
	class Meta:
		model = Siuntiniai
		fields = ['siuntinio_svoris', 'siuntinio_ilgis', 'siuntinio_plotis', 'siuntinio_aukstis', 'siuntinio_apibudinimas', 'siuntinio_vietos_namas',
		'siuntinio_vietos_gatve', 'siuntinio_vietos_pastokodas', 'siuntinio_tikslo_namas', 'siuntinio_tikslo_gatve', 'siuntinio_tikslo_pastokodas',
		'gavejo_telefonas'
		#'siuntinio_vietos_miestas', 'siuntinio_tikslo_miestas' 
		]
		widgets = {"siuntinio_svoris": forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'siuntinio_ilgis': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'siuntinio_plotis': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'siuntinio_aukstis': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'siuntinio_apibudinimas': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'siuntinio_vietos_namas': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'siuntinio_vietos_gatve': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'siuntinio_vietos_pastokodas': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'siuntinio_tikslo_namas': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'siuntinio_tikslo_gatve': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'siuntinio_tikslo_pastokodas': forms.TextInput(attrs={'class' : 'naujas_siunt_class'}),
					'gavejo_telefonas': forms.TextInput(attrs={'class' : 'naujas_siunt_class'})
					
		
		
		
		
		
		
		
		}
		
		
		
		
		

#	def __init__(self, *args, **kwargs):
#		super(SiuntiniaiForm, self).__init__(*args, **kwargs)
#		self.fields['siuntinio_svoris', 'siuntinio_ilgis', 'siuntinio_plotis', 'siuntinio_aukstis', 'siuntinio_apibudinimas', 'siuntinio_vietos_namas',
#		'siuntinio_vietos_gatve', 'siuntinio_vietos_pastokodas', 'siuntinio_tikslo_namas', 'siuntinio_tikslo_gatve', 'siuntinio_tikslo_pastokodas',
#		'gavejo_telefonas'].widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'})
  





class NaujasSiuntinys(forms.Form):

	siuntinio_svoris = forms.FloatField(label='Siuntinio svoris', widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	siuntinio_ilgis = forms.FloatField(label='Siuntinio ilgis', widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	siuntinio_plotis = forms.FloatField(label='Siuntinio plotis', widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	siuntinio_aukstis = forms.FloatField(label='Siuntinio aukstis', widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	siuntinio_vieta = forms.ChoiceField(choices=miestai_choice)
	siuntinio_tikslas = forms.ChoiceField(choices=miestai_choice)
	siuntinio_apibudinimas = forms.CharField(label='Siuntinio apibudinimas', max_length=200, widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	surinkimo_namo_numeris_ar_pav = forms.CharField(label='Siuntinio apibudinimas', max_length=100, widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	surinkimo_gatves_pavadinimas = forms.CharField(label='Siuntinio apibudinimas', max_length=100, widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	surinkimo_pasto_kodas = forms.CharField(label='Siuntinio apibudinimas', max_length=10, widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	pristatymo_pasto_kodas = forms.CharField(label='Siuntinio apibudinimas', max_length=10, widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	pristatymo_gatves_pavadinimas = forms.CharField(label='Siuntinio apibudinimas', max_length=100, widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	pristatymo_namo_numeris_ar_pav = forms.CharField(label='Siuntinio apibudinimas', max_length=100, widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	gavejo_tel_numeris = forms.CharField(label='Siuntinio apibudinimas', max_length=100, widget=forms.TextInput(attrs={'class' : 'naujas_siunt_class'}))
	
	
	
class Prisijungimas_siuntejas (forms.Form):
	siuntejo_prisijungimo_vardas = forms.CharField(help_text='Prisijungimo vardas', label='Prisijungimo vardas', max_length=200, widget=forms.TextInput(attrs={'class' : 'prisijungimas_class'}))
	siuntejo_slaptazodis = forms.CharField(label='Slaptažodis', max_length=200, widget=forms.PasswordInput(attrs={'class' : 'prisijungimas_class'}))
	
	
class Zymejimas (forms.Form):
	zymeklis = forms.BooleanField (required=False, label='', widget=forms.CheckboxInput())


