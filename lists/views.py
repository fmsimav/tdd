from django.shortcuts import redirect, render
from lists.models import Item, List


def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/lists/the-only-list-in-the-world/')

    items = Item.objects.all()
    return render(request, 'lists/home.html', context={'items': items})


def view_list(request):
    items = Item.objects.all()
    return render(request, 'lists/list.html', context={'items': items})


def new_list(request):

    list_ = List.objects.create(text='hobay')
    Item.objects.create(text=request.POST.get('item_text', ''), list=list_)
    return redirect('/lists/the-only-list-in-the-world/')
