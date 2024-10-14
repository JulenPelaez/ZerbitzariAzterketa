from django.contrib import admin
from django.urls import path
from AplikazioaOsakidetza import views

urlpatterns = [
 path('', views.mediku_list, name='zerrenda-default'),
 path('admin/', admin.site.urls),
 path('Mediku/new/', views.mediku_new, name='zerrenda-mediku-new'),
 path('Mediku/ezabatu/<int:id>/', views.ezabatu_medikua, name='zerrenda-mediku-ezabatu'),
 path('Medikua/ezabatu/', views.ezabatu_zerrenda , name='medikua-ezabatu'),
 path('Medikua/zerrenda/', views.medikua_zerrenda, name='zerrenda-medikuak'),
 path('Medikua/aldatu/<int:medikua_id>/', views.medikua_aldatu, name='zerrenda-medikua-aldatu'),
 path('Paziente/list', views.paziente_list, name='zerrenda-pazienteak-ikusi'),
 path('Paziente/new/', views.paziente_new, name='zerrenda-paziente-new'),
 path('Paziente/ezabatu/', views.ezabatu_pazientea_zerrenda , name='paziente-ezabatu'),
 path('Paziente/ezabatu/<int:id>/', views.ezabatu_pazientea, name='zerrenda-paziente-ezabatu'),
 path('Pazientea/zerrenda/', views.paziente_zerrenda, name='zerrenda-pazienteak'),
 path('Pazientea/aldatu/<int:paziente_id>/', views.pazientea_aldatu, name='zerrenda-pazientea-aldatu'),
 path('Zita/berria/', views.zitak_new, name='zita-new'),
 path('Zita/ikusi/', views.zitak_ikusi, name='zitak-ikusi')

]
