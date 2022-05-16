from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from .forms import ProductionForm, ProducttypeForm
from .models import Production

# Create your views here.
def index(request):
    response = HttpResponse()
    response.writelines('<h1>This is homepage</h1>')
    response.write('Home page is here edit')
    return response

def detailview(request, id):
    prd = get_object_or_404(Production, id = id)
    return render(request, "detail.html", {"product": prd})

def viewcreate(request):
    form = ProductionForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProductionForm()
        return redirect('/list')
    return render(request, 'create.html', {'form': form})

def viewcreatetype(request):
    form = ProducttypeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = ProducttypeForm()
        return redirect('/list')
    return render(request, 'create.html', {'form': form})


def viewdelete(request, id):
    prd = get_object_or_404(Production, id = id)

    if request.method == 'POST':
        prd.delete()
        return redirect('/list')
    context = {
        'product': prd
    }
    return render(request, 'delete.html', context)

def viewupdate(request, id):
    prd = get_object_or_404(Production, id = id)
    form = ProductionForm(request.POST or None, instance=prd)

    if request.method == "POST":
        form.save()
        return redirect('/list')

    context = {'form' : form}
    return render(request, "update.html", context)

def viewlist(request):
    keyword = request.GET.get('keyword')

    if keyword:
        prds = Production.objects.filter(name__icontains = keyword)
    else:
        prds = Production.objects.all()

    context = {
        'keyword' : keyword,
        'products': prds.order_by('code')
    }
    return render(request, 'listview.html', context)

