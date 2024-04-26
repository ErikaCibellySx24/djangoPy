from django.shortcuts import render, redirect
from .models import Contato  # Importa o modelo Contato do mesmo diretório
from .agenda import Agenda

agenda = Agenda()

def main(request):
    return render(request, 'index.html')

def listar_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'agenda/listar_contatos.html', {'contatos': contatos})

def adicionar_contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        numero = request.POST.get('numero')
        Contato.objects.create(nome=nome, numero=numero)
        return redirect('listar_contatos')
    return render(request, 'agenda/adicionar_contato.html')

def editar_contato(request, nome):
    contato = Contato.objects.get(nome=nome)
    if request.method == 'POST':
        novo_numero = request.POST.get('numero')
        contato.numero = novo_numero
        contato.save()
        return redirect('listar_contatos')
    return render(request, 'agenda/editar_contato.html', {'contato': contato})

def excluir_contato(request, nome):
    Contato.objects.filter(nome=nome).delete()
    return redirect('listar_contatos')
