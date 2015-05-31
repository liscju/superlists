from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    first_item = Item.objects.first()
    if first_item is not None:
        new_item_text = first_item.text
    else:
        new_item_text = ''

    return render(request,'home.html', {
        'new_item_text': new_item_text
    })