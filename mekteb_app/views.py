from django.shortcuts import render
from .models import Muellim, Telebe

def akif_sayti(request):
    # Bazadakı bütün müəllim və tələbələri çəkirik
    butun_muellimler = Muellim.objects.all()
    butun_telebeler = Telebe.objects.all()
    
    # Onları HTML səhifəsinə göndəririk
    context = {
        'muellimler': butun_muellimler,
        'telebeler': butun_telebeler
    }
    return render(request, 'akif.html', context)