from django.shortcuts import render, redirect

from collection.models import Music

from music.forms import MusicForm



def addMusic(request): # class to add music
    form = MusicForm() # assigns form to Music

    if request.method == 'POST':
        form = MusicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('Music')
    else:
        form = MusicForm()  # assigns form to Music
    


    context = {
        "form":form #assigns context to form
    }

    return render(request, 'collection/addMusic.html', context)


    # def deleteProduct(request, pk):
