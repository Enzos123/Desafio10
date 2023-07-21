from django.shortcuts import render, redirect
from .forms import BlogForm
from .models import Articulo

# Create your views here.
def index(request):
    return render(request, 'base.html')

# Add Blog
def create_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/search')
            except:
                pass
    else:
        form = BlogForm()
    return render(request, 'create.html', {'form':form})



# Search Blog
def retrieve_blog(request):
    articulos = Articulo.objects.all()
    return render(request,'search.html',{'articulos':articulos} )

# Update Blog
def update_blog(request,pk):
    articulos = Articulo.objects.get(id=pk)
    form = BlogForm(instance=articulos)

    if request.method == 'POST':
        form = BlogForm(request.POST, instance=articulos)
        if form.is_valid():
            form.save()
            return redirect('/search')

    context = {
        'articulos': articulos,
        'form': form,
    }
    return render(request,'update.html',context)

# Delete Blog
def delete_blog(request, pk):
    articulos = Articulo.objects.get(id=pk)

    if request.method == 'POST':
        articulos.delete()
        return redirect('/search')

    context = {
        'articulos': articulos,
    }
    return render(request, 'delete.html', context)