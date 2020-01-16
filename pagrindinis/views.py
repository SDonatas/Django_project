from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Siuntejas, Vezejas, Siuntiniai, Miestai, Salys
from .forms import NaujasSiuntinys, Prisijungimas_siuntejas, Zymejimas, forms, SiuntiniaiForm, Create_new_siuntejas, Create_new_vezejas
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import Group, User
from datetime import datetime 







# Create your views here.
#@method_decorator(login_required)




def index(request):
	if request.user.is_authenticated():
		if request.user.groups.filter(name='vezejas').exists() == True:
			return redirect('login_vezejas')
		else:
			return redirect('login_siuntejas')
			
			#prisijunges_siuntejas_left
			
			
	else:
		template = loader.get_template('pagrindinis/index.html')
		form = SiuntiniaiForm()
		form_reg_send = Create_new_siuntejas()
		form_siunt_login = Prisijungimas_siuntejas()
		#dimensions_of_layout
		width_center = 500
		width_left = 200
		width_right = 250
		
		
		
		left_menu = 'pagrindinis/left_menu.html'
		vidurys = 'pagrindinis/vidurys_siunt_be_reg.html'
		right_menu = 'pagrindinis/right_gidas.html'
		if "just_logged_out" in request.session:
			pastaba="Jūs sėkmingai atsijungėte"
			del request.session['just_logged_out']
		elif "pastaba" in request.session:
			pastaba = request.session["pastaba"]
			del request.session["pastaba"]
		
		
		else:
				pastaba = ""

		total_table = width_center + width_left + width_right
		context = {
		'form': form,
		'form_reg_send': form_reg_send,
		'form_siunt_login': form_siunt_login,
		'left_menu':left_menu,
		'pastaba':pastaba,
		'vidurys':vidurys,
		'right_menu':right_menu,
		'width_center':width_center,
		'width_left':width_left,
		'width_right':width_right,
		'total_table':total_table
		}
		#output = ', '.join([q.siuntejo_vardas + " " + q.siuntejo_pavarde for q in paskiausi_siuntejai])
		return HttpResponse(template.render(context, request))

@login_required		
def login_vezejas(request):

	
	def prep_siuntiniu_uzklausos (number, page=0):
		
		def prep_summary_left_menu():
		
			left_summary = []
			left_summary.append("Viso užklausų")
			left_summary.append(len(Siuntiniai.objects.filter(vezejas__isnull=True).values_list('id')))
			left_summary.append("Viso siuntinių krepšelyje")
			filter_args = {}
			filter_args['vezejas']=request.user.id
			filter_args['siuntinio_stadija']=0
			
			
			left_summary.append(len(Siuntiniai.objects.filter(**filter_args).values_list('id')))
			left_summary.append("Svoris")
			svoris_q = Siuntiniai.objects.filter(**filter_args).values_list("siuntinio_svoris", flat=True)
			svoris_final = 0.0
			for matas in svoris_q:
				svoris_final = svoris_final + float(matas)
			left_summary.append(svoris_final)
			del svoris_q, svoris_final
			left_summary.append("Tūris")
			turis_q = Siuntiniai.objects.filter(**filter_args).values_list("siuntinio_ilgis", "siuntinio_plotis", "siuntinio_aukstis")
			turis_final = 0.0
						
			for daiktas in turis_q:
				turis_final = turis_final + (daiktas[0] * daiktas[1] * daiktas[2])	
			left_summary.append(turis_final)
			del turis_final, turis_q
			left_summary.append("Surenkami/vežami siuntiniai")
			filter_args = {}
			filter_args['vezejas']=request.user.id
			filter_args['siuntinio_stadija']=1
			left_summary.append(len(Siuntiniai.objects.filter(**filter_args).values_list('id')))
							
			
			
			left_summary.append("Svoris surenkamų siuntinių")
			svoris_q = Siuntiniai.objects.filter(**filter_args).values_list("siuntinio_svoris", flat=True)
			svoris_final = 0.0
			for matas in svoris_q:
				svoris_final = svoris_final + float(matas)
			left_summary.append(svoris_final)
			del svoris_q, svoris_final
			left_summary.append("Tūris surenkamų")
			turis_q = Siuntiniai.objects.filter(**filter_args).values_list("siuntinio_ilgis", "siuntinio_plotis", "siuntinio_aukstis")
			turis_final = 0.0
						
			for daiktas in turis_q:
				turis_final = turis_final + (daiktas[0] * daiktas[1] * daiktas[2])	
			left_summary.append(turis_final)
			del turis_final, turis_q
			left_summary.append("Pristatyti siuntiniai")			
			filter_args['vezejas']=request.user.id
			filter_args['siuntinio_stadija']=2
			left_summary.append(len(Siuntiniai.objects.filter(**filter_args).values_list('id')))
			del filter_args
			
			
			
			
			
			
			return left_summary
		
		#Fuction to preapre page layout list. Needs to be initiated once maxpages and page number known as inputs
		def prepare_page_layout(page, maxpages):
			
			page_layout = []
			if page + 1 >= 3:
				if page + 1 - 2  <= maxpages:
					page_layout.append(page + 1 - 2)
				if page + 1 - 1 <= maxpages:
					page_layout.append(page + 1 - 1)
				if page + 1 <= maxpages:
					page_layout.append(page + 1 - 0)
				if page + 2 <= maxpages:
					page_layout.append(page + 1 + 1)
				if page + 3 <= maxpages:
					page_layout.append(page + 1 + 2)
			else:
				if 1 <= maxpages:
					page_layout.append(1)
				if 2 <= maxpages:
					page_layout.append(2)
				if 3 <= maxpages:
					page_layout.append(3)
				if 4 <= maxpages:
					page_layout.append(4)
				if 5 <= maxpages:
					page_layout.append(5)
		
			return page_layout
		
		#function to flaten up round up float max pages and modofy page requst if after item removal there is no data. Also query limits for items
		def maxpage_page_out_of_scope(maxpages, page):
			
			if (maxpages % 1) == 0:
				maxpages = maxpages
			else:
				maxpages = maxpages - (maxpages % 1) + 1
			if (page + 1) > maxpages:
				page = maxpages - 1
			lenx = 10 * page
			lenx2 = 10 + (10 * page)
		
			return maxpages, page, lenx, lenx2
		
		#prepare summary left short info as it will be used as output as well as for following operations. this will save varaible space
		summary_left = prep_summary_left_menu()
		
		def capitalise_postcode(siuntiniu_uzklausos):
			for index, item in enumerate(siuntiniu_uzklausos):
				siuntiniu_uzklausos[index][13] = item[13].upper()
				siuntiniu_uzklausos[index][9] = item[9].upper()	
			return siuntiniu_uzklausos
		
		if number == 0:
			#maxpages = len(Siuntiniai.objects.filter(vezejas__isnull=True).values_list('id')) / 10
			maxpages = summary_left[1] / 10
			if maxpages > 0:
				maxpages, page, lenx, lenx2 = maxpage_page_out_of_scope(maxpages, page)			
				siuntiniu_uzklausos = Siuntiniai.objects.filter(vezejas__isnull=True).values_list('id', 'siuntinio_apibudinimas', 'siuntinio_plotis', 'siuntinio_aukstis', 'siuntinio_ilgis', 'siuntinio_svoris', 'siuntinio_vietos_miestas', 'siuntinio_vietos_namas', 'siuntinio_vietos_gatve', 'siuntinio_vietos_pastokodas', 'siuntinio_tikslo_miestas', 'siuntinio_tikslo_namas', 'siuntinio_tikslo_gatve', 'siuntinio_tikslo_pastokodas', 'gavejo_telefonas', 'siuntejas')[lenx:lenx2]
				siuntiniu_uzklausos = list(siuntiniu_uzklausos)
				siuntiniu_uzklausos = [list(elem) for elem in siuntiniu_uzklausos]
				siuntiniu_uzklausos = capitalise_postcode(siuntiniu_uzklausos)
				page_layout = prepare_page_layout(page, maxpages)
			else:
				page=0
				siuntiniu_uzklausos = []
				page_layout = prepare_page_layout(0, 1)
	
		elif number == 1:
			#maxpages = len(Siuntiniai.objects.filter(vezejas=request.user.id).values_list('id')) / 10
			maxpages = summary_left[3] / 10
			if maxpages > 0:
				maxpages, page, lenx, lenx2 = maxpage_page_out_of_scope(maxpages, page)
				filter_args = {}
				filter_args['vezejas']=request.user.id
				filter_args['siuntinio_stadija']=0
				siuntiniu_uzklausos = Siuntiniai.objects.filter(**filter_args).values_list('id', 'siuntinio_apibudinimas', 'siuntinio_plotis', 'siuntinio_aukstis', 'siuntinio_ilgis', 'siuntinio_svoris', 'siuntinio_vietos_miestas', 'siuntinio_vietos_namas', 'siuntinio_vietos_gatve', 'siuntinio_vietos_pastokodas', 'siuntinio_tikslo_miestas', 'siuntinio_tikslo_namas', 'siuntinio_tikslo_gatve', 'siuntinio_tikslo_pastokodas', 'gavejo_telefonas', 'siuntejas')[lenx:lenx2]
				del filter_args				
				siuntiniu_uzklausos = list(siuntiniu_uzklausos)
				siuntiniu_uzklausos = [list(elem) for elem in siuntiniu_uzklausos]
				siuntiniu_uzklausos = capitalise_postcode(siuntiniu_uzklausos)
				page_layout = prepare_page_layout(page, maxpages)
			else:
				page=0
				siuntiniu_uzklausos = []
				page_layout = prepare_page_layout(0, 1)
				
		elif number == 2 or number == 3:
			maxpages = summary_left[9] / 10
			if maxpages > 0:
				maxpages, page, lenx, lenx2 = maxpage_page_out_of_scope(maxpages, page)
				filter_args = {}
				filter_args['vezejas']=request.user.id
				filter_args['siuntinio_stadija']=1
				siuntiniu_uzklausos = Siuntiniai.objects.filter(**filter_args).values_list('id', 'siuntinio_apibudinimas', 'siuntinio_plotis', 'siuntinio_aukstis', 'siuntinio_ilgis', 'siuntinio_svoris', 'siuntinio_vietos_miestas', 'siuntinio_vietos_namas', 'siuntinio_vietos_gatve', 'siuntinio_vietos_pastokodas', 'siuntinio_tikslo_miestas', 'siuntinio_tikslo_namas', 'siuntinio_tikslo_gatve', 'siuntinio_tikslo_pastokodas', 'gavejo_telefonas', 'siuntejas')[lenx:lenx2]
				del filter_args				
				siuntiniu_uzklausos = list(siuntiniu_uzklausos)
				siuntiniu_uzklausos = [list(elem) for elem in siuntiniu_uzklausos]
				siuntiniu_uzklausos = capitalise_postcode(siuntiniu_uzklausos)
				page_layout = prepare_page_layout(page, maxpages)
				


				if number == 3:
					siuntiniu_uzklausos = sorted(siuntiniu_uzklausos, key=lambda x: (x[:][10] ,x[:][13]))
				else:
					siuntiniu_uzklausos = sorted(siuntiniu_uzklausos, key=lambda x: (x[:][6] ,x[:][9]))
				
			else:
				page=0
				siuntiniu_uzklausos = []
				page_layout = prepare_page_layout(0, 1)
		
		elif number == 4:
			#maxpages = len(Siuntiniai.objects.filter(vezejas=request.user.id).values_list('id')) / 10
			maxpages = summary_left[15] / 10
			if maxpages > 0:
				maxpages, page, lenx, lenx2 = maxpage_page_out_of_scope(maxpages, page)
				filter_args = {}
				filter_args['vezejas']=request.user.id
				filter_args['siuntinio_stadija']=2
				siuntiniu_uzklausos = Siuntiniai.objects.filter(**filter_args).values_list('id', 'siuntinio_apibudinimas', 'siuntinio_plotis', 'siuntinio_aukstis', 'siuntinio_ilgis', 'siuntinio_svoris', 'siuntinio_vietos_miestas', 'siuntinio_vietos_namas', 'siuntinio_vietos_gatve', 'siuntinio_vietos_pastokodas', 'siuntinio_tikslo_miestas', 'siuntinio_tikslo_namas', 'siuntinio_tikslo_gatve', 'siuntinio_tikslo_pastokodas', 'gavejo_telefonas', 'siuntejas')[lenx:lenx2]
				del filter_args				
				siuntiniu_uzklausos = list(siuntiniu_uzklausos)
				siuntiniu_uzklausos = [list(elem) for elem in siuntiniu_uzklausos]
				siuntiniu_uzklausos = capitalise_postcode(siuntiniu_uzklausos)
				page_layout = prepare_page_layout(page, maxpages)
			else:
				page=0
				siuntiniu_uzklausos = []
				page_layout = prepare_page_layout(0, 1)
		
		
		
		
		
		
		
		
		
		
							
			
		for index, elem in enumerate(siuntiniu_uzklausos):
			#"Sorting values for ismatavimai and deleting unneeded values
			siuntinio_ismatavimai = float(elem[2]) * float(elem[3]) * float(elem[4])
			siuntinio_ismatavimai = "{0:.1f}".format(siuntinio_ismatavimai) + "m3"
			siuntinio_ismatavimai_str = str(elem[2])+"x"+str(elem[3])+"x"+str(elem[4])
			del siuntiniu_uzklausos[index][2]
			del siuntiniu_uzklausos[index][2]
			del siuntiniu_uzklausos[index][2]
			siuntiniu_uzklausos[index].insert(2, str(siuntinio_ismatavimai)+" ("+siuntinio_ismatavimai_str+")")
			
			#sorting values for destination city and location city
			siuntiniu_uzklausos[index][4] = Miestai.objects.filter(id=siuntiniu_uzklausos[index][4]).values_list('salis_miestas', flat=True)[0]
			siuntiniu_uzklausos[index][8] = Miestai.objects.filter(id=siuntiniu_uzklausos[index][8]).values_list('salis_miestas', flat=True)[0]
			siuntiniu_uzklausos[index][5] = str(siuntiniu_uzklausos[index][5]) + " " + str(siuntiniu_uzklausos[index][6])+ ", " + str(siuntiniu_uzklausos[index][7])
			del siuntiniu_uzklausos[index][6]
			del siuntiniu_uzklausos[index][6]
			siuntiniu_uzklausos[index][7] = str(siuntiniu_uzklausos[index][7]) + " " + str(siuntiniu_uzklausos[index][8])+ ", " + str(siuntiniu_uzklausos[index][9])
			del siuntiniu_uzklausos[index][8]
			del siuntiniu_uzklausos[index][8]
			siuntiniu_uzklausos[index][8] = "Gavėjas: " + str(siuntiniu_uzklausos[index][8]) + ", Siuntėjas: " + str(Siuntejas.objects.filter(siuntejas_user=siuntiniu_uzklausos[index][9]).values_list('siuntejo_telefonas', flat=True)[0])
			del siuntiniu_uzklausos[index][9]
			
			siuntiniu_uzklausos[index].insert(9, "forma")
		
		
		#Preparing map url appendix for directions - menus - surenkami siuntiniai
		if number == 2:
			
			def rreplace(s, old, new, occurrence):
				li = s.rsplit(old, occurrence)
				return new.join(li)
		
		
			zemelapis_appendix = ""
			elem_cnt = 0
			elem_way = 0
			for elem in siuntiniu_uzklausos:
				elem_tmp = elem[5].strip()
				elem_city_country = elem[4]
				
				try:
					elem_city_country =elem_city_country.replace(" ", "+")
					elem_tmp = elem_tmp.replace(" ", "+")
				except:
					pass
				
				try:
					elem_tmp = elem_tmp[:elem_tmp.rfind(",+")+2] + elem_city_country[elem_city_country.index("+-+")+3:] + elem_tmp[elem_tmp.rfind(",+"):]
				except:
					pass
					
				if elem_cnt == 0:
					zemelapis_appendix = zemelapis_appendix + "&origin=" + elem_tmp
					elem_cnt = 1
				else:
					if elem_way == 0:
						zemelapis_appendix = zemelapis_appendix + "&waypoints=" + elem_tmp
						elem_way = 1
					else:
						zemelapis_appendix = zemelapis_appendix + "|" + elem_tmp
				
			if "|" in zemelapis_appendix:
				try:
					zemelapis_appendix = rreplace(zemelapis_appendix, "|", "&destination=", 1)
				except:
					pass
#Ability to optimise root. Seams like embebd API is not the one to use so far
#				if "&waypoints=" in zemelapis_appendix:
#					zemelapis_appendix = zemelapis_appendix.replace("&waypoints=", "&waypoints=optimize:true|")
				
			elif "&waypoints=" in zemelapis_appendix:
				try:
					zemelapis_appendix = rreplace(zemelapis_appendix, "&waypoints=", "&destination=", 1)
				except:
					pass
			elif "&origin=" in zemelapis_appendix:
				zemelapis_appendix = zemelapis_appendix + zemelapis_appendix
				zemelapis_appendix = rreplace(zemelapis_appendix, "&origin=", "&destination=", 1)
			
			
		
		elif number == 3:
		
			def rreplace(s, old, new, occurrence):
				li = s.rsplit(old, occurrence)
				return new.join(li)
		
		
			zemelapis_appendix = ""
			elem_cnt = 0
			elem_way = 0
			for elem in siuntiniu_uzklausos:
				elem_tmp = elem[7].strip()
				elem_city_country = elem[6]
				
				try:
					elem_city_country =elem_city_country.replace(" ", "+")
					elem_tmp = elem_tmp.replace(" ", "+")
				except:
					pass
					
				try:
					elem_tmp = elem_tmp[:elem_tmp.rfind(",+")+2] + elem_city_country[elem_city_country.index("+-+")+3:] + elem_tmp[elem_tmp.rfind(",+"):]
				except:
					pass
				
				if elem_cnt == 0:
					zemelapis_appendix = zemelapis_appendix + "&origin=" + elem_tmp
					elem_cnt = 1
				else:
					if elem_way == 0:
						zemelapis_appendix = zemelapis_appendix + "&waypoints=" + elem_tmp
						elem_way = 1
					else:
						zemelapis_appendix = zemelapis_appendix + "|" + elem_tmp
				
			if "|" in zemelapis_appendix:
				try:
					zemelapis_appendix = rreplace(zemelapis_appendix, "|", "&destination=", 1)
				except:
					pass
#Possible route optimisation code. For it to work need to add the direction variable, which is t
#				if "&waypoints=" in zemelapis_appendix:
#					zemelapis_appendix = zemelapis_appendix.replace("&waypoints=", "&waypoints=optimize:true|")
				
				
			elif "&waypoints=" in zemelapis_appendix:
				try:
					zemelapis_appendix = rreplace(zemelapis_appendix, "&waypoints=", "&destination=", 1)
				except:
					pass
			elif "&origin=" in zemelapis_appendix:
				zemelapis_appendix = zemelapis_appendix + zemelapis_appendix
				zemelapis_appendix = rreplace(zemelapis_appendix, "&origin=", "&destination=", 1)
					
					
					
					
			
		else:
			zemelapis_appendix = ""
		
		
		
		print (zemelapis_appendix)
		return siuntiniu_uzklausos, page_layout, page, summary_left, zemelapis_appendix
	
	
	if request.user.groups.filter(name='vezejas').exists() == True:
	
		#Getting page number
		
		if "page" in request.GET.keys():
			page = int(request.GET.get('page')) - 1
			request.session['page_requested'] = request.GET.get('page')
		elif 'page_requested' in request.session:
			page = int(request.session['page_requested']) - 1
	
		else:
			page = 0
		
		def delete_session_variables():
			if 'sort_type' in request.session:
				del request.session['sort_type']
		
		def prepare_dictionary_for_sortings(siuntiniu_uzklausos, sort=0):
			
			siuntiniu_uzklausos_dic = {}
			
			if sort==0:
				for list_item in siuntiniu_uzklausos:
					if list_item[4] in siuntiniu_uzklausos_dic.keys():
						siuntiniu_uzklausos_dic[list_item[4]].append(list_item)
					else:
						siuntiniu_uzklausos_dic[list_item[4]]=[list_item]
			else:
				for list_item in siuntiniu_uzklausos:
					if list_item[6] in siuntiniu_uzklausos_dic.keys():
						siuntiniu_uzklausos_dic[list_item[6]].append(list_item)
					else:
						siuntiniu_uzklausos_dic[list_item[6]]=[list_item]
						
			return siuntiniu_uzklausos_dic
			
			
			
			
		
		
	
		if 'menu_requested' in request.session:
			if request.session['menu_requested']=="siuntiniu_krepselis":
				vidurys = 'pagrindinis/prisijunges_vezejas_siuntiniu_krepselis.html'
				#del request.session['menu_requested']				
				siuntiniu_uzklausos, page_layout, page, summary_left, zemelapis_appendix = prep_siuntiniu_uzklausos(1, page)
				delete_session_variables()
				
			elif request.session['menu_requested']=="siuntiniu_uzklausos":
				vidurys = 'pagrindinis/prisijunges_vezejas_siuntiniu_uzklausos.html'
				#del request.session['menu_requested'
				siuntiniu_uzklausos, page_layout, page, summary_left, zemelapis_appendix = prep_siuntiniu_uzklausos(0, page)
				delete_session_variables()
				
			elif request.session['menu_requested']=="siuntiniai_kelyje":
				vidurys = 'pagrindinis/prisijunges_vezejas_surenkami_siuntiniai.html'
				#del request.session['menu_requested']
				if 'sort_type' in request.session:
					if request.session['sort_type'] == "pagal_pristatymo_duomenis":
						siuntiniu_uzklausos, page_layout, page, summary_left, zemelapis_appendix = prep_siuntiniu_uzklausos(3, page)
						sort_type = 1
					else:
						siuntiniu_uzklausos, page_layout, page, summary_left, zemelapis_appendix = prep_siuntiniu_uzklausos(2, page)
						sort_type = 0
				else:
					siuntiniu_uzklausos, page_layout, page, summary_left, zemelapis_appendix = prep_siuntiniu_uzklausos(2, page)
					sort_type=0						
				#translate siuntiniu uzklausos to dictionary, with key country, and value - 2d list
								
							
				siuntiniu_uzklausos = prepare_dictionary_for_sortings(siuntiniu_uzklausos, sort_type)
						
			elif request.session['menu_requested']=="pristatyti_siuntiniai":
				vidurys = 'pagrindinis/prisijunges_vezejas_pristatyti_siuntiniai.html'			
				siuntiniu_uzklausos, page_layout, page, summary_left, zemelapis_appendix = prep_siuntiniu_uzklausos(4, page)
				delete_session_variables()	
			
			
			
			
					
			
			else:
				vidurys = 'pagrindinis/prisijunges_vezejas_siuntiniu_uzklausos.html'
				siuntiniu_uzklausos, page_layout, page, summary_left, zemelapis_appendix = prep_siuntiniu_uzklausos(0, page)
				
		else:
			vidurys = 'pagrindinis/prisijunges_vezejas_siuntiniu_uzklausos.html'
			siuntiniu_uzklausos, page_layout, page, summary_left, zemelapis_appendix = prep_siuntiniu_uzklausos(0, page)
	

		width_center = 700
		width_left = 200
		width_right = 250
		login_full_name = str(request.user.first_name) + " " + str(request.user.last_name)
		if login_full_name in [None, "", " "]:
			login_full_name = str(request.user.username)
		template = loader.get_template('pagrindinis/index.html')
		left_menu = 'pagrindinis/prisijunges_vezejas_left.html'
		right_menu = 'pagrindinis/prisijunges_siuntejas_right_gidas_mano_siuntos.html'
		if 'sort_type' not in locals():
			sort_type=0
		
		
		
		
		total_table = width_center + width_left + width_right
		context = {
		'left_menu':left_menu,
		'vidurys':vidurys,
		'right_menu':right_menu,
		'login_full_name':login_full_name,
		'siuntiniu_uzklausos':siuntiniu_uzklausos,
		'width_center':width_center,
		'width_left':width_left,
		'width_right':width_right,
		'page_layout':page_layout,
		'page':page,
		'summary_left':summary_left,
		'sort_type':sort_type,
		'total_table':total_table,
		'zemelapis_appendix':zemelapis_appendix
		}
		return HttpResponse(template.render(context, request))
	
	else:
		return redirect('index')


def rusiuoti_pagal_surinkimo_duomenis(request):
	
	request.session['sort_type'] = "pagal_surinkimo_duomenis"
	if 'page_requested' in request.session:
			del request.session['page_requested']
	
	return redirect('login_vezejas')





def rusiuoti_pagal_pristatymo_duomenis(request):
	
	request.session['sort_type'] = "pagal_pristatymo_duomenis"
	if 'page_requested' in request.session:
			del request.session['page_requested']
	
	return redirect('login_vezejas')



@login_required
def login_vezejas_pristatyti_siuntiniai(request):

	def generate_siuntiniu_uzklausos():
		siuntiniu_uzklausos = Siuntiniai.objects.filter(vezejas=request.user.id, siuntinio_stadija=2).values_list('id')
		siuntiniu_uzklausos = list(siuntiniu_uzklausos)
		siuntiniu_uzklausos = [list(elem) for elem in siuntiniu_uzklausos]
		return siuntiniu_uzklausos
	
	
	
	if "submit" in request.POST.keys():
		if request.POST.get('submit') == "atsaukti":
			siuntiniu_uzklausos = generate_siuntiniu_uzklausos()
			
			for key in request.POST.keys():
				#del request.session[key]
				for index, x in enumerate(siuntiniu_uzklausos):
					if str(key)=="ID"+str(siuntiniu_uzklausos[index][0]) and request.POST.get(key)=="True":
						Siuntiniai.objects.filter(id=siuntiniu_uzklausos[index][0]).update(siuntinio_stadija=1, pristatymo_data=None)
			
			request.session['menu_requested'] = "pristatyti_siuntiniai"
			return redirect('login_vezejas')

	else:
		request.session['menu_requested'] = "pristatyti_siuntiniai"
		if 'page_requested' in request.session:
				del request.session['page_requested']
		return redirect('login_vezejas')		
		
		
@login_required		
def login_vezejas_siuntiniai_kelyje(request):
	
	def generate_siuntiniu_uzklausos():
		siuntiniu_uzklausos = Siuntiniai.objects.filter(vezejas=request.user.id, siuntinio_stadija=1).values_list('id')
		siuntiniu_uzklausos = list(siuntiniu_uzklausos)
		siuntiniu_uzklausos = [list(elem) for elem in siuntiniu_uzklausos]
		return siuntiniu_uzklausos
	
	if "submit" in request.POST.keys():
		if request.POST.get('submit') == "atsaukti":
			siuntiniu_uzklausos = generate_siuntiniu_uzklausos()
			
			for key in request.POST.keys():
				#del request.session[key]
				for index, x in enumerate(siuntiniu_uzklausos):
					if str(key)=="ID"+str(siuntiniu_uzklausos[index][0]) and request.POST.get(key)=="True":
						Siuntiniai.objects.filter(id=siuntiniu_uzklausos[index][0]).update(siuntinio_stadija=0, pristatymo_data=None, surinkimo_data=None)
			
			request.session['menu_requested'] = "siuntiniai_kelyje"
			return redirect('login_vezejas')
			
			
		elif request.POST.get('submit') == "tik_pazymeti_pristatyti":
			siuntiniu_uzklausos = generate_siuntiniu_uzklausos()
			for key in request.POST.keys():
				for index, x in enumerate(siuntiniu_uzklausos):
					if str(key)=="ID"+str(siuntiniu_uzklausos[index][0]) and request.POST.get(key)=="True":
						Siuntiniai.objects.filter(id=siuntiniu_uzklausos[index][0]).update(siuntinio_stadija=2, pristatymo_data=datetime.now())
			
			#Delete variables and return page
			del siuntiniu_uzklausos
			request.session['menu_requested'] = "siuntiniai_kelyje"
			return redirect('login_vezejas')
	
		elif request.POST.get('submit') == "visi_pristatyti":
			siuntiniu_uzklausos = generate_siuntiniu_uzklausos()
			
			for index, x in enumerate(siuntiniu_uzklausos):
				Siuntiniai.objects.filter(id=siuntiniu_uzklausos[index][0]).update(siuntinio_stadija=2, pristatymo_data=datetime.now())
			
			
			#Delete variables and return page
			del siuntiniu_uzklausos
			
			request.session['menu_requested'] = "siuntiniai_kelyje"
			return redirect('login_vezejas')
			
			
			
			
	
	
	else:
		request.session['menu_requested'] = "siuntiniai_kelyje"
		if 'page_requested' in request.session:
				del request.session['page_requested']
		return redirect('login_vezejas')	
		
		
	
		
		
@login_required		
def login_vezejas_siuntiniu_krepselis(request):
	
	def generate_siuntiniu_uzklausos():
		siuntiniu_uzklausos = Siuntiniai.objects.filter(vezejas=request.user.id, siuntinio_stadija=0).values_list('id')
		siuntiniu_uzklausos = list(siuntiniu_uzklausos)
		siuntiniu_uzklausos = [list(elem) for elem in siuntiniu_uzklausos]
		return siuntiniu_uzklausos
		
	
	if "submit" in request.POST.keys():
		if request.POST.get('submit') == "atsaukti":
			siuntiniu_uzklausos = Siuntiniai.objects.filter(vezejas=request.user.id).values_list('id')
			siuntiniu_uzklausos = list(siuntiniu_uzklausos)
			siuntiniu_uzklausos = [list(elem) for elem in siuntiniu_uzklausos]
			
			
			for key in request.POST.keys():
				#del request.session[key]
				for index, x in enumerate(siuntiniu_uzklausos):
					if str(key)=="ID"+str(siuntiniu_uzklausos[index][0]) and request.POST.get(key)=="True":
						Siuntiniai.objects.filter(id=siuntiniu_uzklausos[index][0]).update(vezejas=None, siuntinio_stadija=0, surinkimo_data=None, pristatymo_data=None)
			
			#Delete variables and return page
			del siuntiniu_uzklausos
			request.session['menu_requested'] = "siuntiniu_krepselis"
			return redirect('login_vezejas')
	
		elif request.POST.get('submit') == "tik_pazymetus_vezimas":
			siuntiniu_uzklausos = generate_siuntiniu_uzklausos()
			for key in request.POST.keys():
				for index, x in enumerate(siuntiniu_uzklausos):
					if str(key)=="ID"+str(siuntiniu_uzklausos[index][0]) and request.POST.get(key)=="True":
						Siuntiniai.objects.filter(id=siuntiniu_uzklausos[index][0]).update(siuntinio_stadija=1, surinkimo_data=datetime.now(), pristatymo_data=None)
			
			#Delete variables and return page
			del siuntiniu_uzklausos
			request.session['menu_requested'] = "siuntiniu_krepselis"
			return redirect('login_vezejas')
		
		elif request.POST.get('submit') == "visus_vezimas":
			siuntiniu_uzklausos = generate_siuntiniu_uzklausos()
#			maxpages_tmp = len(siuntiniu_uzklausos) / 10
#			if (maxpages_tmp % 1) == 0:
#				maxpages_tmp = maxpages_tmp
#			else:
#				maxpages_tmp = maxpages_tmp - (maxpages_tmp % 1) + 1
#			
#			
#			if 'page_requested' in request.session:
#				if maxpages_tmp >= int(request.session['page_requested']):
#					page_tmp = int(request.session['page_requested']) - 1
#				else:
#					page_tmp = 0
#			else:
#				page_tmp = 0
#			
#			lenx_tmp = 10 * page_tmp
#			lenx2_tmp = 10 + (10 * page_tmp)
#			
			for index, x in enumerate(siuntiniu_uzklausos):
				Siuntiniai.objects.filter(id=siuntiniu_uzklausos[index][0]).update(siuntinio_stadija=1, surinkimo_data=datetime.now(), pristatymo_data=None)
			
			
			#Delete variables and return page
			del siuntiniu_uzklausos
			
			request.session['menu_requested'] = "siuntiniu_krepselis"
			return redirect('login_vezejas')
		
	
	else:
		request.session['menu_requested'] = "siuntiniu_krepselis"
		if 'page_requested' in request.session:
			del request.session['page_requested']
		return redirect('login_vezejas')

	
@login_required		
def login_vezejas_siuntiniu_uzklausos(request):
	
	if "submit" in request.POST.keys():
		siuntiniu_uzklausos = Siuntiniai.objects.filter(vezejas__isnull=True).values_list('id')
		siuntiniu_uzklausos = list(siuntiniu_uzklausos)
		siuntiniu_uzklausos = [list(elem) for elem in siuntiniu_uzklausos]
		
		
		for key in request.POST.keys():
			#del request.session[key]
			for index, x in enumerate(siuntiniu_uzklausos):
				if str(key)=="ID"+str(siuntiniu_uzklausos[index][0]) and request.POST.get(key)=="True":
					Siuntiniai.objects.filter(id=siuntiniu_uzklausos[index][0]).update(vezejas=request.user.id)
			
		return redirect('login_vezejas')
	
	else:
		request.session['menu_requested'] = "siuntiniu_uzklausos"
		if 'page_requested' in request.session:
			del request.session['page_requested']
		return redirect('login_vezejas')	


		
@login_required
def login_siuntejas(request):

	def prep_siuntiniai(z_set=0, z_id=0):
		if z_set==0:
			siuntiniai_data = Siuntiniai.objects.filter(siuntejas=int(request.user.id)).values_list('id', 'siuntinio_apibudinimas', 'vezejas', 'surinkimo_data', 'pristatymo_data')
		else:
			siuntiniai_data = Siuntiniai.objects.filter(siuntejas=int(request.user.id), pk=z_id).values_list('id', 'siuntinio_apibudinimas', 'vezejas', 'surinkimo_data', 'pristatymo_data')
		siuntiniai_data = list(siuntiniai_data)
		siuntiniai_data = [list(elem) for elem in siuntiniai_data]
		for z, x in enumerate(siuntiniai_data):
			if x[2] is None:
				siuntiniai_data[z][2] = "Ieškomas"
				siuntiniai_data[z].insert(3,"-")
				if z_set==0:
					siuntiniai_data[z].append("Redaguoti")
			else:
				try:
					temp_vezejas = Vezejas.objects.filter(id=int(siuntiniai_data[z][2])).values_list('imones_pavadinimas', 'telefono_numeris')[0]
				except:
					temp_vezejas = "Klaida"
				siuntiniai_data[z][2] = temp_vezejas[0]
				siuntiniai_data[z].insert(3, temp_vezejas[1])
				if z_set==0:
					if x[5] is None or x[5]=="":
						if x[4] is None or x[4]=="":
							siuntiniai_data[z].append("Redaguoti")
						else:
							siuntiniai_data[z].append("Surenkamas")
					else:
						siuntiniai_data[z].append("Įvertink vežėją")
			if x[4] is not None and x[4]!="":
				siuntiniai_data[z][4] = x[4].strftime('%Y-%m-%d %H:%M')
			if x[5] is not None and x[5]!="":
				siuntiniai_data[z][5] = x[5].strftime('%Y-%m-%d %H:%M')
			
			
			
			
				
		return siuntiniai_data
	
	#Once again check that user has access to siuntejas group
	if request.user.groups.filter(name='siuntejas').exists() == True:	
		
		if "pirmas_prisijungimas" in request.session:
			if 'Naujos_siuntos_id' in request.session:
				siuntiniai_data = prep_siuntiniai(1, request.session['Naujos_siuntos_id'])
				vidurys = 'pagrindinis/prisijunges_siuntejas_reg_ir_issiustas_conf.html'
				del request.session['Naujos_siuntos_id']
				form = []
				width_center = 500
				width_left = 200
				width_right = 250
				del request.session['pirmas_prisijungimas']
			else:
				siuntiniai_data = []
				vidurys = 'pagrindinis/prisijunges_siuntejas_reg_conf.html'
				form = []
				width_center = 500
				width_left = 200
				width_right = 250
				del request.session['pirmas_prisijungimas']
			
			
		
		else:
			if 'menu_requested' in request.session:
				if request.session['menu_requested']=="mano_siuntiniai":
					width_center = 700
					width_left = 200
					width_right = 250
					vidurys = 'pagrindinis/prisijunges_siuntejas_mano_siuntiniai.html'
					form = []
					#try:
					siuntiniai_data = prep_siuntiniai()
					#except:
					#	siuntiniai_data = []
				elif request.session['menu_requested']=="issiusti_siuntini":
					if 'Naujos_siuntos_id' in request.session:
						siuntiniai_data = prep_siuntiniai(1, request.session['Naujos_siuntos_id'])
						vidurys = 'pagrindinis/prisijunges_siuntejas_issiustas_conf.html'
						del request.session['Naujos_siuntos_id']
						form = []
						width_center = 500
						width_left = 200
						width_right = 250
					else:
					
						width_center = 500
						width_left = 200
						width_right = 250
						vidurys = 'pagrindinis/prisijunges_siuntejas_siusti_siuntini.html'
						siuntiniai_data = []
						form = SiuntiniaiForm()
						
				elif request.session['menu_requested']=="redaguoti_siuntini":
					
					width_center = 500
					width_left = 200
					width_right = 250
					
					
					if 'redaguotas_siuntinys' in request.session:
						if request.session['redaguotas_siuntinys'] == "issaugoti":
							vidurys = 'pagrindinis/prisijunges_siuntejas_redaguotas_conf.html'
							siuntiniai_data = prep_siuntiniai(1, request.session['redaguoti_siuntini'])
							del request.session['redaguotas_siuntinys'], request.session['redaguoti_siuntini'], request.session['menu_requested']
							form = []
						elif request.session['redaguotas_siuntinys'] == "atsaukti_siuntini":
							vidurys = 'pagrindinis/prisijunges_siuntejas_atsauktas_conf.html'
							siuntiniai_data = prep_siuntiniai(1, request.session['redaguoti_siuntini'])
							
							#execute deletion
							id_mod = int(request.session['redaguoti_siuntini'])
							Siuntiniai.objects.filter(pk=id_mod).delete()
							del id_mod
							
							del request.session['redaguotas_siuntinys'], request.session['redaguoti_siuntini'], request.session['menu_requested']
							form = []
							
							
					else:
					
						vidurys = 'pagrindinis/prisijunges_siuntejas_redaguoti_siuntini.html'
						siuntiniai_data = []
						id_mod = int(request.session['redaguoti_siuntini'])
						record_instance = Siuntiniai.objects.get(pk=id_mod)
						form = SiuntiniaiForm(instance=record_instance)

						
						vieta_tmp = Siuntiniai.objects.filter(pk=id_mod).values_list('siuntinio_vietos_miestas', flat=True)[0]
						form.fields['siuntinio_vieta'].initial = Miestai.objects.filter(pk=vieta_tmp).values_list('salis_miestas', flat=True)[0]
						
						tikslas_tmp = Siuntiniai.objects.filter(pk=id_mod).values_list('siuntinio_tikslo_miestas', flat=True)[0]
						form.fields['siuntinio_tikslas'].initial = Miestai.objects.filter(pk=tikslas_tmp).values_list('salis_miestas', flat=True)[0]
						
						
						del id_mod, tikslas_tmp, vieta_tmp, record_instance
					
						
						
			else:
				width_center = 700
				width_left = 200
				width_right = 250
				vidurys = 'pagrindinis/prisijunges_siuntejas_mano_siuntiniai.html'
				#try:
				siuntiniai_data = prep_siuntiniai()
				form = []
				#except:
			#	siuntiniai_data = []
			
		login_full_name = str(request.user.first_name) + " " + str(request.user.last_name)
		if login_full_name in [None, "", " "]:
			login_full_name = str(request.user.username)
		template = loader.get_template('pagrindinis/index.html')
#		form = SiuntiniaiForm()
		#form_siunt_login = Prisijungimas_siuntejas()
		left_menu = 'pagrindinis/prisijunges_siuntejas_left.html'
		right_menu = 'pagrindinis/prisijunges_siuntejas_right_gidas_mano_siuntos.html'
		#pastaba = ""
		total_table = width_center + width_left + width_right
		context = {
		'form': form,
		'left_menu':left_menu,
		'vidurys':vidurys,
		'right_menu':right_menu,
		'login_full_name':login_full_name,
		'siuntiniai_data':siuntiniai_data,
		'width_center':width_center,
		'width_left':width_left,
		'width_right':width_right,
		'total_table':total_table
		}
		return HttpResponse(template.render(context, request))
	else:
		return redirect('index')

		
def login_siuntejas_redaguoti_siuntini(request):		
		
	if request.user.groups.filter(name='siuntejas').exists() == True:
		if 'redaguoti_siuntini' in request.session:
			if request.POST.get("submit")=="issaugoti":
				id_mod = int(request.session['redaguoti_siuntini'])
				record_instance = Siuntiniai.objects.get(pk=id_mod)
				form = SiuntiniaiForm(request.POST, instance=record_instance)
				Naujas_siunt = form.save(commit=False)
				
				#Populate siuntinio vietos miestas
				vieta_tmp = form.cleaned_data['siuntinio_vieta']
				miestas_tmp_key = Miestai.objects.filter(salis_miestas=vieta_tmp).values_list('pk', flat=True)[0]
				Naujas_siunt.siuntinio_vietos_miestas = Miestai.objects.get(pk=miestas_tmp_key)
				del vieta_tmp, miestas_tmp_key
					
				#Populate siuntinio tikslo miestas
				vieta_tmp = form.cleaned_data['siuntinio_tikslas']
				miestas_tmp_key = Miestai.objects.filter(salis_miestas=vieta_tmp).values_list('pk', flat=True)[0]
				Naujas_siunt.siuntinio_tikslo_miestas  = Miestai.objects.get(pk=miestas_tmp_key)
				del vieta_tmp, miestas_tmp_key
			
				#Save_data
					
				Naujas_siunt.save()
				form.save_m2m()
			
				del Naujas_siunt, form, record_instance, id_mod
			
				request.session['redaguotas_siuntinys'] = "issaugoti"
				return redirect('login_siuntejas')
			
			elif request.POST.get("submit")=="atsaukti_siuntini":
				
				#id_mod = int(request.session['redaguoti_siuntini'])
				#Siuntiniai.objects.filter(pk=id_mod).delete()
				#del id_mod
				request.session['redaguotas_siuntinys'] = "atsaukti_siuntini"
				return redirect('login_siuntejas')
				
				
	else:	
		return redirect('login_siuntejas')
		
		
		
@login_required
def login_siuntejas_mano_siuntiniai(request):
	request.session['menu_requested'] = "mano_siuntiniai"
	return redirect('login_siuntejas')
@login_required
def login_siuntejas_issiusti_siuntini(request):
	request.session['menu_requested'] = "issiusti_siuntini"
	return redirect('login_siuntejas')

@login_required	
def login_siuntejas_redaguoti(request):
	
	if "redaguoti" in request.POST:
		request.session['redaguoti_siuntini'] = request.POST.get("redaguoti")
		request.session['menu_requested'] = "redaguoti_siuntini"
		print (request.POST.get("redaguoti"))
		return redirect('login_siuntejas')
	else:
		return redirect('login_siuntejas')
	
	
@login_required
def login_siuntejas_siusti_siuntini(request):

	if request.user.groups.filter(name='siuntejas').exists() == True:
		
		if request.method == "POST":
			form = SiuntiniaiForm(request.POST)
			if form.is_valid:
				Naujas_siunt = form.save(commit=False)
			
				#Populate siuntejas
				Naujas_siunt.siuntejas = request.user
			
				#Populate siuntinio vietos miestas
				vieta_tmp = form.cleaned_data['siuntinio_vieta']
				miestas_tmp_key = Miestai.objects.filter(salis_miestas=vieta_tmp).values_list('pk', flat=True)[0]
				Naujas_siunt.siuntinio_vietos_miestas = Miestai.objects.get(pk=miestas_tmp_key)
				del vieta_tmp, miestas_tmp_key
				
				#Populate siuntinio tikslo miestas
				vieta_tmp = form.cleaned_data['siuntinio_tikslas']
				miestas_tmp_key = Miestai.objects.filter(salis_miestas=vieta_tmp).values_list('pk', flat=True)[0]
				Naujas_siunt.siuntinio_tikslo_miestas  = Miestai.objects.get(pk=miestas_tmp_key)
				del vieta_tmp, miestas_tmp_key
				
				#Save_data
				
				Naujas_siunt.save()
				form.save_m2m()
				
				
				#extracting all variables from the form
				#siuntinio_svoris, siuntinio_ilgis, siuntinio_plotis, siuntinio_aukstis, siuntinio_vietos_miestas, siuntinio_tikslo_miestas, siuntinio_apibudinimas, siuntinio_vietos_namas, siuntinio_vietos_gatve, siuntinio_vietos_pastokodas, siuntinio_tikslo_namas, siuntinio_tikslo_gatve, siuntinio_tikslo_pastokodas, gavejo_telefonas, siuntinio_stadija, sukurimo_data, pristatymo_data, surinkimo_data, pristatymo_data, surinkimo_data
				
				#Return confirmation about new record 
				
				request.session['Naujos_siuntos_id'] = Naujas_siunt.pk
				del Naujas_siunt, form
				
				
				
				
				return redirect('login_siuntejas')
			
			return redirect('login_siuntejas')
		return redirect('login_siuntejas')
	else:
		return redirect('/pagrindinis/')

		
		
def registruoti_su_siuntiniu(request):

	if request.POST.get("submit") == "registruoti_ir_siusti":
		
		if request.method == "POST":
			form = Create_new_siuntejas(request.POST)
			if form.is_valid:
				Naujas_siuntejas = form.save(commit=False)
				elpastas= form.cleaned_data['siuntejo_elpastas'].strip()
				
				if User.objects.filter(username=elpastas).exists():
					user = User.objects.filter(username=elpastas)
					request.session["pastaba"]="Pastaba: nurodytas vartotojas su el.pašto adresu " + elpastas + " jau užregistruotas"
					return redirect('/pagrindinis/')
				else:
					u = User.objects.create_user(username=elpastas,
											email=elpastas,
											password=form.cleaned_data['siuntejo_slaptazodis'].strip(),
											first_name=form.cleaned_data['siuntejo_vardas'].strip(),
											last_name=form.cleaned_data['siuntejo_pavarde'].strip(),
											)
				
					u.save()

					g = Group.objects.get(name='siuntejas') 
					g.user_set.add(u)
					user = authenticate(username=elpastas, password=form.cleaned_data['siuntejo_slaptazodis'].strip())
					login(request, user)
					
					
					
					Naujas_siuntejas.siuntejas_user = User.objects.get(username=elpastas)
					Naujas_siuntejas.save()
					form.save_m2m()
					
					#Save Siuntinys data without Siuntejas
					
					if request.method == "POST":
						form = SiuntiniaiForm(request.POST)
						if form.is_valid:
							Naujas_siunt = form.save(commit=False)
						
							#Populate siuntejas
							Naujas_siunt.siuntejas = request.user
						
							#Populate siuntinio vietos miestas
							vieta_tmp = form.cleaned_data['siuntinio_vieta']
							miestas_tmp_key = Miestai.objects.filter(salis_miestas=vieta_tmp).values_list('pk', flat=True)[0]
							Naujas_siunt.siuntinio_vietos_miestas = Miestai.objects.get(pk=miestas_tmp_key)
							del vieta_tmp, miestas_tmp_key
							
							#Populate siuntinio tikslo miestas
							vieta_tmp = form.cleaned_data['siuntinio_tikslas']
							miestas_tmp_key = Miestai.objects.filter(salis_miestas=vieta_tmp).values_list('pk', flat=True)[0]
							Naujas_siunt.siuntinio_tikslo_miestas  = Miestai.objects.get(pk=miestas_tmp_key)
							del vieta_tmp, miestas_tmp_key
							
							#Save_data
							
							Naujas_siunt.save()
							form.save_m2m()
							
							
							#extracting all variables from the form
							#siuntinio_svoris, siuntinio_ilgis, siuntinio_plotis, siuntinio_aukstis, siuntinio_vietos_miestas, siuntinio_tikslo_miestas, siuntinio_apibudinimas, siuntinio_vietos_namas, siuntinio_vietos_gatve, siuntinio_vietos_pastokodas, siuntinio_tikslo_namas, siuntinio_tikslo_gatve, siuntinio_tikslo_pastokodas, gavejo_telefonas, siuntinio_stadija, sukurimo_data, pristatymo_data, surinkimo_data, pristatymo_data, surinkimo_data
							
							#Return confirmation about new record 
							
							request.session['Naujos_siuntos_id'] = Naujas_siunt.pk
							request.session['pirmas_prisijungimas'] = True
							del Naujas_siunt, form
							
							
							
							request.session['menu_requested']="issiusti_siuntini"
							return redirect('login_siuntejas')
						return redirect('login_siuntejas')
					return redirect('login_siuntejas')
					
			else:
				request.session["pastaba"]="Pastaba: neteisingai suvesta forma, bandykite dar kartą"
				return redirect('/pagrindinis/')
	
	
		else:
			return redirect('/pagrindinis/')
	
	
	else:
		return redirect('/pagrindinis/')



def registracija_main(request):


	template = loader.get_template('pagrindinis/registracija_main.html')

	context = {
	}
	return HttpResponse(template.render(context, request))


def registracija_main_registruoti_vezeja(request):

	if request.POST.get("submit") == "registruoti_vezeja":
		form = Create_new_vezejas(request.POST)
		if form.is_valid:
			Naujas_vezejas = form.save(commit=False)
			elpastas= form.cleaned_data['vezejo_elpastas'].strip()
	
			if User.objects.filter(username=elpastas).exists():
				user = User.objects.filter(username=elpastas)
				request.session["pastaba"]="Pastaba: nurodytas vartotojas su el.pašto adresu " + elpastas + " jau užregistruotas"
				return redirect('registracija_main_registruoti_vezeja')
			else:
				u = User.objects.create_user(username=elpastas,
										email=elpastas,
										password=form.cleaned_data['vezejo_slaptazodis'].strip(),
										first_name=form.cleaned_data['vezejo_vardas'].strip(),
										last_name=form.cleaned_data['vezejo_pavarde'].strip(),
										)
				u.save()
				g = Group.objects.get(name='vezejas') 
				g.user_set.add(u)
				user = authenticate(username=elpastas, password=form.cleaned_data['vezejo_slaptazodis'].strip())
				login(request, user)
				
				Naujas_vezejas.vezejas_main_user = User.objects.get(username=elpastas)
				Naujas_vezejas.save()
				form.save_m2m()
				
				
				
				
				del elpastas
				return redirect('login_vezejas')
		else:
			#If form is not valid
	
			pastaba = request.session["pastaba"]="Pastaba: neteisingai suvesta forma. Bandykite dar kartą"
			return redirect('registracija_main_registruoti_vezeja')
	
	
	else:

		if "pastaba" in request.session:
			pastaba = request.session["pastaba"]
			del request.session["pastaba"]
		else:
			pastaba = ""
		
		template = loader.get_template('pagrindinis/registracija_main_vezejas.html')
		form_reg_vez = Create_new_vezejas()
		context = {
		'form_reg_vez':form_reg_vez,
		'pastaba':pastaba
		}
		return HttpResponse(template.render(context, request))


	
	
def registracija_main_registruoti_siunteja(request):	

	if request.POST.get("submit")=="registruoti_siunteja":
		
		
		form = Create_new_siuntejas(request.POST)
		if form.is_valid:
			Naujas_siuntejas = form.save(commit=False)
			elpastas= form.cleaned_data['siuntejo_elpastas'].strip()
			
			if User.objects.filter(username=elpastas).exists():
				user = User.objects.filter(username=elpastas)
				request.session["pastaba"]="Pastaba: nurodytas vartotojas su el.pašto adresu " + elpastas + " jau užregistruotas"
				return redirect('registracija_main_registruoti_siunteja')
			else:
				u = User.objects.create_user(username=elpastas,
										email=elpastas,
										password=form.cleaned_data['siuntejo_slaptazodis'].strip(),
										first_name=form.cleaned_data['siuntejo_vardas'].strip(),
										last_name=form.cleaned_data['siuntejo_pavarde'].strip(),
										)
			
				u.save()
				g = Group.objects.get(name='siuntejas') 
				g.user_set.add(u)
				user = authenticate(username=elpastas, password=form.cleaned_data['siuntejo_slaptazodis'].strip())
				login(request, user)
					
					
					
				Naujas_siuntejas.siuntejas_user = User.objects.get(username=elpastas)
				Naujas_siuntejas.save()
				form.save_m2m()
				del elpastas
				
				request.session["pirmas_prisijungimas"]=True
				return redirect('login_siuntejas')
				
		
		else:
			request.session["pastaba"] = "Pastaba: neteisingai suvesta forma. Bandykite dar kartą"
			return redirect('registracija_main_registruoti_siunteja')
	
	else:
		if "pastaba" in request.session:
			pastaba = request.session["pastaba"]
			del request.session["pastaba"]
		else:
			pastaba = ""
		template = loader.get_template('pagrindinis/registracija_main_siuntejas.html')
		form_reg_send = Create_new_siuntejas()
		context = {
		'form_reg_send':form_reg_send,
		'pastaba':pastaba
		}
		return HttpResponse(template.render(context, request))
	
	
	
	
	
	
@login_required		
def logout_user(request):
	logout(request)
	request.session['just_logged_out'] = "True"
	return redirect('index')
		
		
		
		
def detail(request, siuntejas_id):
    return HttpResponse("Siuntejas %s." % question_id)

def results(request, vezejas_id):
    response = "Vezejas %s."
    return HttpResponse(response % vezejas_id)

def vote(request, siuntiniai_id):
    return HttpResponse("Siuntiniai %s." % siuntiniai_id)
	
	
	
	
	
	
	
def siuntinys_naujas_be_reg(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
        # create a form instance and populate it with data from the request:
		form = NaujasSiuntinys(request.POST)
        # check whether it's valid:
		if form.is_valid():
			# process the data in form.cleaned_data as required
			# redirect to a new URL:
			template = loader.get_template('pagrindinis/siuntinys_be_login.html')
			form2 = NaujasSiuntinys()
			context = {
			'form': form2
			}
		
			return HttpResponse(template.render(context, request))

			# return HttpResponseRedirect('/thanks/')

	# if a GET (or any other method) we'll create a blank form
	else:
		form = NaujasSiuntinys()
		return render(request, 'pagrindinis/siuntinys_be_login.html', {'form': form})
		
	
#Authentifikacija - t.y. varotojo prisijungimas pirma karta is pradinio lango
def vartotojo_prisijungimas(request):

	form_obj = Prisijungimas_siuntejas(request.POST)

	if form_obj.is_valid():
		username = form_obj.cleaned_data['siuntejo_prisijungimo_vardas']
		password = form_obj.cleaned_data['siuntejo_slaptazodis']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				if user.groups.filter(name='vezejas').exists() == True:
					login(request, user)
					return redirect('/pagrindinis/')
				else:
					login(request, user)
					return redirect('/pagrindinis/')
		
				#context = {}
				#template = loader.get_template('pagrindinis/index.html')
				#return HttpResponse(template.render(context, request))
		else:
			
			request.session["pastaba"]="Pastaba: neteisingas prisijungimo vardas arba slaptažodis"
			return redirect('/pagrindinis/')
			
			
#			template = loader.get_template('pagrindinis/index.html')
#			form = NaujasSiuntinys()
#			form_siunt_login = Prisijungimas_siuntejas()
#			left_menu = 'pagrindinis/left_menu.html'
#			vidurys = 'pagrindinis/vidurys_siunt_be_reg.html'
#			right_menu = 'pagrindinis/right_gidas.html'
#			pastaba = "Pastaba: neteisingas prisijungimo vardas arba slaptažodis"
#			width_center = 500
#			width_left = 200
#			width_right = 250
#			
#			context = {
#			'form': form,
#			'form_siunt_login': form_siunt_login,
#			'left_menu':left_menu,
#			'pastaba':pastaba,
#			'vidurys':vidurys,
#			'right_menu':right_menu,
#			'width_center':width_center,
#			'width_left':width_left,
#			'width_right':width_right,
			
			
#			}
#			template = loader.get_template('pagrindinis/index.html')
			#return HttpResponse(template.render(context, request))
#			return HttpResponse(template.render(context, request))
			
