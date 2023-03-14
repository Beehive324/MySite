from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Q 

 
from django.shortcuts import render
from collection.models import Music
from user.models import User
import webbrowser


# Create your views here.

def home_page_view(request): # home page view

    context = {} # context variable

    query = ''
    if request.GET:
        query = request.GET['q']
        context['query '] = str(query)

    blank = {}

    users = User.objects.all() #users variable assigned to all user objects
    blank['users'] = users

  

    # list_of_links = []  # creates a list of links
    # list_of_links.append("Soundcloud")
    # list_of_links.append("Instagram")
    # list_of_links.append("Youtube")
    # list_of_links.append("Depop")
    # list_of_links.append("Beatstars")
    # list_of_links.append("Purchase your tracks")
    # list_of_links.append("Linktree")
    # context['list_of_links'] = list_of_links


    # songs = Music.objects.all()
    # context['songs'] = songs


   
    return render(request, "collection/home.html", context)
    return render(request, "collection/home.html", blank)

def link_view(request): # display the links, link view

    return render(request, 'collection/links.html')




def showMusic(request): # function to display music to the web app
    products = Music.objects.all() # assigns products to every object in Music

    context = {
        'products': products # assigns context to products
    }

    return render(request, 'collection/showMusic.html', context) # links to the html page



def musicdetail(request, pk): # function to display music detail
    eachproduct = Music.objects.get(title=pk) #links eachproduct to objects in music

    context = {
        'eachProduct': eachProduct #Links context to eachproduct
    }

    return render(request, 'musicDetail/showMusic.html', context) #links to the html page


def searchBar(request): # search bar 
    if request.method == 'GET': # request method get
        query = request.GET.get('q') # assigns query to q
        if query:
            products = Music.objects.filter(title__icontains=query) # search for the music objects in the collection
            return render(request, 'collection/searchbar.html', {'products':products}) 
        else:
            print("No values to search")
            return request(request, 'collection/searchbar.html', {}) #links to the html page