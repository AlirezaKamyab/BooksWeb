from django.shortcuts import render, redirect
from .models import Book
from .forms import Bookform
from django.contrib import messages
from .BookManager import RemoveItemById, GetBookByUser, BooksRead
# Create your views here.
def home(request):
    if request.method == "POST":
        try:
            form = Bookform(request.POST)
            if form.is_valid:
                item = form.save()
                item.user = request.user
                item.save()
                messages.success(request, "Item is added!", 'SUCCESS')
            return redirect('home')
        except:
            messages.success(request, "Item is NOT added!\nMake sure you don't leave anything empty", 'DANGER')
            return redirect('home')

    list = GetBookByUser(request.user)
    return render(request, 'home.html', {'list' : list})

def remove(request, item_id):
    result = RemoveItemById(item_id)
    if result : messages.add_message(request, 1, "Item is deleted!", 'SUCCESS')
    messages.success(request, "Item is removed!", 'SUCCESS')
    return redirect('home')

def update(request,item_id):
    try:
        newChecked = False
        book = Book.objects.get(pk=item_id)
        newChecked = True if book.Checked == False else False
        book.Checked = newChecked
        book.save()
        messages.success(request, "{} read mode is {}!".format(book.BookName, newChecked), 'SUCCESS')
    except:
        pass
    return redirect('home')

def profile(request):
    all, read = BooksRead(request.user)
    return render(request, 'profile.html', {'all': all, 'read' : read})
