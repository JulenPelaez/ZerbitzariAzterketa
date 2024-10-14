from django.shortcuts import render,redirect,get_object_or_404
from .models import Paziente,Medikua,Zitak
from .forms import MedikuForm,MedikuaAldatuForm,PazienteForm,ZitakGehituForm

def mediku_list(request):
    medikuZerrenda=Medikua.objects.all()
    return render(request, 'mediku_list.html', {'medikuak':medikuZerrenda})
def mediku_new(request):
    if request.method == 'POST':
        form=MedikuForm(request.POST)
        if form.is_valid:
            mediku = form.save()
            mediku.save()
        return redirect('zerrenda-default')
    else:
        form=MedikuForm()
        return render(request, 'mediku_new.html', {'form':form})
def ezabatu_medikua(request, id):
    mediku = get_object_or_404(Medikua, id=id)
    mediku.delete()
    return redirect('medikua-ezabatu')
def ezabatu_zerrenda(request):
    medikuZerrenda = Medikua.objects.all()
    form = MedikuForm()
    return render(request, 'mediku_ezabatu.html', {'form': form, 'medikuak': medikuZerrenda})
def medikua_aldatu(request, medikua_id):
    medikua = get_object_or_404(Medikua, id=medikua_id)

    if request.method == 'POST':
        form = MedikuaAldatuForm(request.POST, instance=medikua)
        if form.is_valid():
            form.save()
            return redirect('zerrenda-default')
    else:
        form = MedikuaAldatuForm(instance=medikua)

    return render(request, 'medikua_aldatu.html', {'form': form})
def medikua_zerrenda(request):
 medikuazerrenda=Medikua.objects.all()
 return render(request, 'aukeratumedikua.html', {'medikuak':medikuazerrenda})
def paziente_list(request):
    pazienteZerrenda=Paziente.objects.all()
    return render(request, 'paziente_list.html', {'pazienteak':pazienteZerrenda})
def paziente_new(request):
    if request.method == 'POST':
        form=PazienteForm(request.POST)
        if form.is_valid:
            paziente = form.save()
            paziente.save()
        return redirect('zerrenda-pazienteak')
    else:
        form=PazienteForm()
        return render(request, 'paziente_new.html', {'form':form})
def ezabatu_pazientea(request, id):
    paziente = get_object_or_404(Paziente, id=id)
    paziente.delete()
    return redirect('paziente-ezabatu')
def ezabatu_pazientea_zerrenda(request):
    pazienteZerrenda = Paziente.objects.all()
    form = PazienteForm()
    return render(request, 'paziente_ezabatu.html', {'form': form, 'pazienteak': pazienteZerrenda})
def pazientea_aldatu(request, paziente_id):
    pazientea = get_object_or_404(Paziente, id=paziente_id)

    if request.method == 'POST':
        form = PazienteForm(request.POST, instance=pazientea)
        if form.is_valid():
            form.save()
            return redirect('zerrenda-pazienteak')
    else:
        form = PazienteForm(instance=pazientea)

    return render(request, 'pazientea_aldatu.html', {'form': form})
def paziente_zerrenda(request):
 pazienteazerrenda=Paziente.objects.all()
 return render(request, 'aukeratupazientea.html', {'pazienteak':pazienteazerrenda})

def zitak_new(request):
    if request.method == 'POST':
        form=ZitakGehituForm(request.POST)
        if form.is_valid:
            nota = form.save()
            nota.save()
        return redirect('zitak-ikusi')
    else:
        form=ZitakGehituForm()
        return render(request, 'zita_new.html', {'form':form})
def zitak_ikusi(request):
    zitakzerrenda=Zitak.objects.all()
    return render(request, 'zitakikusi.html', {'zitak':zitakzerrenda})