from django.conf.urls import url

from . import views
from pagrindinis import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^login_siuntejes/$', views.login_siuntejas, name='login_siuntejas'),
	url(r'^registruoti_su_siuntiniu/$', views.registruoti_su_siuntiniu, name='registruoti_su_siuntiniu'),
	url(r'^registracija_main/$', views.registracija_main, name='registracija_main'),
	url(r'^registracija_main/registruoti_siunteja/$', views.registracija_main_registruoti_siunteja, name='registracija_main_registruoti_siunteja'),
	url(r'^registracija_main/registruoti_vezeja/$', views.registracija_main_registruoti_vezeja, name='registracija_main_registruoti_vezeja'),
	url(r'^login_siuntejes/mano_siuntiniai/$', views.login_siuntejas_mano_siuntiniai, name='login_siuntejas_mano_siuntiniai'),
	url(r'^login_siuntejes/issiusti_siuntini/$', views.login_siuntejas_issiusti_siuntini, name='login_siuntejas_issiusti_siuntini'),
	url(r'^login_siuntejes/siusti_siuntini/$', views.login_siuntejas_siusti_siuntini, name='login_siuntejas_siusti_siuntini'),
	url(r'^login_siuntejes/redaguoti_siuntini/$', views.login_siuntejas_redaguoti_siuntini, name='login_siuntejas_redaguoti_siuntini'),
	url(r'^login_siuntejes/redaguoti/$', views.login_siuntejas_redaguoti, name='login_siuntejas_redaguoti'),
	url(r'^login_vezejas/$', views.login_vezejas, name='login_vezejas'),
	url(r'^login_vezejas/siuntiniu_krepselis/$', views.login_vezejas_siuntiniu_krepselis, name='login_vezejas_siuntiniu_krepselis'),
	url(r'^login_vezejas/siuntiniu_uzklausos/$', views.login_vezejas_siuntiniu_uzklausos, name='login_vezejas_siuntiniu_uzklausos'),
	url(r'^login_vezejas/siuntiniai_kelyje/$', views.login_vezejas_siuntiniai_kelyje, name='login_vezejas_siuntiniai_kelyje'),
	url(r'^login_vezejas/siuntiniai_kelyje/rusiuoti_pagal_pristatymo_duomenis/$', views.rusiuoti_pagal_pristatymo_duomenis, name='rusiuoti_pagal_pristatymo_duomenis'),
	url(r'^login_vezejas/siuntiniai_kelyje/rusiuoti_pagal_surinkimo_duomenis/$', views.rusiuoti_pagal_surinkimo_duomenis, name='rusiuoti_pagal_surinkimo_duomenis'),
	url(r'^login_vezejas/pristatyti_siuntiniai/$', views.login_vezejas_pristatyti_siuntiniai, name='login_vezejas_pristatyti_siuntiniai'),
	url(r'^logout/$', views.logout_user, name='logout_user'),
	url(r'^(?P<siuntejas_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<vezejas_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<siuntiniai_id>[0-9]+)/vote/$', views.vote, name='vote'),
	url(r'^Siunt_be_reg/$', views.siuntinys_naujas_be_reg, name='siuntinys_naujas_be_reg'),
	url(r'vartotojo_prisijungimas/$', views.vartotojo_prisijungimas, name='vartotojo_prisijungimas'),
	
	
	]
	
	
