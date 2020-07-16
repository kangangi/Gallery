from django.shortcuts import render
from .models import Image, Category, Location
from django.core.exceptions import ObjectDoesNotExist

def index(request):
    '''
    Displays home page
    '''
    title = "Gallery"
    images = Image.display_all_images()
    locations = Location.display_all_locations()

    return render(request, "index.html", {"title":title, "images": images, "locations": locations})

def image_search(request):
    '''
    Displays the search results page
    '''
    title = "search results"
    if "category" in request.GET and request.GET["category"]:
        searched_category = request.GET.get("category")
        try: 
            category = Category.objects.get(name__icontains = searched_category)
            searched_images = Image.search_image(category)
            message= f"{searched_category}"
            return render(request, 'search.html', {"message":message,"searched_images":searched_images, "title": title})
        except ObjectDoesNotExist:
            message = f" No items under {searched_category}"
        return render(request, 'search.html', {"message":message, "title": title})

    else:
        message = "You haven't searched for anything"
        return render(request, 'search.html', {"message":message,"title": title})

def location_images(request, location):
    '''
    Function to display images per location
    '''
    location_images = Image.filter_by_location(location)

    return render(request, 'location.html', {"location_images": location_images, "location":location})

