from django.shortcuts import render


def Accueil(request) :
    context={

    }
    return render(request, 'Accueil', context)